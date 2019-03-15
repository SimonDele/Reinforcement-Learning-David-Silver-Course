# Lecture 3 : Planning by Dynamic Programming

[Lecture](https://www.youtube.com/watch?v=Nd1-UUMVfz4), [Slides](http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching_files/DP.pdf)

## Introduction

*Dynamic* sequential or temporal component to the problem

*Programming* optimising a "program" (i.e policy)

*Dynamic programming* is a very general solution method for problems which have 2 properties :
* Optimal substructure (i.e combining optimal solution for substructure give optimal solution)
* Overlapping subproblems

MDP satisfy these both property (<3 Markov property & Bellman equation)

**Dynamic programming assumes full knowledge of the MDP**. It is used for planning in an MDP, for prediction (~evaluation a policy ??). Or control (finding the best policy)... (But is also used in other fields).

## Policy Evaluation

**Problem** : How to evaluate a given policy <img src="/Lecture3-PlanningByDynamicProgramming/tex/f30fdded685c83b0e7b446aa9c9aa120.svg?invert_in_darkmode&sanitize=true" align=middle width=9.96010619999999pt height=14.15524440000002pt/>.

**Solution** : iterative application of Bellman expaction backup.

<img src="/Lecture3-PlanningByDynamicProgramming/tex/3a002e4fb25e6c76819741600aa7a993.svg?invert_in_darkmode&sanitize=true" align=middle width=164.56094324999998pt height=17.723762100000005pt/>

Using **synchronous backups** :
At each iteration k+1 :
* For all states <img src="/Lecture3-PlanningByDynamicProgramming/tex/2d8cca33f0ee74986943da285a93a659.svg?invert_in_darkmode&sanitize=true" align=middle width=38.82401819999999pt height=22.465723500000017pt/>
* Update <img src="/Lecture3-PlanningByDynamicProgramming/tex/d53d03132ef32e56e54f8107634fe462.svg?invert_in_darkmode&sanitize=true" align=middle width=53.19083384999998pt height=24.65753399999998pt/> from <img src="/Lecture3-PlanningByDynamicProgramming/tex/8d94ff4fd8440c1865ff94cce0fbfe07.svg?invert_in_darkmode&sanitize=true" align=middle width=41.15879789999999pt height=24.7161288pt/>
* where s' is a successor state of s


<img src='images/policy_evaluation.PNG'>

GridWorld application can be found [[here]](./Applications/policy_evaluation_grid_world.py)

## Policy Iteration

*How to improve our policy ?*

* Given a policy <img src="/Lecture3-PlanningByDynamicProgramming/tex/f30fdded685c83b0e7b446aa9c9aa120.svg?invert_in_darkmode&sanitize=true" align=middle width=9.96010619999999pt height=14.15524440000002pt/>
    * Evaluate the policy $\pi$ ($v_\pi(s) = E[R_{t+1} + \gamma T_{t+2} + ... | S_t = s]$)
    * Improve the policy by acting greedily with respect to $v_\pi$ ($\pi' = greedy(v_\pi)$)

In a small GridWorld env 1 iteration is enough. But in general more iterations is necesary.
This process always converges to the optimal policy <img src="/Lecture3-PlanningByDynamicProgramming/tex/b1384136386b001cacf877cd93c98628.svg?invert_in_darkmode&sanitize=true" align=middle width=16.69528244999999pt height=22.63846199999998pt/>.

<img src='./images/policy_iteration.PNG'>

**TODO** Car rental exercise

## Value Iteration

## Extension to Dynamic Programming 

## Contraction Mapping
