

"""class NoOpAgent():
    def __init__(self, action_space, num_actions=0):
        self.action_space = action_space
        self.num_actions = num_actions

    def sample_action(self, state=None):
        action = {}
        return action"""



# Attempt 1:
    
import random

class NoOpAgent:
    def __init__(self, action_space, num_actions=0):
        self.action_space = action_space
        self.num_actions = num_actions

    def sample_action(self, state=None):
        # Defining action selection strategy/policy
        
        
        action = {}
        
        # If the action space is discrete, select a random action index
        if self.action_space == "discrete":
            action_index = random.randint(0, self.num_actions - 1)
            action["action_index"] = action_index
        
        # If the action space is continuous, select random action values
        elif self.action_space == "continuous":
            action_values = [random.uniform(0, 1) for _ in range(self.num_actions)]
            action["action_values"] = action_values
        
        return action
    
   
# Attempt 2:

import numpy as np
from scipy.optimize import minimize

class NoOpAgent:
    def __init__(self, action_space, num_actions=0, horizon=5):
        self.action_space = action_space
        self.num_actions = num_actions
        self.horizon = horizon

    def sample_action(self, state=None):
        # Defining MPC algorithm 
        # we can use scipy.optimize.minimize to optimize an objective function
        
        action = {}
        
        if self.action_space == "continuous":
            # Define the objective function to be minimized
            def objective_function(action_values):
                # Compute the cost or reward associated with the action sequence based on the current state and future predictions
                
                # Needs to be replaced!
                cost = 0
                for t in range(self.horizon):
                    cost += some_cost_function(state, action_values[t])
                
                return cost
            
            # Set the bounds for action values
            bounds = [(0, 1)] * self.num_actions
            
            # Initialize the initial guess for action values
            initial_guess = np.random.uniform(0, 1, self.num_actions * self.horizon)
            
            # Use scipy.optimize.minimize to find the optimal action values
            result = minimize(objective_function, initial_guess, bounds=bounds)
            
            # Extract the optimal action values
            optimal_action_values = result.x.reshape((self.horizon, self.num_actions))
            
            # Set the action to the first optimal action values
            action["action_values"] = optimal_action_values[0]
        
        return action


