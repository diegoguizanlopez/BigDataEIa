import gymnasium as gym
import random
import numpy as np
import matplotlib.pyplot as plt

# render_mode="human"
environment = gym.make("FrozenLake-v1", is_slippery=False,
                       render_mode="human")
environment.reset()
environment.render()
print("asdkfjlas")