import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
from sklearn.metrics import silhouette_score


def k_means(x_set):
    clf = KMeans(n_clusters=3)
    y_predict = clf.fit_predict(x_set)
    plt.scatter(x_set[:, 0], x_set[:, 1], c=clf.labels_)
    plt.show()
    print('k_mean silhouette score:{}'.format(silhouette_score(x_set, y_predict)))


def dbscan(x_set):
    clf = DBSCAN(eps=0.43, min_samples=25)
    y_predict = clf.fit_predict(x_set)
    plt.scatter(x_set[:, 0], x_set[:, 1], c=clf.labels_)
    plt.show()
    print('dbscan silhouette score:{}'.format(silhouette_score(x_set, y_predict)))


def main():
    data_set = np.load('Data_for_Cluster.npz')
    x_set = data_set['X']
    y_set = data_set['labels_true']
    plt.scatter(x_set[:, 0], x_set[:, 1], c=y_set)
    plt.show()
    dbscan(x_set)
    k_means(x_set)


if __name__ == '__main__':
    main()
