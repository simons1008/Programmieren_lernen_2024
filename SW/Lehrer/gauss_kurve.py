# Plotting of 1-dimensional Gaussian distribution function
# https://stackoverflow.com/questions/14873203/plotting-of-1-dimensional-gaussian-distribution-function

from matplotlib import pyplot as mp
import numpy as np

def gaussian(x, mu, sig):
    return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))

x_values = np.linspace(-3, 3, 50)
mu = 0
sig = 2
y_values = gaussian(x_values, mu, sig)
print(y_values)
mp.plot(x_values, y_values)

mp.show()
