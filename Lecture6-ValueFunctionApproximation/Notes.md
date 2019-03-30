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
* <img src="/Lecture6-ValueFunctionApproximation/tex/2596cac35e935805daafb4e9acca3ba7.svg?invert_in_darkmode&sanitize=true" align=middle width=107.86395179999998pt height=24.65753399999998pt/>
* <img src="/Lecture6-ValueFunctionApproximation/tex/2dc9c05cf1df519b6090876b990f59a7.svg?invert_in_darkmode&sanitize=true" align=middle width=138.59451374999998pt height=24.65753399999998pt/>
* Generalise to unseen states
* Update parameter w using MC or TD learning


### Type of value function approximation

<img src='images/types_value_func.png'>



## Incremental Methods

Update the value function in direction of the gradient given by :
* For MC, the target is the return <img src="/Lecture6-ValueFunctionApproximation/tex/ab4745a27f0ed02fe9e696bcff9d032c.svg?invert_in_darkmode&sanitize=true" align=middle width=17.890435199999988pt height=22.465723500000017pt/>

<img src="/Lecture6-ValueFunctionApproximation/tex/6bfa8c6f479a77e5ac900503676c7bdb.svg?invert_in_darkmode&sanitize=true" align=middle width=247.78768244999998pt height=24.65753399999998pt/>
* For TD(0), the target is the TD target <img src="/Lecture6-ValueFunctionApproximation/tex/5e6853e84c314cb8a669c209965642e0.svg?invert_in_darkmode&sanitize=true" align=middle width=137.79963614999997pt height=24.65753399999998pt/>

<img src="/Lecture6-ValueFunctionApproximation/tex/d4917ad02fe9f18c2309075dabbae136.svg?invert_in_darkmode&sanitize=true" align=middle width=390.9579432pt height=24.65753399999998pt/>

* For <img src="/Lecture6-ValueFunctionApproximation/tex/2c1bde9ec7807d75b2da29f87a646661.svg?invert_in_darkmode&sanitize=true" align=middle width=48.33005759999999pt height=24.65753399999998pt/>, the target is the <img src="/Lecture6-ValueFunctionApproximation/tex/fd8be73b54f5436a5cd2e73ba9b6bfa9.svg?invert_in_darkmode&sanitize=true" align=middle width=9.58908224999999pt height=22.831056599999986pt/>-return <img src="/Lecture6-ValueFunctionApproximation/tex/a01f0bf6617889e4ddc741568b67f077.svg?invert_in_darkmode&sanitize=true" align=middle width=20.72149694999999pt height=27.91243950000002pt/>
<img src="/Lecture6-ValueFunctionApproximation/tex/1fabe2048c5ed12fb8237724a3cb5244.svg?invert_in_darkmode&sanitize=true" align=middle width=274.70174655pt height=27.91243950000002pt/>


We can apply supervised learning to "training data". For example : 
for MC <img src="/Lecture6-ValueFunctionApproximation/tex/046f7cfde2a75477024543a1c751ddf6.svg?invert_in_darkmode&sanitize=true" align=middle width=178.70311139999998pt height=24.65753399999998pt/>
same idea for the other methods

### Control with Value Function Approximation

* **Policy evaluation** Approximate policy evaluation
* **Policy improvement** <img src="/Lecture6-ValueFunctionApproximation/tex/7ccca27b5ccc533a2dd72dc6fa28ed84.svg?invert_in_darkmode&sanitize=true" align=middle width=6.672392099999992pt height=14.15524440000002pt/>-greedy policy improvement

### Convergence of prediction algorithm

<img src='images/convergence_algo_pred.png'>

<img src='images/convergence_algo_control.png'>

## Batch Methods

### Experience Replay 

Given experience consisting of (state, value) pairs
<img src="/Lecture6-ValueFunctionApproximation/tex/533d981d48f2470815a00194c7831271.svg?invert_in_darkmode&sanitize=true" align=middle width=193.5802176pt height=24.65753399999998pt/> 

Repeat : 
1. Sample state, value from experience
2. Apply stochastic gradient descent update


### Deep Q-Networks with Experience Replay 

DQN uses experience replay and fixed Q-targets
* Take action <img src="/Lecture6-ValueFunctionApproximation/tex/9789555e5d8fa5de21171cc40c86d2cd.svg?invert_in_darkmode&sanitize=true" align=middle width=13.65494624999999pt height=14.15524440000002pt/> according to <img src="/Lecture6-ValueFunctionApproximation/tex/7ccca27b5ccc533a2dd72dc6fa28ed84.svg?invert_in_darkmode&sanitize=true" align=middle width=6.672392099999992pt height=14.15524440000002pt/>-greedy policy 
* Store transition <img src="/Lecture6-ValueFunctionApproximation/tex/f69a027d31dca0407dfd61411afa8e16.svg?invert_in_darkmode&sanitize=true" align=middle width=122.65808939999998pt height=24.65753399999998pt/> in replay memory D
* Sample random mini-batch transitions <img src="/Lecture6-ValueFunctionApproximation/tex/63868432008a84594e0e215bedd15358.svg?invert_in_darkmode&sanitize=true" align=middle width=70.37478029999998pt height=24.7161288pt/> from D
* Compute Q-learning targets wrt old fixed  parameters <img src="/Lecture6-ValueFunctionApproximation/tex/d75649fbfd453bfa21eed2bb87fa9bf2.svg?invert_in_darkmode&sanitize=true" align=middle width=22.48486679999999pt height=26.17730939999998pt/>
* Optimise MSE between Q-network and Q-learning targets

$L_i(w_i) = E_{s,a,r,s ~ D_i} [(r + \gamma \underset{a'}{max} Q(s', a', w_i^-) - Q(s, a, w_i)^2)]
* Using variant of stochastic gradient descent



### DQN in Atari 

* End to end learning of values Q(s, a) from pixels
* Input state s is stack of raw pixels from last 4 frames
* Ouput is Q(s, a)
* Reward is change in score
 