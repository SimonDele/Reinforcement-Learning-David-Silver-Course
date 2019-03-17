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








