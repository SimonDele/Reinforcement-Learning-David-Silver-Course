# Lecture 5 : Model-Free Control

[Lecture](https://www.youtube.com/watch?v=0g4j2k_Ggc4&list=PLqYmG7hTraZDM-OYHWgPebj2MfCFzFObQ&index=5), [Slides](http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching_files/control.pdf)


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

For any <img src="/Lecture5-Model-Free-Control/tex/7ccca27b5ccc533a2dd72dc6fa28ed84.svg?invert_in_darkmode&sanitize=true" align=middle width=6.672392099999992pt height=14.15524440000002pt/>-greedy policy <img src="/Lecture5-Model-Free-Control/tex/f30fdded685c83b0e7b446aa9c9aa120.svg?invert_in_darkmode&sanitize=true" align=middle width=9.96010619999999pt height=14.15524440000002pt/>, the <img src="/Lecture5-Model-Free-Control/tex/7ccca27b5ccc533a2dd72dc6fa28ed84.svg?invert_in_darkmode&sanitize=true" align=middle width=6.672392099999992pt height=14.15524440000002pt/>-greedy policy <img src="/Lecture5-Model-Free-Control/tex/e1c4ca96d10da0d56ad235b3b5fe363e.svg?invert_in_darkmode&sanitize=true" align=middle width=13.750048949999991pt height=24.7161288pt/> with respect to <img src="/Lecture5-Model-Free-Control/tex/d9fad2914b7324ed12eb8bd6f289f92b.svg?invert_in_darkmode&sanitize=true" align=middle width=8.099960549999992pt height=14.15524440000002pt/> is an improvement, i.e <img src="/Lecture5-Model-Free-Control/tex/fc2fe3f10893121afc9b96985a6e2fcd.svg?invert_in_darkmode&sanitize=true" align=middle width=96.67934264999998pt height=24.7161288pt/>

Can be proven in a few lines...

### Monte-Carlo Control

Every episode : 
* Policy evaluation : Monte-Carlo policy evaluation <img src="/Lecture5-Model-Free-Control/tex/0d07098d4d69b1160fe8f507a7ceca34.svg?invert_in_darkmode&sanitize=true" align=middle width=50.35132739999999pt height=22.465723500000017pt/>
* Policy improvement : <img src="/Lecture5-Model-Free-Control/tex/7ccca27b5ccc533a2dd72dc6fa28ed84.svg?invert_in_darkmode&sanitize=true" align=middle width=6.672392099999992pt height=14.15524440000002pt/>-greedy improvement

### GLIE : Greedy in the Limit with Infinite Exploration
* All state-action pairs are explored infinitely many times
* The policy converges on a greedy policy

<img src="/Lecture5-Model-Free-Control/tex/7ccca27b5ccc533a2dd72dc6fa28ed84.svg?invert_in_darkmode&sanitize=true" align=middle width=6.672392099999992pt height=14.15524440000002pt/>-greedy is GLIE for <img src="/Lecture5-Model-Free-Control/tex/3dd7247f8f7b91b6b4fe86173ef55403.svg?invert_in_darkmode&sanitize=true" align=middle width=62.19175379999999pt height=24.65753399999998pt/> for example.


### GLIE Monte-Carlo Control

* Sample kth episode using <img src="/Lecture5-Model-Free-Control/tex/f30fdded685c83b0e7b446aa9c9aa120.svg?invert_in_darkmode&sanitize=true" align=middle width=9.96010619999999pt height=14.15524440000002pt/>
* For each state <img src="/Lecture5-Model-Free-Control/tex/9f8bba50b95de09625626ddafa0698eb.svg?invert_in_darkmode&sanitize=true" align=middle width=15.04571639999999pt height=22.465723500000017pt/> and action <img src="/Lecture5-Model-Free-Control/tex/df02e7666c632d22547b9c75b98c49bf.svg?invert_in_darkmode&sanitize=true" align=middle width=17.29459049999999pt height=22.465723500000017pt/> in the episode

<img src="/Lecture5-Model-Free-Control/tex/780a43e27251f9456e6ee62436742095.svg?invert_in_darkmode&sanitize=true" align=middle width=192.03177015pt height=24.65753399999998pt/>

<img src="/Lecture5-Model-Free-Control/tex/38982a3c870a729c261ada57fbe30437.svg?invert_in_darkmode&sanitize=true" align=middle width=374.8446174pt height=24.65753399999998pt/>

* Improve policy based on new action-value function

<img src="/Lecture5-Model-Free-Control/tex/e5ee2039be7d4bdcd9c0b80772b6dde1.svg?invert_in_darkmode&sanitize=true" align=middle width=57.75677984999999pt height=24.65753399999998pt/>

<img src="/Lecture5-Model-Free-Control/tex/ca1c0ff853b51e94520537ec36c72b62.svg?invert_in_darkmode&sanitize=true" align=middle width=136.89188699999997pt height=24.65753399999998pt/>


**TODO** application on Black-jack




## On-Policy Temporal-Difference Learning


### SARSA :

Global idea : use TD instead of MC in our control loop

<img src='./images/sarsa.png'>

<img src='./images/sarsa_algo.PNG'>

**Theorem** 

SARSA converges to the optimal action-value function, under the following conditions :
* GLIE sequence of policies <img src="/Lecture5-Model-Free-Control/tex/3d616719b01083e04b7706e1ba8f0219.svg?invert_in_darkmode&sanitize=true" align=middle width=48.90429224999998pt height=24.65753399999998pt/>
* Robbins-Monro squence of step-sizes <img src="/Lecture5-Model-Free-Control/tex/583ce5b96b9bb83e6e6c47a06a398ef9.svg?invert_in_darkmode&sanitize=true" align=middle width=15.48143849999999pt height=14.15524440000002pt/>

<img src="/Lecture5-Model-Free-Control/tex/b8cf98c8672631ad01fa9d572f328eed.svg?invert_in_darkmode&sanitize=true" align=middle width=78.13928429999999pt height=26.438629799999987pt/>
<img src="/Lecture5-Model-Free-Control/tex/832a8d852fd51f9779ee17e36d47890a.svg?invert_in_darkmode&sanitize=true" align=middle width=78.13928429999999pt height=26.438629799999987pt/>


### n-step Sarsa

<img src='./images/n-step_sarsa.PNG'>

### Sarsa(<img src="/Lecture5-Model-Free-Control/tex/fd8be73b54f5436a5cd2e73ba9b6bfa9.svg?invert_in_darkmode&sanitize=true" align=middle width=9.58908224999999pt height=22.831056599999986pt/>)

Average all n-steps Sarsa :

<img src="/Lecture5-Model-Free-Control/tex/13c3035d325d20a9ec131a7f22138523.svg?invert_in_darkmode&sanitize=true" align=middle width=199.26390494999998pt height=34.337843099999986pt/>

Forward view : <img src="/Lecture5-Model-Free-Control/tex/d6a2ee3fb7a3e994c56ed86823c4ced3.svg?invert_in_darkmode&sanitize=true" align=middle width=306.87427154999995pt height=27.91243950000002pt/>

### Backward-view Sarsa(<img src="/Lecture5-Model-Free-Control/tex/fd8be73b54f5436a5cd2e73ba9b6bfa9.svg?invert_in_darkmode&sanitize=true" align=middle width=9.58908224999999pt height=22.831056599999986pt/>)

Use **eligibility traces** in an online algorithm

Sarsa(<img src="/Lecture5-Model-Free-Control/tex/fd8be73b54f5436a5cd2e73ba9b6bfa9.svg?invert_in_darkmode&sanitize=true" align=middle width=9.58908224999999pt height=22.831056599999986pt/>) has one eligibiliy trace for each state-action pair
* <img src="/Lecture5-Model-Free-Control/tex/13ad418c2658711e2b9593b375d69c31.svg?invert_in_darkmode&sanitize=true" align=middle width=86.13196844999999pt height=24.65753399999998pt/>
* <img src="/Lecture5-Model-Free-Control/tex/b3719d2213508a018cc248e52fb3f3bb.svg?invert_in_darkmode&sanitize=true" align=middle width=299.89721354999995pt height=24.65753399999998pt/>

<img src="/Lecture5-Model-Free-Control/tex/117ae84ef4502431c8cb477a2063ab73.svg?invert_in_darkmode&sanitize=true" align=middle width=49.48137479999998pt height=24.65753399999998pt/> is updated for every state and action

In proportion to the TD-error <img src="/Lecture5-Model-Free-Control/tex/10ea9eec57d7dd8109d5e58e9baf6620.svg?invert_in_darkmode&sanitize=true" align=middle width=12.27173144999999pt height=22.831056599999986pt/> and eligibility trace <img src="/Lecture5-Model-Free-Control/tex/1976738d6b55a6d7419b48a6fa9df6f8.svg?invert_in_darkmode&sanitize=true" align=middle width=54.408357299999984pt height=24.65753399999998pt/>
* <img src="/Lecture5-Model-Free-Control/tex/160f49a95dbb6a5d198ab10410d7f458.svg?invert_in_darkmode&sanitize=true" align=middle width=286.96007834999995pt height=24.65753399999998pt/>
* <img src="/Lecture5-Model-Free-Control/tex/e429c3bb8222fa74943a20dd276a8c76.svg?invert_in_darkmode&sanitize=true" align=middle width=222.70302284999994pt height=24.65753399999998pt/>

To sum up, the final algorithm is : 

<img src='./images/backward-sarsa_lambda.PNG'>

## Off-Policy Learning

Evaluate **target policy** <img src="/Lecture5-Model-Free-Control/tex/a5f75f5c24cae21447686b47e4f99d38.svg?invert_in_darkmode&sanitize=true" align=middle width=43.70637809999999pt height=24.65753399999998pt/> to compute <img src="/Lecture5-Model-Free-Control/tex/85aed0b0f7b723a72042b5a7378030bf.svg?invert_in_darkmode&sanitize=true" align=middle width=37.38085559999999pt height=24.65753399999998pt/> or <img src="/Lecture5-Model-Free-Control/tex/f4fd307c043a8d1ae7d10dec8715ec8f.svg?invert_in_darkmode&sanitize=true" align=middle width=52.74613904999998pt height=24.65753399999998pt/>

While **following behaviour** policy <img src="/Lecture5-Model-Free-Control/tex/44466e9be069ee87b299d635e626d0f5.svg?invert_in_darkmode&sanitize=true" align=middle width=43.65121529999999pt height=24.65753399999998pt/>

Interest : 
* Learn  from observing humans or other agents
* Re-use experience generated from old policies
* Learn about *optimal* policy while following *exploratory* policy
* Learn about *multiple* policies while following one policy

### Importance Sampling for Off-Policy TD

* Use TD targets generated from <img src="/Lecture5-Model-Free-Control/tex/07617f9d8fe48b4a7b3f523d6730eef0.svg?invert_in_darkmode&sanitize=true" align=middle width=9.90492359999999pt height=14.15524440000002pt/> to evalute <img src="/Lecture5-Model-Free-Control/tex/f30fdded685c83b0e7b446aa9c9aa120.svg?invert_in_darkmode&sanitize=true" align=middle width=9.96010619999999pt height=14.15524440000002pt/>
* Weight TD target <img src="/Lecture5-Model-Free-Control/tex/37656f3b25fd7bf8af232b869a9aa6e0.svg?invert_in_darkmode&sanitize=true" align=middle width=80.46834179999999pt height=24.7161288pt/> by importance sampling
* Only need a single importance sampling correction

<img src='images/formule_importance.PNG'>

### Q-learning

* We now consider off-policy learning of action-value Q(s, a)
* No importance sampling is required
* Next action is chosen using behaviour policy <img src="/Lecture5-Model-Free-Control/tex/074e883bbfdf3742df280ef6e9a36994.svg?invert_in_darkmode&sanitize=true" align=middle width=104.36844659999998pt height=24.65753399999998pt/>
* But we consider alternantive succesor action <img src="/Lecture5-Model-Free-Control/tex/c8b479b680cfff8c8768d2dc451a2325.svg?invert_in_darkmode&sanitize=true" align=middle width=86.60388659999998pt height=24.7161288pt/>
* And update <img src="/Lecture5-Model-Free-Control/tex/bd388eab74bded5ef1295c4b6abbacf5.svg?invert_in_darkmode&sanitize=true" align=middle width=67.07084009999998pt height=24.65753399999998pt/> towards value of alternative action

<img src="/Lecture5-Model-Free-Control/tex/2a3ada3cdd4ba0a1d8d8b3a9d4a2effc.svg?invert_in_darkmode&sanitize=true" align=middle width=437.29450049999997pt height=24.7161288pt/>

### Off-policy Control with Q-learning 

<img src='images/q_learning.PNG'>

<img src='images/q_learning_algo.PNG'>


## Summary


<img src='./images/summary.PNG'>

<img src='./images/summary_2.PNG'>