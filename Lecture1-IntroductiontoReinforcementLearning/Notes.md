# Introduction to Reinforcement Learning

[Lecture](https://www.youtube.com/watch?v=2pWv7GOvuf0&list=PLqYmG7hTraZDM-OYHWgPebj2MfCFzFObQ), [Slides](http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching_files/intro_RL.pdf)

Characteristics of Reinforcement Learning :
* No supervisor, only a **reward** signal
* Feedback is delayed
* Time really matters (sequential, non i.i.d data)
* Agent's action affect the subsequent data it receives

Examples of Application : 
* Fly stunt manoeuvres in a helicopter
* Defeat the world champion at Backgammon
* Manage an investment portfolio
* Control a power station
* Make a humanoid robot walk
* Play many different Atari games better than humans


Objective of an agent is to **maximise cumulative reward**. 

In a RL task there is this infinite loop :

<img src='images/rl_loop.PNG'>

The agent can only control its action.

We define the history as the sequence of observations, actions, rewards of past events. 
<img src="https://latex.codecogs.com/gif.latex?H_t=A_1,O_1,R_1,...,A_t,O_t,R_t" title="H_t=A_1,O_1,R_1,...,A_t,O_t,R_t" />

A state <img src="https://latex.codecogs.com/gif.latex?S_t" /> is **Markov** if and only if  <img src="https://latex.codecogs.com/gif.latex?P[S_{t+1|S_t}]=P[S_{t+1}|S_1,...,S_t]"/>
If a state is a **Markov state** then it contains all useful information from the history (i.e the history may be thrown away).

There are 2 types of environment : 
* **Fully observable environment** (defined by MDP). Agent sees <img src="https://latex.codecogs.com/gif.latex?O_t" /> 
* **Partially observable environment** (defined by POMDP). Agent must construct its own representation of the environment state (i.e. a kind of environment state prediction based on the part he sees)

An RL agent must include one or more of these components : 
* **Policy** <img src="https://latex.codecogs.com/gif.latex?\pi"/>: agent's behaviour function (for *deterministic policy* : <img src="https://latex.codecogs.com/gif.latex?a=\pi(s)"/>, for *stochastic policy* : <img src="https://latex.codecogs.com/gif.latex?\pi(a|s)=P[A=a|S=s]"/>) 
* **Value function** : how good is each state and/or action. It's a prediction of future *discounted* reward. (<img src="https://latex.codecogs.com/gif.latex?v_\pi(s)=E_\pi[R_t+\gammaR_{t+1}+\gamma^2R_{t+2}+...|S_t=s]"/>)
* **Model** : agent's representation of the environment, predicts how environment will be updated <img src="https://latex.codecogs.com/gif.latex?P^a_{ss'}=P[S'=s'|S=s,A=a]"/> and the next immediate reward <img src="https://latex.codecogs.com/gif.latex?R_s^a=R[R|S=s,A=a]"/>

Taxonomy of different types of RL agents, based on what they have : 
* Value based
    * No policy (Implicit)
    * Value Function
* Policy based 
    * Policy 
    * No Value function
* Actor Critic
    * Policy 
    * Value function

* Model Free
    * Policy and/or Value function
    * No model
* Model Based
    * Policy and/or Value function
    * Model

<img height='300px' src='images/taxonomy_RL_agents.PNG' />


## Problems in RL

In **RL** the environment is initially unknown by the agent, but rules are learnt by interacting with the environnement.
Whereas in **Planning** a model of the environnment is known (e.g. exact tree search).   

Rl is like **trial-and-error learning**.

**Exploration vs Exploitation** :
* **Exploration** finds more information about the environment.

* **Exploitation** exploits known information to maximize rewards.

**Prediction vs Control** :

* **Prediction** problem : *evaluate the future*, given a policy

* **Control** problem : *optimize the future*, find the best 
policy