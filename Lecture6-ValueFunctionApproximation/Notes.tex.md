# Lecture 6 : Value Function Approximation

[Lecture](https://www.youtube.com/watch?v=UoPei5o4fps&index=6&list=PLqYmG7hTraZDM-OYHWgPebj2MfCFzFObQ), [Slides](http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching_files/FA.pdf)

**Applications** :  Linear function approximation [[here]](./applications/mountain_car_linear_func_approx.py)


## Introduction

We need value function approximation to solve large problems.

So far we have represente value function by a *look up* table
* V(s)
* Q(s, a)

For large MDPs it is not scalable
* too many states/actions
* too slow to learn value of each state **separately**

Solution :
* $\hat{v} (s, w) \approx v_\pi(s)$
* $\hat{q} (s, a, w) \approx q_\pi(s,a)$
* Generalise to unseen states
* Update parameter w using MC or TD learning


### Type of value function approximation

<img src='images/types_value_func.png'>



## Incremental Methods

Update the value function in direction of the gradient given by :
* For MC, the target is the return $G_t$

$\nabla w = \alpha(G_t - \hat{v}(S_t, w)) \nabla_w\hat{v}(S_t, w)$
* For TD(0), the target is the TD target $R_{t+1} + \gamma \hat{v}(S_{t+1},w)$

$\nabla w = \alpha( \textcolor{red}{R_{t+1} + \gamma \hat{v}(S_{t+1},w)} - \hat{v}(S_t, w)) \nabla_w\hat{v}(S_t, w)$

* For $TD(\lambda)$, the target is the $\lambda$-return $G^\lambda_t$
$\nabla w = \alpha( \textcolor{red}{G_t^\lambda} - \hat{v}(S_t, w)) \nabla_w\hat{v}(S_t, w)$


We can apply supervised learning to "training data". For example : 
for MC $<(S_1, G_1), (S_2, G_2), ... >$
same idea for the other methods

### Control with Value Function Approximation

* **Policy evaluation** Approximate policy evaluation
* **Policy improvement** $\epsilon$-greedy policy improvement

### Convergence of prediction algorithm

<img src='images/convergence_algo_pred.png'>

<img src='images/convergence_algo_control.png'>

## Batch Methods

### Experience Replay 

Given experience consisting of (state, value) pairs
$ D = \{(s_1,v_1^\pi), ..., (s_t,v_t^\pi) >} $ 

Repeat : 
1. Sample state, value from experience
2. Apply stochastic gradient descent update


### Deep Q-Networks with Experience Replay 

DQN uses experience replay and fixed Q-targets
* Take action $a_t$ according to $\epsilon$-greedy policy 
* Store transition $(s_t, a_t, r_{t+1}, s_{t+1})$ in replay memory D
* Sample random mini-batch transitions $(s, a, r, s')$ from D
* Compute Q-learning targets wrt old fixed  parameters $w^-$
* Optimise MSE between Q-network and Q-learning targets

$L_i(w_i) = E_{s,a,r,s ~ D_i} [(r + \gamma \underset{a'}{max} Q(s', a', w_i^-) - Q(s, a, w_i)^2)]
* Using variant of stochastic gradient descent



### DQN in Atari 

* End to end learning of values Q(s, a) from pixels
* Input state s is stack of raw pixels from last 4 frames
* Ouput is Q(s, a)
* Reward is change in score
 