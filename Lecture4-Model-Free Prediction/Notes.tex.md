# Lecture 4 : Model-Free Prediction

## Introduction

In model-free methods, the **MDP** that rules the world is **unknown**.

## Monte-Carlo (MC) Learning

MC methods learn directly from episodes of experience

MC is a model-free : no knowledge of MDP transitions/rewards

**MC learns from complete episodes : no boostrapping** 

**Goal** learn $v_\pi$ from episodes of experience under policy $\pi$. ($S_1,A_1,R_2,...,S_k ~ \pi)

Recall :
* *return* G is the total discounted reward

*G_t = R_{t+1} + \gamma R_{t+2] + ... + \gamma^{T-1} R_T*

* Value function is the expected return

$v_\pi(s) = E_\pi[G_t | S_t = s]

### First-visit Monte-Carlo Policy Evaluation

The first time-step t that state s is visited in an episode 

1. Increment counter $N(s) \leftarrow N(s) +1$

2. Increment total return with the return $S(s) \leftarrow S(s) + G_t$

3. Value is estimated by mean return V(s) = S(s) / N(s)

4. By law a large numbers, $V(s) \leftarrow v_\pi(s)$ as $N(s) \leftarrow \infty$

### Every-Visit Monte-Carlo Policy Evaluation

Every time-step t that state s is visited in an episode

1. Increment counter $N(s) \leftarrow N(s) + 1$ 
2. Increment total return $S(s) \leftarrow S(s) + G_t$
3. Value is estimated by mean return $V(s) = S(s) / N(s)
4. Again, by law a large numbers, $V(s) \leftarrow v_\pi(s)$ as $N(s) \leftarrow \infty$

**Application** on Black-jack [[here]](./Applications/monte_carlo_policy_evaluation.ipynb)




**Monte Carlo policy evaluation uses empiral mean return instead of expected return** 

## Temporal-Difference Learning

## TD($\lambda$)