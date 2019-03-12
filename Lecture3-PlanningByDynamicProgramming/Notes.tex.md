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

**Problem** : How to evaluate a given policy $\pi$.

**Solution** : iterative application of Bellman expaction backup.

$v_1 => v_2 => ... => v_\pi$

Using **synchronous backups** :
At each iteration k+1 :
* For all states $s \in S$
* Update $v_{k+1}(s)$ from $v_k(s')$
* where s' is a successor state of s


<img src='images/policy_evaluation.PNG'>

**TODO** GridWorld application

## Policy Iteration

## Value Iteration

## Extension to Dynamic Programming 

## Contraction Mapping
