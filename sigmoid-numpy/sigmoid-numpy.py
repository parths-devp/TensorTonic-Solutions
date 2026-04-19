import numpy as np

def sigmoid(x):
    array = np.array(x)
    y = -array
    return 1/(1+np.exp(y))