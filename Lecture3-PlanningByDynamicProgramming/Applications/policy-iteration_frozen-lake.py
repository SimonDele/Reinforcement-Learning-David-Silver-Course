import gym
import numpy as np


def policy_evaluation(env, V, pi, gamma=1, epsilon=0.1):
    """ Return Value function of a given policy """
    delta = 100
    #V = np.zeros(env.nS) # may be we can reuse the old one and just update its value instead of starting from 0 each time
    while delta > epsilon:
        # for all states
        for  s in range(env.observation_space.n):
            sum = 0
            # for all posible actions
            for a, action_prob in enumerate(pi[:,s]):
                # for all sucessive states of that given action
                for prob, next_state, reward, done in env.P[s][a]:
                    sum += action_prob * (reward + gamma * prob * V[next_state]) 
            delta = abs(V[s] - sum)
            V[s] = sum   
    return V

def update_policy(env, v, gamma=1):
    """ Update the policy given a value function """
    pi = np.zeros(env.nS)
    for s in range(env.nS):
        q_sa = np.zeros(env.nA)
        for a in range(env.nA):
            for prob, next_state, reward, _ in env.P[s][a]:
                q_sa[a] +=  gamma * prob * v[next_state]
            q_sa[a] += reward 
        pi[s] = np.argmax(q_sa)
    return pi      

def policy_iteration(env):
    pi = np.random.choice(env.nA, size = env.nS) # random policy
    V = np.zeros(env.nS)
    max_iter = 2000
    gamma = 1.0 # coef for discounted rewards
    for i in range(max_iter):
        V = policy_evaluation(env, V, pi, gamma=gamma)
        new_pi = policy_iteration(env, V, gamma=gamma)
        if (np.all(policy == new_policy)):
            print ('Policy-Iteration converged at step %d.' %(i+1))
                break
        policy = new_policy
    return policy


def run_episode(env, policy, gamma = 1.0, render = False):
    """ Runs an episode and return the total reward """
    obs = env.reset()
    total_reward = 0
    step_idx = 0
    while True:
        if render:
            env.render()
        obs, reward, done , _ = env.step(int(policy[obs]))
        total_reward += (gamma ** step_idx * reward)
        step_idx += 1
        if done:
            break
    return total_reward


def evaluate_policy(env, policy, gamma = 1.0, n = 100):
    scores = [run_episode(env, policy, gamma, False) for _ in range(n)]
    return np.mean(scores)

env = gym.make('FrozenLake5=8x8-v0')
pi = policy_iteration(env)
# see performance of pi
run_episode(env, pi, gamma=1, render=True)