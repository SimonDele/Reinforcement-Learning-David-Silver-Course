# Lecture 5 : Model-Free Control

## Introduction

Find the best policy without knowing the MDP that rules the world.


* **On-policy** learning : "learn on the job", learn about policy <img src="/Lecture5-Model-Free-Control/tex/f30fdded685c83b0e7b446aa9c9aa120.svg?invert_in_darkmode&sanitize=true" align=middle width=9.96010619999999pt height=14.15524440000002pt/> from experience sampled from <img src="/Lecture5-Model-Free-Control/tex/f30fdded685c83b0e7b446aa9c9aa120.svg?invert_in_darkmode&sanitize=true" align=middle width=9.96010619999999pt height=14.15524440000002pt/>

* **Off-policy** learning : "look over someone's shoulder, learn about policy <img src="/Lecture5-Model-Free-Control/tex/f30fdded685c83b0e7b446aa9c9aa120.svg?invert_in_darkmode&sanitize=true" align=middle width=9.96010619999999pt height=14.15524440000002pt/> from experience sampled from <img src="/Lecture5-Model-Free-Control/tex/07617f9d8fe48b4a7b3f523d6730eef0.svg?invert_in_darkmode&sanitize=true" align=middle width=9.90492359999999pt height=14.15524440000002pt/>


## On-Policy Monte-Carlo Control

With value iteration, we were doing a greed policy improvement over <img src="/Lecture5-Model-Free-Control/tex/1ae4c80eec5d4a776a42d28dc01e0c90.svg?invert_in_darkmode&sanitize=true" align=middle width=33.732943199999994pt height=24.65753399999998pt/> but that requires model of MDP :

<img src="/Lecture5-Model-Free-Control/tex/fa447c4da3761bb21049d887a555d56e.svg?invert_in_darkmode&sanitize=true" align=middle width=221.71757189999997pt height=29.339719199999994pt/>

But we want to be model-free...

So Greedy policy improvement over Q(s, a) which is model-free :

<img src="/Lecture5-Model-Free-Control/tex/e9fd8366a311b7a8ce99bf893a76cb31.svg?invert_in_darkmode&sanitize=true" align=middle width=163.97149559999997pt height=29.339719199999994pt/>


With model-free methods we need to introduce an exploratory strategy in order to make sure to visit everything.

**\epsilon-greedy exploration** : 
* every actions are tried with non-zero probability for every states
* with probability <img src="/Lecture5-Model-Free-Control/tex/bdb8f1d1c8fbdfe5abfdafd09a2b6227.svg?invert_in_darkmode&sanitize=true" align=middle width=34.98279179999999pt height=21.18721440000001pt/> choose the greedy action
* with probability <img src="/Lecture5-Model-Free-Control/tex/7ccca27b5ccc533a2dd72dc6fa28ed84.svg?invert_in_darkmode&sanitize=true" align=middle width=6.672392099999992pt height=14.15524440000002pt/> choose an action at random


### Theorem

For any <img src="/Lecture5-Model-Free-Control/tex/7ccca27b5ccc533a2dd72dc6fa28ed84.svg?invert_in_darkmode&sanitize=true" align=middle width=6.672392099999992pt height=14.15524440000002pt/>-greedy policy <img src="/Lecture5-Model-Free-Control/tex/f30fdded685c83b0e7b446aa9c9aa120.svg?invert_in_darkmode&sanitize=true" align=middle width=9.96010619999999pt height=14.15524440000002pt/>, the <img src="/Lecture5-Model-Free-Control/tex/7ccca27b5ccc533a2dd72dc6fa28ed84.svg?invert_in_darkmode&sanitize=true" align=middle width=6.672392099999992pt height=14.15524440000002pt/>-greedy policy <img src="/Lecture5-Model-Free-Control/tex/e1c4ca96d10da0d56ad235b3b5fe363e.svg?invert_in_darkmode&sanitize=true" align=middle width=13.750048949999991pt height=24.7161288pt/> with respect to <img src="/Lecture5-Model-Free-Control/tex/d9fad2914b7324ed12eb8bd6f289f92b.svg?invert_in_darkmode&sanitize=true" align=middle width=8.099960549999992pt height=14.15524440000002pt/> is an improvement, i.e <img src="/Lecture5-Model-Free-Control/tex/8ae42fd2e00e31396f95c338b4a7ad4d.svg?invert_in_darkmode&sanitize=true" align=middle width=481.00594904999997pt height=124.7488638pt/>Q \approx q_\pi<img src="/Lecture5-Model-Free-Control/tex/e606a682cae854333c0eae3fe8fa9265.svg?invert_in_darkmode&sanitize=true" align=middle width=163.12102785pt height=22.831056599999986pt/>\epsilon<img src="/Lecture5-Model-Free-Control/tex/0a63a188d199e1567347e28154fa84a7.svg?invert_in_darkmode&sanitize=true" align=middle width=700.27451835pt height=85.29681270000002pt/>\epsilon<img src="/Lecture5-Model-Free-Control/tex/5af67c426f69cb9fc1b4171c8cf0828a.svg?invert_in_darkmode&sanitize=true" align=middle width=146.3393448pt height=22.831056599999986pt/>\epsilon_k = 1/k<img src="/Lecture5-Model-Free-Control/tex/d4510c0c0a9dfcbd02042e9b343e4694.svg?invert_in_darkmode&sanitize=true" align=middle width=188.53931415pt height=85.29681270000002pt/>\pi<img src="/Lecture5-Model-Free-Control/tex/c8c3ea900046866d04e9cff431c40c0a.svg?invert_in_darkmode&sanitize=true" align=middle width=105.76331535pt height=22.831056599999986pt/>S_t<img src="/Lecture5-Model-Free-Control/tex/10495d6965b9051a6542374bb3a8e3f9.svg?invert_in_darkmode&sanitize=true" align=middle width=72.34920329999999pt height=22.831056599999986pt/>A_t<img src="/Lecture5-Model-Free-Control/tex/34fd54d6872903ffeae0fa12b4a17e50.svg?invert_in_darkmode&sanitize=true" align=middle width=92.06301554999999pt height=22.831056599999986pt/>N(S_t, A_t) \leftarrow N(S_t, A_t) + 1<img src="/Lecture5-Model-Free-Control/tex/51709c221bb606c7f0a6193f462db8dd.svg?invert_in_darkmode&sanitize=true" align=middle width=8.21920935pt height=14.15524440000002pt/>Q(S_t, A_t) \leftarrow Q(S_t, A_t) + (G_t - Q(S_t, A_t))/N(S_t, A_t) <img src="/Lecture5-Model-Free-Control/tex/00ac197d9e09033866ee1b8ebd706fdc.svg?invert_in_darkmode&sanitize=true" align=middle width=365.43483075pt height=45.84475499999998pt/>\epsilon \leftarrow 1/k<img src="/Lecture5-Model-Free-Control/tex/51709c221bb606c7f0a6193f462db8dd.svg?invert_in_darkmode&sanitize=true" align=middle width=8.21920935pt height=14.15524440000002pt/>\pi \leftarrow \epsilon-greedy(Q)<img src="/Lecture5-Model-Free-Control/tex/f65f9acbc642ef3ad2749e5622b0a5ed.svg?invert_in_darkmode&sanitize=true" align=middle width=700.27449855pt height=361.4611935pt/>\pi_t(a|s)<img src="/Lecture5-Model-Free-Control/tex/55662df21f7c41358311625e62a6a964.svg?invert_in_darkmode&sanitize=true" align=middle width=299.51941965000003pt height=22.831056599999986pt/>\alpha_t<img src="/Lecture5-Model-Free-Control/tex/51709c221bb606c7f0a6193f462db8dd.svg?invert_in_darkmode&sanitize=true" align=middle width=8.21920935pt height=14.15524440000002pt/>\sum_{t=1}^\infty = \infty<img src="/Lecture5-Model-Free-Control/tex/cbe4745c368cb36ecf6b1c81ef1d330a.svg?invert_in_darkmode&sanitize=true" align=middle width=8.21920935pt height=14.15524440000002pt/>\sum_{t=1}^\infty \leq \infty<img src="/Lecture5-Model-Free-Control/tex/9b9cb459bb65a6f930d3aec3ce5385ed.svg?invert_in_darkmode&sanitize=true" align=middle width=290.24263125pt height=126.57534119999997pt/>\lambda<img src="/Lecture5-Model-Free-Control/tex/8272b9b730847f03c2de75137d385997.svg?invert_in_darkmode&sanitize=true" align=middle width=182.557551pt height=45.84475500000001pt/>q_t^\lambda = (1-\lambda) \sum_{n=1}^\infty \lambda^{n-1} q_t^{(n)}<img src="/Lecture5-Model-Free-Control/tex/763aa461877aee56ac9ac32da74c4402.svg?invert_in_darkmode&sanitize=true" align=middle width=97.80849209999998pt height=39.45205439999997pt/>Q(S_t, A_t) \leftarrow Q(S_t, A_t) + \alpha (q_t^\lambda - Q(S_t, A_t))<img src="/Lecture5-Model-Free-Control/tex/82d8de7faf4959b9a66847f6a3a20150.svg?invert_in_darkmode&sanitize=true" align=middle width=147.21506909999997pt height=47.67123239999998pt/>\lambda<img src="/Lecture5-Model-Free-Control/tex/fda1e78dbe0f915ab5eaa8fd387dea27.svg?invert_in_darkmode&sanitize=true" align=middle width=335.89134974999996pt height=87.12328680000002pt/>\labmda<img src="/Lecture5-Model-Free-Control/tex/482342fda4514d29cb9cca9f2e6ebad3.svg?invert_in_darkmode&sanitize=true" align=middle width=358.4628795pt height=24.65753399999998pt/>E_0(s,a) = 0<img src="/Lecture5-Model-Free-Control/tex/27728fe426f41c0b349ee0fa77589aae.svg?invert_in_darkmode&sanitize=true" align=middle width=8.219209349999991pt height=15.296829900000011pt/>E_t(s, a) = \gamma \labmda E_{t-1} (s,a) + I(S_t = s, A_t = a)<img src="/Lecture5-Model-Free-Control/tex/51709c221bb606c7f0a6193f462db8dd.svg?invert_in_darkmode&sanitize=true" align=middle width=8.21920935pt height=14.15524440000002pt/>Q(s, a)<img src="/Lecture5-Model-Free-Control/tex/1b675153dd315c3ceba138ee9bef081b.svg?invert_in_darkmode&sanitize=true" align=middle width=244.30112354999997pt height=45.84475500000001pt/>\delta_t<img src="/Lecture5-Model-Free-Control/tex/fac9079e3c0c7d7e8890e67b05dbe1a1.svg?invert_in_darkmode&sanitize=true" align=middle width=135.21233385pt height=22.831056599999986pt/>E_t(s,a)<img src="/Lecture5-Model-Free-Control/tex/27728fe426f41c0b349ee0fa77589aae.svg?invert_in_darkmode&sanitize=true" align=middle width=8.219209349999991pt height=15.296829900000011pt/>\delta_t = R_{t+1} + \gamma Q(S_{t+1}, A_{t+1}) - Q(S_t, A_t)<img src="/Lecture5-Model-Free-Control/tex/d67bea32c301ebd5d63d6fcc3bb57b4e.svg?invert_in_darkmode&sanitize=true" align=middle width=230.92223219999994pt height=24.65753399999998pt/>

To sum up, the final algorithm is : 

<img src='./images/backward-sarsa_lambda.PNG'>

## Off-Policy Learning

Evaluate **target policy** <img src="/Lecture5-Model-Free-Control/tex/ed1967f6a60fcbb64f1da0f891adbb60.svg?invert_in_darkmode&sanitize=true" align=middle width=118.39655685pt height=24.65753399999998pt/>v_\pi(s)<img src="/Lecture5-Model-Free-Control/tex/a65bb86748f43a1e52d3e1d77fd8c92f.svg?invert_in_darkmode&sanitize=true" align=middle width=15.84100649999999pt height=14.15524440000002pt/>q_\pi(s,a)<img src="/Lecture5-Model-Free-Control/tex/0a640bddf30487875ce1a0dcf5f407ed.svg?invert_in_darkmode&sanitize=true" align=middle width=252.78618254999998pt height=45.84475499999998pt/>\mu(s|a)<img src="/Lecture5-Model-Free-Control/tex/006774e14a2d36bfcfe3afa42e6ed1f4.svg?invert_in_darkmode&sanitize=true" align=middle width=700.2747493499999pt height=203.6529759pt/>\mu<img src="/Lecture5-Model-Free-Control/tex/1996a27fc27833d3d4ca43d2d490687f.svg?invert_in_darkmode&sanitize=true" align=middle width=67.03413419999998pt height=22.831056599999986pt/>\pi<img src="/Lecture5-Model-Free-Control/tex/a27bec4da4c45298e1432b0d09731d7a.svg?invert_in_darkmode&sanitize=true" align=middle width=133.65674355pt height=22.831056599999986pt/>R + \gamma V(s')<img src="/Lecture5-Model-Free-Control/tex/735f27d772f70a5a01b9e655de9f42a9.svg?invert_in_darkmode&sanitize=true" align=middle width=700.27451835pt height=164.20092150000002pt/>A_{t+1} \sim \mu( . | S_t)<img src="/Lecture5-Model-Free-Control/tex/0ba90ec144304f99e4f385735aa0967f.svg?invert_in_darkmode&sanitize=true" align=middle width=318.52055399999995pt height=22.831056599999986pt/>A' \sim \pi(. | S_t)<img src="/Lecture5-Model-Free-Control/tex/40e7bcc54349a27f5b3d3dc4bf1fa8c6.svg?invert_in_darkmode&sanitize=true" align=middle width=87.48704084999999pt height=22.831056599999986pt/>Q(S_t, A_t)<img src="/Lecture5-Model-Free-Control/tex/ff12de01d6219a930c6ef9a39152506a.svg?invert_in_darkmode&sanitize=true" align=middle width=243.2489928pt height=22.831056599999986pt/>Q(S_t, A_t) \leftarrow Q(S_t, A_t) + \alpha (R_{t+1} + \gamma Q(S_{t+1} , A') - Q(S_t, A_t))

### Off-policy Control with Q-learning 

<img src='image/q-learning.PNG'>

<img src='images/q_learning_algo.PNG'>


## Summary


<img src='./images/summary.PNG'>

<img src='./images/summary_2.PNG'>