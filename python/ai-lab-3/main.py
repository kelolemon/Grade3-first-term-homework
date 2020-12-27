import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from matplotlib.colors import ListedColormap
from sklearn.cluster import DBSCAN


def plot_decision_boundary(model, x_train):
    h = .02
    x_min, x_max = x_train[:, 0].min() - .5, x_train[:, 0].max() + .5
    y_min, y_max = x_train[:, 1].min() - .5, x_train[:, 1].max() + .5
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    zz = model.predict(np.c_[xx.ravel(), yy.ravel()])
    zz = zz.reshape(xx.shape)
    custom_cmap = ListedColormap(['#EF9A9A', '#FFF59D', '#90CAF9'])
    plt.pcolormesh(xx, yy, zz, cmap=custom_cmap, shading='auto')


def k_means(x_set):
    clf = KMeans(n_clusters=3)
    clf.fit(x_set)
    plot_decision_boundary(clf, x_set)
    plt.scatter(x_set[:, 0], x_set[:, 1], c=clf.labels_)
    plt.show()


def dbscan(x_set):
    clf = DBSCAN(eps=0.43, min_samples=13)
    clf.fit(x_set)
    plt.scatter(x_set[:, 0], x_set[:, 1], c=clf.labels_)
    plt.show()


def main():
    data_set = np.load('Data_for_Cluster.npz')
    x_set = data_set['X']
    y_set = data_set['labels_true']
    dbscan(x_set)


if __name__ == '__main__':
    main()
