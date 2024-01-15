"""
Jake Mann 2024
Deep Q Learning 2048 Game
"""

import gym
from gym import error, spaces, utils
from gym.utils import seeding
import numpy as np
import os
import ctypes

np.random.seed(42)

class Env2048(gym.Env):
  metadata = {'render.modes': ['console', 'human']}

  def __init__(self):
    self.state = None
    self.counter = 0
    self.done = False
    self.oldgrid = None
    self.score = 0
    self.reset()

  def step(self, action):
    # UP DOWN LEFT RIGHT 0 1 2 3
    tempstate = None

    if action == 0:
      # UP: Transpose and reverse each row
      tempstate = [[row[i] for row in self.state] for i in range(len(self.state[0]))]
      tempstate = [l[::-1] for l in tempstate]
      tempstate = self.applymerge(tempstate)
      # Undo
      tempstate = [l[::-1] for l in tempstate]
      tempstate = [[row[i] for row in tempstate] for i in range(len(tempstate[0]))]

    elif action == 1:
      #DOWN : transpose only
      tempstate = [[row[i] for row in self.state] for i in range(len(self.state[0]))]
      tempstate = self.applymerge(tempstate)
      # Undo 
      tempstate = [[row[i] for row in tempstate] for i in range(len(tempstate[0]))]

    elif action == 2:
      #LEFT : just reverse em
      tempstate = [l[::-1] for l in self.state]
      tempstate = self.applymerge(tempstate)
      # Undo 
      tempstate = [l[::-1] for l in tempstate]

    elif action == 3:
      tempstate = self.state
      tempstate = self.applymerge(tempstate)

    self.state = tempstate
    done = self.is_game_over()
    self.render()

    return self.state, self.score, done, {}  
  
  def applymerge(self, grid):
    #makes a move to the right, following 2048 rules (I think)
    def move_right(my_list):
      zero_count = my_list.count(0)
      non_zero_elements = [x for x in my_list if x != 0]
      return [0] * zero_count + non_zero_elements
    def merge(row):
      thisrow = row[::-1]
      for i in range(len(thisrow) - 1):
        if thisrow[i] != 0 and thisrow[i] == thisrow[i+1]:
           thisrow[i] = thisrow[i]*2
           self.score += thisrow[i]*2
           thisrow[i+1] = 0
      row = thisrow[::-1]
      return row
    
    self.oldgrid = self.state #for later comparison
    newgrid = []
    # Move all the way to the right every time
    for row in grid:
      #if empty, pass
      if (sum(row) == 0):
        newgrid.append([0]*len(row))
        continue
      #move all tiles all the way to the right
      row = move_right(row)
      row = merge(row)    
      row = move_right(row)
      newgrid.append(row)
    
    if self.oldgrid != newgrid:
      self.new_tile(newgrid, 1)
      
    #print(score)
    #print(newgrid)
    return newgrid
  
  def is_game_over(self):
    for i in range(4):
        for j in range(4):
            # Check if the current tile is empty
            if self.state[i][j] == 0:
                return False
            # Check for same number in the right tile
            if j < 3 and self.state[i][j] == self.state[i][j + 1]:
                return False
            # Check for same number in the below tile
            if i < 3 and self.state[i][j] == self.state[i + 1][j]:
                return False
    # If no empty spaces and no adjacent same numbers, the game is over
    print("GAME OVER!")
    return True
  
  def reset(self):
    #Set the board back up- empty grid
    self.state = []
    for i in range(4):
      self.state += [[]]
      for j in range(4):
        self.state[i] += [0]
    # randomly set two tiles
    self.new_tile(self.state, 2)

    self.render()
    return self.state


  def new_tile(self, inputgrid, numtiles=1):
    zero_coordinates = [(i, j) for i in range(4) for j in range(4) if inputgrid[i][j] == 0]
    if len(zero_coordinates) >= numtiles:
        for _ in range(numtiles):
            # Randomly select a coordinate pair from zero_coordinates
            coord = np.random.choice(len(zero_coordinates))
            selected_coordinate = zero_coordinates[coord]
            # Set the selected coordinate to a new tile value (e.g., 2 or 4)
            inputgrid[selected_coordinate[0]][selected_coordinate[1]] = np.random.choice([2, 4], p=[.9, .1])
    else:
        print("Not enough empty cells to place new tiles.")

  def render(self, mode='console'):
        if mode == 'console':
            os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
            for row in self.state:
                print(row)
            print(f'\nscore: {self.score}')
            print()  # Extra line for separation
        elif mode == 'human':
            # Later, this will be used for Pygame rendering
            pass
