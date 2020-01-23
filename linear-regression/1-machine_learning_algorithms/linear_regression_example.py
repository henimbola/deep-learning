# Importing relevent libraries

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def generate_dataset():
    """
        This function generates inputs and the targets of the datasets
        :param observations
        :param xs
        :param zs
        :param inputs
    """
    observations = 1000
    xs = np.random.uniform(low=-10, high=10, size=(observations, 1))
    zs = np.random.uniform(low=-10, high=10, size=(observations, 1))
    inputs = np.column_stack((xs, zs))
    noise = np.random.uniform(low=-1, high=1, size=(observations, 1))
    targets = 3*xs + 2*zs + 5 + noise

    return targets, inputs 

print(generate_dataset()[1].shape)

# Model

# Objective function

# Optimization algorithm
