# Lecture 2 - Markov Decision Process

[Lecture](https://www.youtube.com/watch?v=lfHX2hHRMVQ&t=4s), [Slides](http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching_files/MDP.pdf)


## Markov Process

Markov decision process *formally* describe an environment for reinforcement learning.

Where the environment is **fully** observable.

(Partially observable problems can be converted into MDPs)

**Bandits** are MDPs with one state.

### Markov property :
 <img src="https://latex.codecogs.com/gif.latex?P[S_{t+1|S_t}]=P[S_{t+1}|S_1,...,S_t]"/>


### State transition Matrix 

The state transition probablity is defined by
<img src="https://latex.codecogs.com/gif.latex?P^a_{ss'}=P[S'=s'|S=s,A=a]"/>

We can define the state transition matrix thanks to all <img src="https://latex.codecogs.com/gif.latex?P^a_{**}"/>


A **Markov process** is a tyle (S, P), where : 
* S is a (finite) set of state
* P is a state transition probability matrix

## Markov Reward Process

A markov reward process is a tuple **(S, P, R, <img src="/Lecture2-MDP/tex/11c596de17c342edeed29f489aa4b274.svg?invert_in_darkmode&sanitize=true" align=middle width=9.423880949999988pt height=14.15524440000002pt/>)**
* S is a (finite) set of state
* P is a state transition probability matrix
* R is a reward function, <img src="/Lecture2-MDP/tex/1462376602603b14e0d70450520ebd21.svg?invert_in_darkmode&sanitize=true" align=middle width=148.6100352pt height=24.65753399999998pt/>
* <img src="/Lecture2-MDP/tex/11c596de17c342edeed29f489aa4b274.svg?invert_in_darkmode&sanitize=true" align=middle width=9.423880949999988pt height=14.15524440000002pt/>  is a discount factor, <img src="/Lecture2-MDP/tex/faddbecff1e63dbb1e5f23aae07a652d.svg?invert_in_darkmode&sanitize=true" align=middle width=62.39174864999998pt height=24.65753399999998pt/>


**Return** <img src="/Lecture2-MDP/tex/ef97d941958bc9c931fac79c478168d7.svg?invert_in_darkmode&sanitize=true" align=middle width=299.37084539999995pt height=27.91243950000002pt/>
* <img src="/Lecture2-MDP/tex/11c596de17c342edeed29f489aa4b274.svg?invert_in_darkmode&sanitize=true" align=middle width=9.423880949999988pt height=14.15524440000002pt/> close to 0 leads to interest in long-term rewards
* <img src="/Lecture2-MDP/tex/11c596de17c342edeed29f489aa4b274.svg?invert_in_darkmode&sanitize=true" align=middle width=9.423880949999988pt height=14.15524440000002pt/> close to 1 leads to interest in short-term rewards
* <img src="/Lecture2-MDP/tex/11c596de17c342edeed29f489aa4b274.svg?invert_in_darkmode&sanitize=true" align=middle width=9.423880949999988pt height=14.15524440000002pt/> avoids infinite returns in cycle (<img src="/Lecture2-MDP/tex/2569b17c0d0bf367e3f6217115f505d9.svg?invert_in_darkmode&sanitize=true" align=middle width=39.56070194999999pt height=21.18721440000001pt/> is ok if all sequences terminate)

**Value function V(s)**
The state value function V(s) of an MRP is the expected return starting from state s.
v(s) = E[G_t|S_t=s]

**Bellman Equation for MRPs**
The value function can be decomposed intro 2 parts :
* immediate reward <img src="/Lecture2-MDP/tex/464207bf81effbe38d5a981f0168b2d2.svg?invert_in_darkmode&sanitize=true" align=middle width=34.09118789999999pt height=22.465723500000017pt/>
* discounted value of successor state <img src="/Lecture2-MDP/tex/c028cea81301eb3a58f8b5c47e15ddb9.svg?invert_in_darkmode&sanitize=true" align=middle width=63.27865994999999pt height=24.65753399999998pt/>

<p align="center"><img src="/Lecture2-MDP/tex/91da05f4f1786c5d85786a28818ff1bb.svg?invert_in_darkmode&sanitize=true" align=middle width=323.60547779999996pt height=138.60813285pt/></p>


Using matrices : <img src="/Lecture2-MDP/tex/18760146fb0ed3efb93b2fbc7c271a89.svg?invert_in_darkmode&sanitize=true" align=middle width=93.99362774999999pt height=22.465723500000017pt/>
<img src='images/bellman_eq.PNG'>

It can be solved directly 

<img src="/Lecture2-MDP/tex/640182df60adce58bb4d8cca4c192adf.svg?invert_in_darkmode&sanitize=true" align=middle width=124.38562619999999pt height=26.76175259999998pt/>

It's computational complecity is <img src="/Lecture2-MDP/tex/90846c243bb784093adbb6d2d0b2b9d0.svg?invert_in_darkmode&sanitize=true" align=middle width=43.02219404999999pt height=26.76175259999998pt/> for n states => not feasible for big MRPs.

## Markov Decision Process (MDP)

A Markov Decision Process is a tuple <img src="/Lecture2-MDP/tex/c43b38bd04f8e8df9319c551cd6eafb8.svg?invert_in_darkmode&sanitize=true" align=middle width=97.4944905pt height=24.65753399999998pt/>
* S is a finite set of states
* A is a finite set of actions
* P is a state transition probability matrix, <img src="/Lecture2-MDP/tex/ec5ba87ced2847438257a0a9df887adc.svg?invert_in_darkmode&sanitize=true" align=middle width=253.74712275pt height=24.7161288pt/>
* R is a reward function, <img src="/Lecture2-MDP/tex/9450d21eff00548444e5177125e4ba79.svg?invert_in_darkmode&sanitize=true" align=middle width=205.69219604999995pt height=24.65753399999998pt/>
* <img src="/Lecture2-MDP/tex/11c596de17c342edeed29f489aa4b274.svg?invert_in_darkmode&sanitize=true" align=middle width=9.423880949999988pt height=14.15524440000002pt/> is a discount factor <img src="/Lecture2-MDP/tex/faddbecff1e63dbb1e5f23aae07a652d.svg?invert_in_darkmode&sanitize=true" align=middle width=62.39174864999998pt height=24.65753399999998pt/>


###  Policy 
A **policy** <img src="/Lecture2-MDP/tex/f30fdded685c83b0e7b446aa9c9aa120.svg?invert_in_darkmode&sanitize=true" align=middle width=9.96010619999999pt height=14.15524440000002pt/> is a distribution over actions given states.
<img src="/Lecture2-MDP/tex/76f2a903a085588efce98313fd6d9f93.svg?invert_in_darkmode&sanitize=true" align=middle width=190.02643275pt height=24.65753399999998pt/>

* A policy fully defines the behaviour of an agent
* Policies are stationary (time-independent)
* We have : <img src="/Lecture2-MDP/tex/c50fb249eca971ca617ce2a68998487f.svg?invert_in_darkmode&sanitize=true" align=middle width=167.22949649999998pt height=24.657735299999988pt/>
* And <img src="/Lecture2-MDP/tex/3bbb6bb49ff38008d4d0d91c1aeda1f5.svg?invert_in_darkmode&sanitize=true" align=middle width=153.68117159999997pt height=24.657735299999988pt/>

### Value function

The **state-value function <img src="/Lecture2-MDP/tex/85aed0b0f7b723a72042b5a7378030bf.svg?invert_in_darkmode&sanitize=true" align=middle width=37.38085559999999pt height=24.65753399999998pt/>** of an MDP is :
<img src="/Lecture2-MDP/tex/07b4a3e453e751dd3ca2da0e046f9627.svg?invert_in_darkmode&sanitize=true" align=middle width=158.25680804999996pt height=24.65753399999998pt/>

The **action-value fnction <img src="/Lecture2-MDP/tex/3580cae5d32bba7f4d60574ab98e99d3.svg?invert_in_darkmode&sanitize=true" align=middle width=52.74613904999998pt height=24.65753399999998pt/>** is : 
<img src="/Lecture2-MDP/tex/2fa370f6cbfc801dee0809554659e3c9.svg?invert_in_darkmode&sanitize=true" align=middle width=229.65124544999998pt height=24.65753399999998pt/>

### Bellman Expectation equation 

* <img src="/Lecture2-MDP/tex/7617b43653d81e0ed4fb1764b7123ea3.svg?invert_in_darkmode&sanitize=true" align=middle width=266.15950349999997pt height=24.65753399999998pt/>
* <img src="/Lecture2-MDP/tex/ee8abd9af6ab804833701259cf006759.svg?invert_in_darkmode&sanitize=true" align=middle width=378.9904668pt height=24.65753399999998pt/>

Link between these 2 notions :

<img src="/Lecture2-MDP/tex/3fbf96c6df9e1649a82a3be47546bccf.svg?invert_in_darkmode&sanitize=true" align=middle width=182.04805409999997pt height=24.657735299999988pt/>

<img src="/Lecture2-MDP/tex/ed8b9728c55513fe7f67361a3e2a3426.svg?invert_in_darkmode&sanitize=true" align=middle width=210.34008765pt height=24.7161288pt/>

Putting the first equation in the second one, we've got in matrice format : 

<img src="/Lecture2-MDP/tex/ee3340285c753b54c001790f471b1dcb.svg?invert_in_darkmode&sanitize=true" align=middle width=127.67964824999999pt height=22.465723500000017pt/> 

The **optimal state-value function <img src="/Lecture2-MDP/tex/db5852fb90abf0498e60793cc2f0ecb1.svg?invert_in_darkmode&sanitize=true" align=middle width=36.01606799999999pt height=24.65753399999998pt/>** is : 
<img src="/Lecture2-MDP/tex/e88e69b401ace6d9582952e192223f8d.svg?invert_in_darkmode&sanitize=true" align=middle width=127.83175349999998pt height=24.65753399999998pt/>


The **optimal action-value function <img src="/Lecture2-MDP/tex/da08563baf659b0eb51a343d501bd6dd.svg?invert_in_darkmode&sanitize=true" align=middle width=51.38135144999999pt height=24.65753399999998pt/>** is : 
<img src="/Lecture2-MDP/tex/964884b522157c8fcae7ad6496ffbe0f.svg?invert_in_darkmode&sanitize=true" align=middle width=158.56231874999997pt height=24.65753399999998pt/>

### Theorem  
For any MDP, there exists an optimal policy.

### Bellman Optimality Equation 

<img src="/Lecture2-MDP/tex/e9679da5d191a0b906e50e64bcccce6b.svg?invert_in_darkmode&sanitize=true" align=middle width=141.83224769999998pt height=24.65753399999998pt/> 

This makes the Bellman Optimality Equation *non-linear*. In general there isn't a closed form solution.
But there are iterative solution methods : 
* Value iteration
* Policy iteration
* Q-learning
* Sarsa

## Extension to MDPs

There are other forms of MDPs which are : 
* Infinite and continuous MDPs
* Partially observable MDPs (POMDP)
* Undiscounted, average reward MDPs


A *POMDP* is a tuple <img src="/Lecture2-MDP/tex/382ea2eba8afb86d2e28ee19f43596bd.svg?invert_in_darkmode&sanitize=true" align=middle width=136.58570639999996pt height=24.65753399999998pt/>
* S is a finite set of states
* A is a finite set of actions
* O is a finite set of observations
* P is a state transition probability matrix, <img src="/Lecture2-MDP/tex/ec5ba87ced2847438257a0a9df887adc.svg?invert_in_darkmode&sanitize=true" align=middle width=253.74712275pt height=24.7161288pt/>
* R is a reward function, <img src="/Lecture2-MDP/tex/9450d21eff00548444e5177125e4ba79.svg?invert_in_darkmode&sanitize=true" align=middle width=205.69219604999995pt height=24.65753399999998pt/>
* Z is an observation function, <img src="/Lecture2-MDP/tex/d4e72be2b8d41d80de034efed335974a.svg?invert_in_darkmode&sanitize=true" align=middle width=265.26752999999997pt height=24.7161288pt/>
* <img src="/Lecture2-MDP/tex/11c596de17c342edeed29f489aa4b274.svg?invert_in_darkmode&sanitize=true" align=middle width=9.423880949999988pt height=14.15524440000002pt/> is a discount factor <img src="/Lecture2-MDP/tex/faddbecff1e63dbb1e5f23aae07a652d.svg?invert_in_darkmode&sanitize=true" align=middle width=62.39174864999998pt height=24.65753399999998pt/>
