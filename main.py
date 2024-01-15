import numpy as np
import os
import gym
from dqn2048.envs.env2048 import Env2048  # Assuming your class is in env_2048.py

def main():
    # Create an instance of your 2048 environment
    env = Env2048()

    # Mapping of user input to actions
    action_mapping = {
        'w': 0,  # Up
        's': 1,  # Down
        'a': 2,  # Left
        'd': 3,  # Right
    }

    # Initial setup
    state = env.reset()
    done = False

    # Game loop
    while not done:
        env.render()

        # Get user input for the next move
        move = input("Next move (w/a/s/d): ").strip().lower()
        if move in action_mapping:
            # Perform the action
            state, reward, done, info = env.step(action_mapping[move])
            print(f"Reward: {reward}")
        else:
            print("Invalid move. Please enter 'w', 'a', 's', or 'd'.")

        # Check if the game is over
        if done:
            print("Game over!")
            break

    env.render()
    print("Final state:")

if __name__ == "__main__":
    main()
