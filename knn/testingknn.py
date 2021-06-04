from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
from knn import distance
from synthdata import generate_synth_data
from predict_grid import make_prediction_grid
from findingknn import find_nearest_neighbors, knn_predict
import numpy as np
import random
import scipy.stats as ss

def plot_prediction_grid (xx, yy, prediction_grid, filename):
    """ Plot KNN predictions for every point on the grid."""
    from matplotlib.colors import ListedColormap
    background_colormap = ListedColormap(["hotpink", "lightskyblue", "yellowgreen"])
    observation_colormap = ListedColormap(["red", "blue", "green"])
    plt.figure(figsize=(10, 10))
    plt.pcolormesh(xx, yy, prediction_grid, cmap=background_colormap, alpha=0.5)
    plt.scatter(predictors[:, 0], predictors[:, 1], c=outcomes, cmap=observation_colormap, s=50)
    plt.xlabel('Variable 1'); plt.ylabel('Variable 2')
    plt.xticks(()); plt.yticks(())
    plt.xlim(np.min(xx), np.max(xx))
    plt.ylim(np.min(yy), np.max(yy))
    plt.savefig(filename)




iris = datasets.load_iris()
# print(iris["data"])

predictors = iris.data[:, :2]
outcomes = iris.target
# plt.plot(predictors[outcomes == 0][:, 0], predictors[outcomes == 0][:, 1], "ro")
# plt.plot(predictors[outcomes == 1][:, 0], predictors[outcomes == 1][:, 1], "go")
# plt.plot(predictors[outcomes == 2][:, 0], predictors[outcomes == 2][:, 1], "bo")
#
# # plt.show()
#
# k = 5; filename = "iris_grid.pdf"; limits = (4, 8, 1.5, 4.5); h = 0.1
# (xx, yy, prediction_grid) = make_prediction_grid(predictors, outcomes, limits, h, k)
# plot_prediction_grid(xx, yy, prediction_grid, filename)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(predictors, outcomes)
sk_predictions = knn.predict(predictors)

my_predictions = np.array([knn_predict(p, predictors, outcomes, 5) for p in predictors])
# print(my_predictions.shape)

print(100*np.mean(sk_predictions == my_predictions))

print(100*np.mean(sk_predictions == outcomes))
print(100*np.mean(my_predictions == outcomes))


