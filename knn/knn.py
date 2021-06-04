import numpy as np


def distance(p1, p2):
    """
    With this function we will find the distance between two points.
    This is very important as the first step to use K-nearest neighbour is finding the distance between
    each point
    REQUIREMENTS: importing numpy as np
    :param p1: the location of the first point
    :param p2: the location of the second point
    :return: the distance that separates these points
    """
    # np.power takes two arguments, the value(or operation) and then the number we want to power it to
    x = np.sqrt(np.sum(np.power(p2 - p1, 2)))
    return x


p1 = np.array([1, 1])
p2 = np.array([4, 4])
# print(distance(p1, p2))

