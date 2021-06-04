import numpy as np
import matplotlib.pyplot as plt
from knn import distance
from majvote import majority_vote


# first step: loop over all points
#     compute the distance between point p and every other point
# sort distances and return k points that are nearest to point p
def find_nearest_neighbors(p, points, k=5):
    """
    Find the k nearest neighbors of point p and return their indices
    :param p: Unclassified points
    :param points: points to compare and to check distance
    :param k: nª of neighbors(with default 5)
    :return: indices of those points
    """
    distances = np.zeros(points.shape[0])
    for i in range(len(distances)):
        distances[i] = distance(p, points[i])
    ind = np.argsort(distances)
    return ind[:k]


def knn_predict(p, points, outcomes, k=5):
    # find k nearest neighbors
    ind = find_nearest_neighbors(p, points, k)
    # predict the class of p based on majority vote
    return majority_vote(outcomes[ind])


# points = np.array([[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3]])
# outcomes = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1])
# p = np.array([2.5, 2])
#
# plt.plot(points[:, 0], points[:, 1], "ro")
# plt.plot(p[0], p[1], "bo")
# # plt.show()
# x = knn_predict(np.array([2.5, 2.7]), points, outcomes, k=2)
# y = knn_predict(np.array([1.0, 2.7]), points, outcomes, k=2)
# print(x)
# print(y)