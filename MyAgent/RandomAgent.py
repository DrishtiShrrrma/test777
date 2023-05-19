

class RandomAgent():

    def __init__(self, action_space, num_actions=0):
      self.action_space = action_space
      self.num_actions = num_actions

    
    def sample_actions(self, state=None):
      begin = 1
      future = 100
      generate = numpy.random.poisson(lam=5.0, size=future)
      fib = fibonacci(start=begin, length=future)
      action = generate/fib
      action = action.sum()
      return action
