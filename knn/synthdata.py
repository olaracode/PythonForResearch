from knn import distance
import numpy as np
import random
import scipy.stats as ss
import matplotlib.pyplot as plt


# Standard deviation
def generate_synth_data(n=50):
    """
    Create two sets of points from bivariate normal distributions
    :param n: number of points
    :return: a tuple containing points and outcomes
    """

    points = np.concatenate((ss.norm(0, 1).rvs((n, 2)), ss.norm(1, 1).rvs((n, 2))))
    outcomes = np.concatenate((np.repeat(0, n), np.repeat(1, n)))
    return (points, outcomes)

# n = 20
# points, outcome = generate_synth_data(n)
# plt.figure()
# plt.plot(points[:n, 0], points[:n, 1], "ro")
# plt.plot(points[n:, 0], points[n:, 1], "bo")
# plt.show()