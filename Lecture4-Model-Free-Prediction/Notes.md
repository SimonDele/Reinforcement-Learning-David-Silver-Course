# Lecture 4 : Model-Free Prediction

## Introduction

In model-free methods, the **MDP** that rules the world is **unknown**.

## Monte-Carlo (MC) Learning

MC methods learn directly from episodes of experience

MC is a model-free : no knowledge of MDP transitions/rewards

**MC learns from complete episodes : no boostrapping** 

**Goal** learn <img src="/Lecture4-Model-Free-Prediction/tex/143c6aa101ce0c82aab772be351df16b.svg?invert_in_darkmode&sanitize=true" align=middle width=16.06802669999999pt height=14.15524440000002pt/> from episodes of experience under policy <img src="/Lecture4-Model-Free-Prediction/tex/f30fdded685c83b0e7b446aa9c9aa120.svg?invert_in_darkmode&sanitize=true" align=middle width=9.96010619999999pt height=14.15524440000002pt/>. (<img src="/Lecture4-Model-Free-Prediction/tex/a6e378ee0764e0c9978f21a39aa95f05.svg?invert_in_darkmode&sanitize=true" align=middle width=139.93589939999998pt height=24.65753399999998pt/>


Recall :
* *return* G is the total discounted reward

<img src="/Lecture4-Model-Free-Prediction/tex/30b2dda7a53ee03bee023f238edaef4c.svg?invert_in_darkmode&sanitize=true" align=middle width=224.13701475000002pt height=22.465723500000017pt/>

* Value function is the expected return

<img src="/Lecture4-Model-Free-Prediction/tex/07b4a3e453e751dd3ca2da0e046f9627.svg?invert_in_darkmode&sanitize=true" align=middle width=158.25680804999996pt height=24.65753399999998pt/>

### First-visit Monte-Carlo Policy Evaluation

The first time-step t that state s is visited in an episode 

1. Increment counter <img src="/Lecture4-Model-Free-Prediction/tex/9f0ead62b7b6ce274dbf5e8df9da2ff5.svg?invert_in_darkmode&sanitize=true" align=middle width=124.8627633pt height=24.65753399999998pt/>

2. Increment total return with the return <img src="/Lecture4-Model-Free-Prediction/tex/a3a39fed9b506fff08f98d72d864dce7.svg?invert_in_darkmode&sanitize=true" align=middle width=126.5888184pt height=24.65753399999998pt/>

3. Value is estimated by mean return V(s) = S(s) / N(s)

4. By law a large numbers, <img src="/Lecture4-Model-Free-Prediction/tex/0a6101a67bf7271d9a99b2435ba64c8c.svg?invert_in_darkmode&sanitize=true" align=middle width=96.68439989999999pt height=24.65753399999998pt/> as <img src="/Lecture4-Model-Free-Prediction/tex/960c87d717b01929185ddfa2676820c2.svg?invert_in_darkmode&sanitize=true" align=middle width=77.49988454999999pt height=24.65753399999998pt/>

### Every-Visit Monte-Carlo Policy Evaluation

Every time-step t that state s is visited in an episode

1. Increment counter <img src="/Lecture4-Model-Free-Prediction/tex/084834181961559f5d5073dcf5200f13.svg?invert_in_darkmode&sanitize=true" align=middle width=124.8627633pt height=24.65753399999998pt/> 
2. Increment total return <img src="/Lecture4-Model-Free-Prediction/tex/a3a39fed9b506fff08f98d72d864dce7.svg?invert_in_darkmode&sanitize=true" align=middle width=126.5888184pt height=24.65753399999998pt/>
3. Value is estimated by mean return <img src="/Lecture4-Model-Free-Prediction/tex/ea256e9130c97c34c2299b147786e334.svg?invert_in_darkmode&sanitize=true" align=middle width=129.96571665pt height=24.65753399999998pt/>
4. Again, by law a large numbers, <img src="/Lecture4-Model-Free-Prediction/tex/0a6101a67bf7271d9a99b2435ba64c8c.svg?invert_in_darkmode&sanitize=true" align=middle width=96.68439989999999pt height=24.65753399999998pt/> as <img src="/Lecture4-Model-Free-Prediction/tex/960c87d717b01929185ddfa2676820c2.svg?invert_in_darkmode&sanitize=true" align=middle width=77.49988454999999pt height=24.65753399999998pt/>

**Application** on Black-jack [[here]](./Applications/monte_carlo_policy_evaluation.ipynb)


**Monte Carlo policy evaluation uses empiral mean return instead of expected return** 


### Incremental Monte-Carlo updates

Use the formula of the *incremental mean* :
<img src="/Lecture4-Model-Free-Prediction/tex/d0cd6fee5657e8916b398e80a3a8b6c3.svg?invert_in_darkmode&sanitize=true" align=middle width=216.81507539999998pt height=24.65753399999998pt/>. Which gives :
* <img src="/Lecture4-Model-Free-Prediction/tex/3317b914ec331c424cb9c0ed536615c5.svg?invert_in_darkmode&sanitize=true" align=middle width=141.18703004999998pt height=24.65753399999998pt/>
* <img src="/Lecture4-Model-Free-Prediction/tex/ef1449da3cd0bebf22096fe574f926df.svg?invert_in_darkmode&sanitize=true" align=middle width=275.72144984999994pt height=24.65753399999998pt/>

In non-stationary problems, it can be useful to track a running mean (i.e to forget old episodes) : 
<img src="/Lecture4-Model-Free-Prediction/tex/893ab197570cb0e43f7a91b684255d83.svg?invert_in_darkmode&sanitize=true" align=middle width=233.51247645pt height=24.65753399999998pt/>


## Temporal-Difference Learning

TD learns from **incomplete episodes** by *boostrapping*
TD is model-free, learn directly from experience


In *Incremental every-visit MC* we had : 
    $V(S_t) \leftarrow V(S_t) + \alpha (G_t - V(S_t))$ 
which means that we move a litte bit in the direction given by the current error.

In TD(0) we use the same idea but we leverage the Bellman equation to learn from incomplete sequence : 
<img src="/Lecture4-Model-Free-Prediction/tex/76ffd7a097bfb9230807a4f7516a52e0.svg?invert_in_darkmode&sanitize=true" align=middle width=337.76725949999997pt height=24.65753399999998pt/>





<img src="/Lecture4-Model-Free-Prediction/tex/f4fac9913a40f49ae900340e1eeee5a6.svg?invert_in_darkmode&sanitize=true" align=middle width=122.96711459999997pt height=24.65753399999998pt/> is called the *TD target*

<img src="/Lecture4-Model-Free-Prediction/tex/93f38902504f093339f51ed36acb137f.svg?invert_in_darkmode&sanitize=true" align=middle width=219.96463994999993pt height=24.65753399999998pt/> is called the *TD error*

<img src='./images/diff_MC-TD.png'>

TD can learn *before* knowing the final outcome, MC can't. 

### Bias/Variance Trade-Off
Return <img src="/Lecture4-Model-Free-Prediction/tex/2d70468f18a4a73317e00739dd5f2a39.svg?invert_in_darkmode&sanitize=true" align=middle width=118.75676174999998pt height=22.465723500000017pt/> is unbiased estimate of <img src="/Lecture4-Model-Free-Prediction/tex/9af5e9d50fa194442f8f33f355b3f834.svg?invert_in_darkmode&sanitize=true" align=middle width=47.17097549999999pt height=24.65753399999998pt/>
TD target <img src="/Lecture4-Model-Free-Prediction/tex/b2bf14e346ab70c2d514534051261066.svg?invert_in_darkmode&sanitize=true" align=middle width=122.96711459999997pt height=24.65753399999998pt/> is biased estimate of <img src="/Lecture4-Model-Free-Prediction/tex/3f81ed330e4e97dc7a32caa2c3647be2.svg?invert_in_darkmode&sanitize=true" align=middle width=45.54298979999999pt height=24.65753399999998pt/> but lower variance because return is full of noise (random actions, transition, rewards)

TD exploits Markov property and is then more efficient in Markov environments. In other case, MC is more efficient.


### Unified View - Backups

**Monte-Carlo** backup  

<img src='images/mc_backup.png'>

**TD** backup

<img src='images/td_backup.png'>

**Dynamic programming** backup

<img src='images/dp_backup.png'>

### Bootstrapping and Sampling

**Boostrapping** use your estimate of the return
* MC does not bootstrap
* DP bootstraps
* TD bootstraps

**Sampling** update samples an expectation
* MC samples
* DP does not sample
* TD samples

<img src='images/unified_view.png'>


## TD(<img src="/Lecture4-Model-Free-Prediction/tex/fd8be73b54f5436a5cd2e73ba9b6bfa9.svg?invert_in_darkmode&sanitize=true" align=middle width=9.58908224999999pt height=22.831056599999986pt/>)

TD(0) = look 1 step into the future (<img src="/Lecture4-Model-Free-Prediction/tex/c417c533849bcdedb93b6c09fd79373b.svg?invert_in_darkmode&sanitize=true" align=middle width=163.59707595pt height=24.65753399999998pt/>)

TD(1) = look 2 steps ino the future (<img src="/Lecture4-Model-Free-Prediction/tex/7501879aa20570e55d180634d0f86c4d.svg?invert_in_darkmode&sanitize=true" align=middle width=235.39966395000002pt height=26.76175259999998pt/>)


TD(n) = ...

TD(<img src="/Lecture4-Model-Free-Prediction/tex/f7a0f24dc1f54ce82fecccbbf48fca93.svg?invert_in_darkmode&sanitize=true" align=middle width=16.43840384999999pt height=14.15524440000002pt/>) = Monte-Carlo

TD(<img src="/Lecture4-Model-Free-Prediction/tex/fd8be73b54f5436a5cd2e73ba9b6bfa9.svg?invert_in_darkmode&sanitize=true" align=middle width=9.58908224999999pt height=22.831056599999986pt/>) : averaging (with weight <img src="/Lecture4-Model-Free-Prediction/tex/d1906ea8459090ad568407b22f215a3b.svg?invert_in_darkmode&sanitize=true" align=middle width=85.22659034999998pt height=26.76175259999998pt/>) the return of all time-steps. <img src="/Lecture4-Model-Free-Prediction/tex/46911fd58616f647e7b401150adfd3d7.svg?invert_in_darkmode&sanitize=true" align=middle width=209.25701775pt height=34.337843099999986pt/> where <img src="/Lecture4-Model-Free-Prediction/tex/1e8f8f06f641b8b8e4f1d9523d637141.svg?invert_in_darkmode&sanitize=true" align=middle width=31.324698899999987pt height=34.337843099999986pt/> is the return of TD(n).

