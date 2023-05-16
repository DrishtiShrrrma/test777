

"""class NoOpAgent():
    def __init__(self, action_space, num_actions=0):
        self.action_space = action_space
        self.num_actions = num_actions

    def sample_action(self, state=None):
        action = {}
        return action"""



Attempt 1:
    
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
