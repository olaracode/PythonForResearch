from knn import distance
from findingknn import find_nearest_neighbors, knn_predict
import numpy as np
import random
import scipy.stats as ss
import matplotlib.pyplot as plt


def make_prediction_grid(predictors, outcomes, limits, h, k):
    """
    Classify each point on the prediction grid
    :param predictors:
    :param outcomes:
    :param limits:
    :param h:
    :param k:
    :return:
    """
    (x_min, x_max, y_min, y_max) = limits
    xs = np.arange(x_min, x_max, h)
    ys = np.arange(y_min, y_max, h)
    xx, yy = np.meshgrid(xs, ys)

    prediction_grid = np.zeros(xx.shape, dtype=int)
    for i, x in enumerate(xs):
        for j, y in enumerate(ys):
            p = np.array([x, y])
            prediction_grid[j, i] = knn_predict(p, predictors, outcomes, k)
    return (xx, yy, prediction_grid)

