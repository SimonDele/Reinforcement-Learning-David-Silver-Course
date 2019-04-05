import gym
from gym.wrappers import Monitor

import matplotlib.pyplot as plt
import numpy as np
import random

import tensorflow as tf

import keras
from keras.models import Sequential
from keras.layers import Conv2D, Flatten, Dense
from keras import callbacks
from keras.optimizers import Adam
from utils import preprocessed_img

import itertools
import sys, os
from tqdm import tqdm
import time
from collections import deque

from easy_tf_log import tflog


def updateTargetModel(model, target_model):
    weights = model.get_weights()
    target_weights = target_model.get_weights()
    for i in range(len(target_weights)):
        target_weights[i] = weights[i]
    target_model.set_weights(target_weights)

def huber_loss(y_true, y_pred):
    return tf.losses.huber_loss(y_true,y_pred)



# def updateTargetModel(model, targetModel):
#   modelWeights       = model.trainable_weights
#   targetModelWeights = targetModel.trainable_weights

#   for i in range(len(targetModelWeights)):
#     targetModelWeights[i].assign(modelWeights[i])

def build_model(input_shape, nA):
    model = Sequential()
    model.add(Dense(16, input_shape=input_shape, activation="relu"))
    # model.add(Flatten())
    model.add(Dense(16, activation="relu"))
    model.add(Dense(nA, activation="linear"))
    model.summary()
    #model.compile(optimizer='adam', loss='mse')
    model.compile(loss='mse', optimizer=Adam(lr=0.001))

    return model




def make_epsilon_greedy_policy(estimator, nA):
    """
    Creates an epsilon-greedy policy based on a given Q-function approximator and epsilon.

    Args:
        estimator: An estimator that returns q values for a given state
        nA: Number of actions in the environment.

    Returns:
        A function that takes the (sess, observation, epsilon) as an argument and returns
        the probabilities for each action in the form of a numpy array of length nA.

    """
    def policy_fn(observation, epsilon):
        A = np.ones(nA, dtype=float) * epsilon / nA
        q_values = estimator.predict(np.expand_dims(observation, 0))[0]
        best_action = np.argmax(q_values)
        A[best_action] += (1.0 - epsilon)
        return A
    return policy_fn



#def train():


### Hyperparameter
max_episodes = 40000
epsilon_start = 1.0
epsilon_end = 0.1
epsilon_decay_steps = 3000
batch_size = 32
replay_memory_init_size = 1000
replay_memory_size = 20000
update_target_weights_every = 100
discount_factor = 0.99

record_video_every = 2000

### Initialisation

monitor_path = os.path.abspath("./monitor/")
env = gym.envs.make('CartPole-v0')
nA = env.action_space.n

obs = env.reset()
t_steps = 0
replay_memory = deque(maxlen=replay_memory_size)
nA = env.action_space.n
ts = time.gmtime()
time_readable = time.strftime("%Y-%m-%d %H:%M:%S", ts)
log_dir = os.path.join('./logs/' + time_readable)
tbCallBack = callbacks.TensorBoard(log_dir=log_dir, histogram_freq=0,  
          write_graph=True, write_images=True)


print(env.observation_space.shape)
q_estimator = build_model((env.observation_space.shape[0],), nA)
target_estimator = build_model((env.observation_space.shape[0],), nA)
updateTargetModel(q_estimator, target_estimator)

policy = make_epsilon_greedy_policy(q_estimator, nA)
# epsilon decay
epsilons = np.linspace(epsilon_start, epsilon_end, epsilon_decay_steps)



#### Init replay memory
obs = env.reset()
#obs = np.stack([obs] * 4, axis=1) # one_input = 4 * obs

for _ in tqdm(range(replay_memory_init_size)):
    action_probs = policy(obs, epsilon_start)
    action = np.random.choice(np.arange(len(action_probs)), p=action_probs)

    new_obs, reward, done, _ = env.step(action)
    reward = reward #if not done else -100
    #new_obs = np.append(obs[:,1:], np.expand_dims(new_obs, 1), axis=1)
    
    replay_memory.append((obs, action, reward, new_obs, done))

    if done:
        obs = env.reset()
        #obs = np.stack([obs] * 4, axis=1) # one_input = 4 * obs
    else: 
        obs = new_obs
#env = Monitor(env, directory=monitor_path, video_callable=lambda count: count % record_video_every == 0, resume=True)

### Training Loop
for n_episode in range(max_episodes):

    obs = env.reset()
    #obs = np.stack([obs]*4, axis=1)
    eps_length = 0
    eps_reward = 0
    eps_loss = 0
    eps_avg_q = 0
    for t in itertools.count():
        # Print out which step we're on, useful for debugging.
        print("\rStep {} ({}) @ Episode {}/{}".format(
                t, t_steps, n_episode + 1, max_episodes), end="")
        sys.stdout.flush()
        
        
        # Update decaying epsilon 
        epsilon = epsilons[min(epsilon_decay_steps-1,t_steps)]
        
        # If necessary update target weights
        if t_steps % update_target_weights_every == 0:
            updateTargetModel(q_estimator, target_estimator)
        
        # Sample action
        action_probs = policy(obs, epsilon)
        action = np.random.choice(np.arange(len(action_probs)), p=action_probs)
        # Environment step
        new_obs, reward, done, _ = env.step(action)
        reward = reward # if not done else -100
        #new_obs = np.append(obs[:,1:], np.expand_dims(new_obs, axis=1), axis=1)

        replay_memory.append((obs, action, reward, new_obs, done))

        # Update episode stats
        eps_reward += reward


        # Sample a minibatch from memory
        idx = np.random.choice(np.arange(len(replay_memory)),
                               size=batch_size,
                               replace=False)
        samples = [replay_memory[ii] for ii in idx]
        
        states_batch, action_batch, rewards_batch, next_states_batch, done_batch = map(np.array, zip(*samples))        


        # Compute target
        q_values_next = q_estimator.predict(next_states_batch)
        targets = rewards_batch + (1-done_batch) * discount_factor * np.max(q_values_next, axis=1)

        # Update estimator weights
        target_f = q_estimator.predict(states_batch)
        
        for i, action in enumerate(action_batch):
            target_f[i,action] = targets[i]
    
        loss = q_estimator.train_on_batch(states_batch, target_f)

        eps_loss += loss

        obs = new_obs
        t_steps += 1

        if done:
            break
        

    tflog('avg_q', eps_avg_q / t, custom_dir=log_dir)
    tflog('running_reward', eps_reward, custom_dir=log_dir)
    tflog('eps_length', t, custom_dir=log_dir)
    tflog('epsilon', epsilon, custom_dir=log_dir)
    tflog('loss', eps_loss, custom_dir=log_dir)