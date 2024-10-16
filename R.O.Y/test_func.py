import numpy as np

def Ackley(x, y):
    res1 = -0.2 * np.sqrt(0.5 * (x ** 2 + y ** 2))
    res2 = 0.5 * (np.cos(2 * np.pi * x) + np.cos(2 * np.pi * y))
    return -20 * np.exp(res1) - np.exp(res2) + np.e + 20

def Bila(x, y):
    return (1.5 - x + x * y) ** 2 + (2.25 - x + x * y ** 2) ** 2 + (2.625 - x + x * y ** 3) ** 2