


import numpy as np
from scipy.optimize import minimize

#UAV-specific code
def some_cost_function(state, action_value):
    # Calculate the Euclidean distance between current position and goal position
    current_pos = (state['pos-x'], state['pos-y'], state['pos-z'])
    goal_pos = (state['GOAL-X'], state['GOAL-Y'], state['GOAL-Z'])
    distance = np.sqrt(np.sum((np.array(current_pos) - np.array(goal_pos)) ** 2))
    
    # Return the negative distance as the cost
    return -distance


class RandomAgent():
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
                
                cost = 0
                for t in range(self.horizon):
                    state['set-acc'] = action_values[t]
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
        
        elif self.action_space == "discrete":
            # Define the objective function to be minimized
            def objective_function(action_values):
                # Compute the cost or reward associated with the action sequence based on the current state and future predictions
                
                cost = 0
                for t in range(self.horizon):
                    state['set-acc'] = action_values[t]
                    cost += some_cost_function(state, action_values[t])
                
                return cost
            
            # Define the discrete action space
            action_space = list(range(self.num_actions))
            
            # Initialize the initial guess for action values
            initial_guess = np.random.choice(action_space, size=self.horizon)
            
            # Use scipy.optimize.minimize to find the optimal action values
            result = minimize(objective_function, initial_guess, bounds=[(0, self.num_actions-1)] * self.horizon, method='Nelder-Mead')
            
            # Extract the optimal action values
            optimal_action_values = result.x.astype(int)
            
            # Set the action to the first optimal action values
            action["action_values"] = optimal_action_values
        
        return action


    """def __init__(self, action_space, num_actions=0, horizon=5):
        self.action_space = action_space
        self.num_actions = num_actions
        self.horizon = horizon

    def sample_action(self, state=None):
        action = {}

        if self.action_space == "continuous":
            # Define the objective function to be minimized
            def objective_function(action_values):
                # Compute the cost or reward associated with the action sequence based on the current state and future predictions
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
        
        return action"""



