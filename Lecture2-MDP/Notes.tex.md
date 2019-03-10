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

A markov reward process is a tuple (S, P, R, $\gamma$ )