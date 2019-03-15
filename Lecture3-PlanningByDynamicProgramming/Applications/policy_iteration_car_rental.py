import numpy as np


class Location():
    def __init__(self, lambdaReturn, lambdaRequest, maximum_cars=20):
        self.maximum_cars = maximum_cars 
        self.lambdaRequest = lambdaRequest
        self.lambdaReturn = lambdaReturn
        self.nCars = 15
        self.reward_per_request = 10

    def update(self):
        cars_returned = np.random.poisson(self.lambdaReturn,1)
        cars_requested = np.random.poisson(self.lambdaRequest,1)
        if(cars_requested > self.nCars):
            self.nCars = 0
            #print('not enough cars !!')
        self.nCars += cars_returned - cars_requested
        if self.nCars > 20:
            self.nCars = 20
        return cars_requested * self.reward_per_request 

class Car_Rental():
    def __init__(self):
        self.loc1 = Location(3,3)
        self.loc1 = Location(2,4) 
        self.action_space = np.array(range(11)) - 5 #moving from loc1 to loc2

        # Start with Random Policy
        self.V = np.ones(2, len(self.action_space)) / self.action_space


    def policy_evaluation(self, gamma=0.9, epsilon=0.1):
        delta = 100
        while delta > epsilon:
            # for all states
            for  s in range(env.observation_space.n):
                sum = 0
                # for all posible actions
                for a, action_prob in enumerate(pi[:,s]):
                    # for all sucessive states of that given action
                    for prob, next_state, reward, done in env.P[s][a]:
                        sum += action_prob * (reward + gamma * prob * self.V[next_state]) 
                delta = abs(self.V[s] - sum)
                self.V[s] = sum   
        
    
    # def update(self):
    #     reward1 = self.loc1.update()
    #     reward2 = self.loc1.update() 

    #     return reward1 + reward2

    

car_rental = Car_Rental()

for i in range(100):
    _ = car_rental.update()