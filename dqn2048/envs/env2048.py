"""
Jake Mann 2024
Deep Q Learning 2048 Game
"""

import gym
from gym import error, spaces, utils
from gym.utils import seeding

class Env2048(gym.Env):
  metadata = {'render.modes': ['human']}

  def __init__(self):
    self.state = []
    for i in range(4):
      self.state += [[]]
      for j in range(4):
        self.state[i] += ["-"]
    self.counter = 0
    self.done = 0
    self.add = [0, 0]
    self.reward = 0
    self.reset()

  def step(self, action):
    ...
  
  def reset(self):
    ...

  def render(self, mode='human', close=False):
    for i in range(3):
      for j in range(3):
        print(self.state[i][j], end = " ")
      print("")
