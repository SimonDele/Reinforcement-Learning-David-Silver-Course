import gym
import numpy as np
from gym import wrappers 
from env_grid_world import GridworldEnv

def policy_evaluation(env, V, pi, gamma=1, epsilon=0.01):
    """ Return Value function of a given policy """
    delta = 100
    #V = np.zeros(env.observation_space.n) # may be we can reuse the old one and just update its value iobservation_space.ntead of starting from 0 each time
    while delta > epsilon:
        # for all states
        for  s in range(env.observation_space.n):
            sum = 0
            # for all posible actions
            for a, action_prob in enumerate(pi[s,:]):
                # for all sucessive states of that given action
                for prob, next_state, reward, _ in env.P[s][a]:
                    sum += action_prob * (reward + gamma * prob * V[next_state]) 
            delta = abs(V[s] - sum)
            V[s] = sum   
    return V

def one_step_lookahead(state, V, gamma=1):
    """ Return the action value for each action of a given state """
    A = np.zeros(env.action_space.n)
    for a in range(env.action_space.n):
        for prob, next_state, reward, _ in env.P[state][a]:
            A[a] += prob * (reward + gamma * V[next_state])
    return A


def policy_iteration(env):
    """ Policy iteration algorithm - iteratively improve a policy """
    pi = 1.0 / env.action_space.n * np.ones((env.observation_space.n, env.action_space.n))
    V = np.zeros(env.observation_space.n)
    max_iter = 2000
    gamma = 1.0 # coef for discounted rewards
    for i in range(max_iter):
        policy_stable = True        
        V = policy_evaluation(env, V, pi, gamma=gamma)
        for s in range(env.observation_space.n):
            chosen_a = np.argmax(pi[s,:])    
            action_values = one_step_lookahead(s, V, gamma=gamma)
            best_a = np.argmax(action_values)
            if chosen_a != best_a:
                policy_stable = False
            pi[s] = np.eye(env.action_space.n)[best_a]
        if policy_stable:
            break     
    return pi, V, i

def run_episode(env, policy, gamma = 1.0, render = False):
    """ Run an episode and return the total reward """
    obs = env.reset()
    total_reward = 0
    step_idx = 0
    max_iter = 2000
    n_iter = 0
    while n_iter < max_iter:
        if render:
            env._render()
        obs, reward, done , _ = env.step(np.argmax(policy[obs,:]))
        total_reward += (gamma ** step_idx * reward)
        step_idx += 1
        if done:
            break
    return total_reward

env = GridworldEnv()
pi, V, i = policy_iteration(env)
# see performance of our policy
run_episode(env, pi, gamma=1, render=True)
# print the policy 
print(np.reshape(np.argmax(pi, axis=1), env.shape))