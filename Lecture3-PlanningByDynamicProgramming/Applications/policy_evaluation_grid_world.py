'''
Implementation of Policy Evaluation on GridWorld environment
as explained in the course.
'''


import gym
import sys
import numpy as np

from env_grid_world import GridworldEnv


env = GridworldEnv()    
env._render()

# Initialisation
# Pi => random policy (i.e. 0.25 proba for each action)
pi = 1/env.action_space.n * np.ones((env.action_space.n, env.observation_space.n))
# v(.) => 0
v = np.zeros(env.observation_space.n)
gamma = 1
# Iterative Policy Evaluation
for i in range(100):
    # for all states
    for  s in range(env.observation_space.n):
        sum = 0
        # for all posible actions
        for a, action_prob in enumerate(pi[:,s]):
            # for all sucessive states of that given action
            for prob, next_state, reward, done in env.P[s][a]:
                sum += action_prob * (reward + gamma * prob * v[next_state]) 
        v[s] = sum   
    print(v.reshape(env.shape))
