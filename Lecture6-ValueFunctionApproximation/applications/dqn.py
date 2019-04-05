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


from easy_tf_log import tflog

def updateTargetModel(model, target_model):
    weights = model.get_weights()
    target_weights = target_model.get_weights()
    for i in range(len(target_weights)):
        target_weights[i] = weights[i]
    target_model.set_weights(target_weights)

def huber_loss(y_true, y_pred):
    return tf.losses.huber_loss(y_true,y_pred)

def build_model(input_shape, nA):
    model = Sequential()
    model.add(Conv2D(filters=32, kernel_size=8, strides=4, activation='relu', input_shape=input_shape))
    model.add(Conv2D(filters=64, kernel_size=4, strides=2, activation='relu'))
    model.add(Conv2D(filters=64, kernel_size=3, strides=1, activation='relu'))
    model.add(Flatten())
    model.add(Dense(256, activation='relu'))
    model.add(Dense(nA))

    model.summary()
    optimizer = Adam(lr=0.00001)
    model.compile(optimizer='adam', loss='mse')

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
max_episodes = 10000
epsilon_start = 1.0
epsilon_end = 0.1
batch_size = 32
epsilon_decay_steps = 500000
replay_memory_init_size = 20000
replay_memory_size = 30000
update_target_weights_every = 10000
discount_factor = 0.99

record_video_every = 50

### Initialisation

env = gym.envs.make('Breakout-v0')
obs = env.reset()
#env = Monitor(env, directory=monitor_path, video_callable=lambda count: count % record_video_every == 0, resume=True)

nA = env.action_space.n
print("Action Space :" + str(nA))
q_estimator = build_model((84,84,4),nA)
target_estimator = build_model((84,84,4),nA)

t_steps = 0
replay_memory = []
nA = env.action_space.n
ts = time.gmtime()
time_readable = time.strftime("%Y-%m-%d %H:%M:%S", ts)
log_dir = os.path.join('./logs/' + time_readable)
tbCallBack = callbacks.TensorBoard(log_dir=log_dir, histogram_freq=0,  
          write_graph=True, write_images=True)

policy = make_epsilon_greedy_policy(q_estimator, nA)
# epsilon decay
epsilons = np.linspace(epsilon_start, epsilon_end, epsilon_decay_steps)
monitor_path = os.path.abspath("./monitor/" + time_readable + "/")

#### Init replay memory
obs = preprocessed_img(obs)
obs = np.stack([obs] * 4, axis=2) # one_input = 4 * obs

for _ in tqdm(range(replay_memory_init_size)):
    action_probs = policy(obs, epsilon_start)
    action = np.random.choice(np.arange(len(action_probs)), p=action_probs)

    new_obs, reward, done, _ = env.step(action)
    new_obs = preprocessed_img(new_obs)
    new_obs = np.append(obs[:,:,1:], np.expand_dims(new_obs, 2), axis=2)
    
    replay_memory.append((obs, action, reward, new_obs, done))

    if done:
        obs = preprocessed_img(env.reset())
        obs = np.stack([obs] * 4, axis=2) # one_input = 4 * obs
    else: 
        obs = new_obs

env = Monitor(env, directory=monitor_path, video_callable=lambda count: count % record_video_every == 0, resume=True)


### Training Loop
for n_episode in range(max_episodes):

    obs = env.reset()
    obs = preprocessed_img(obs)
    obs = np.stack([obs]*4, axis=2)
    eps_length = 0
    eps_reward = 0
    eps_loss = 0
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
        new_obs = preprocessed_img(new_obs)
        new_obs = np.append(obs[:,:,1:], np.expand_dims(new_obs, axis=2), axis=2)

        if len(replay_memory) >= replay_memory_size:
            replay_memory.pop(0)

        replay_memory.append((obs, action, reward, new_obs, done))

        # Update episode stats
        eps_reward += reward


        # Sample a minibatch from memory
        samples = random.sample(replay_memory, batch_size)
        states_batch, action_batch, reward_batch, next_states_batch, done_batch = map(np.array, zip(*samples))        

        # Compute target
        #q_values_next = target_estimator.predict(next_states_batch)
        q_values_next = target_estimator.predict(next_states_batch)
        targets = reward_batch + (1-done_batch) * discount_factor * np.amax(q_values_next, axis=1)

        # Update estimator weights
        target_f = q_estimator.predict(states_batch)

        #target_f[:,action_batch] = targets
    
        for i, action in enumerate(action_batch):
            target_f[i,action] = targets[i]

        loss = q_estimator.train_on_batch(states_batch, target_f)
        
        eps_loss += loss
        
        if done:
            break
        
        obs = new_obs
        t_steps += 1

    tflog('running_reward', eps_reward, custom_dir=log_dir)
    tflog('eps_length', t, custom_dir=log_dir)
    tflog('epsilon', epsilon, custom_dir=log_dir)
    tflog('loss', eps_loss, custom_dir=log_dir)
