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
    * Evaluate the policy 
    
    ($v_\pi(s) = E[R_{t+1} + \gamma T_{t+2} + ... | S_t = s]$)
    * Improve the policy by acting greedily with respect to 
    
    $v_\pi$ ($\pi' = greedy(v_\pi)$)

In a small GridWorld env 1 iteration is enough. But in general more iterations is necesary.
This process always converges to the optimal policy <img src="/Lecture3-PlanningByDynamicProgramming/tex/b1384136386b001cacf877cd93c98628.svg?invert_in_darkmode&sanitize=true" align=middle width=16.69528244999999pt height=22.63846199999998pt/>.

<img src='./images/policy_iteration.PNG'>


More formally :

* Consider a deterministic policy, <img src="/Lecture3-PlanningByDynamicProgramming/tex/2afd7aaff2306a902c027fe99967b373.svg?invert_in_darkmode&sanitize=true" align=middle width=61.05778469999999pt height=24.65753399999998pt/>
* We can improve the policy by acting greedily <img src="/Lecture3-PlanningByDynamicProgramming/tex/9e4199c4b51a8dd27b910b2a167d37e7.svg?invert_in_darkmode&sanitize=true" align=middle width=167.23625984999998pt height=29.339719199999994pt/>
* This imporoves the value from any stat s over one step
<img src="/Lecture3-PlanningByDynamicProgramming/tex/47b155b28d4ac31a604c2119904f37d6.svg?invert_in_darkmode&sanitize=true" align=middle width=309.5076831pt height=31.1662098pt/>

* It therefore improves the value function, <img src="/Lecture3-PlanningByDynamicProgramming/tex/f486dbe71390d523507a53e6a6967658.svg?invert_in_darkmode&sanitize=true" align=middle width=74.76171285pt height=24.7161288pt/>
* If improvements stop, q<img src="/Lecture3-PlanningByDynamicProgramming/tex/fec84172ddb21d45e2008a7519ac86b9.svg?invert_in_darkmode&sanitize=true" align=middle width=168.20716439999998pt height=24.7161288pt/>, then the Bellman optimality equation is satisfied. So <img src="/Lecture3-PlanningByDynamicProgramming/tex/f30fdded685c83b0e7b446aa9c9aa120.svg?invert_in_darkmode&sanitize=true" align=middle width=9.96010619999999pt height=14.15524440000002pt/> is an optimal policy.

GridWorld application can be found [[here]](./Applications/policy-iteration_grid_world.py)

## Value Iteration

Any optimal pollicy can be subdivided into 2 components :
* an optimal first action
* followed by an optimal policy from successor state

### Deterministic Value Iteration

* If we know the solution to subproblems <img src="/Lecture3-PlanningByDynamicProgramming/tex/c23e70abc37b4dc4e0ac3e1fdb4f47ea.svg?invert_in_darkmode&sanitize=true" align=middle width=40.627943399999985pt height=24.7161288pt/>
* Then solution <img src="/Lecture3-PlanningByDynamicProgramming/tex/db5852fb90abf0498e60793cc2f0ecb1.svg?invert_in_darkmode&sanitize=true" align=middle width=36.01606799999999pt height=24.65753399999998pt/> can be found by one-step lookahead, <img src="/Lecture3-PlanningByDynamicProgramming/tex/40ecb00356ef68bdf3e956a0f61b80f9.svg?invert_in_darkmode&sanitize=true" align=middle width=273.45899955pt height=24.7161288pt/>
* The idea of value iteation is to apply these updates iteratively

To sum up, we have built 3 different *synchronous* algorithms : 
<img src='images/sum_up_lecture3.png'>

## Extensions to Dynamic Programming 

Extensions to dynamic programming are :
*  *Asynchronous* dynamic programming. States are backs up individually. Can reduce computation.
* In-place dynamic programming
* Prioritised sweeping, back-up state with the largest remaining Bellman error
* Real-time dynamic programming, use of agent experience 
