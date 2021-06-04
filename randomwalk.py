import random
import numpy as np
import matplotlib.pyplot as plt

"""
-> Random Walk
x(t=0) = x0
x(t=1) = x(t=0) + deltax(t=1) \ x0+deltax(t=1)
x(t=2) = x(t=1) + deltax(t=2)

-> Cumulative sum
numpy.cumsum/np.cumsum()

-> concatenate

"""
x_0 = np.array([[0], [0]])
delta_x = np.random.normal(0, 1, (2, 5))
# plt.plot(delta_x[0], delta_x[1], "go")
x = np.concatenate((x_0, np.cumsum(delta_x, axis=1)), axis=1)
plt.plot(delta_x[0], x[1], "go-")
plt.show()