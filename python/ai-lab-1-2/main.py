import pandas as pd
from matplotlib.colors import ListedColormap
from sklearn.model_selection import train_test_split
from sklearn import linear_model
import matplotlib.pyplot as plt
import numpy as np


# draw the decision boundary
def plot_decision_boundary(model, x_train):
    h = .02
    x_min, x_max = x_train[:, 0].min() - .5, x_train[:, 0].max() + .5
    y_min, y_max = x_train[:, 1].min() - .5, x_train[:, 1].max() + .5
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    zz = model.predict(np.c_[xx.ravel(), yy.ravel()])
    zz = zz.reshape(xx.shape)
    custom_cmap = ListedColormap(['#EF9A9A', '#FFF59D', '#90CAF9'])
    plt.pcolormesh(xx, yy, zz, cmap=custom_cmap, shading='auto')


def logistic_regression(x_train, x_predict, y_train, y_predict):
    logistic_reg = linear_model.LogisticRegression(solver='newton-cg')
    logistic_reg.fit(x_train, y_train)
    plt.subplot(313)
    plot_decision_boundary(logistic_reg, x_train)
    setosa_sample = x_train[y_train == 0, :]
    versicolor_sample = x_train[y_train == 1, :]
    virginica_sample = x_train[y_train == 2, :]
    plt.scatter(setosa_sample[:, 0], setosa_sample[:, 1], label='setosa', marker='o', color='red')
    plt.scatter(versicolor_sample[:, 0], versicolor_sample[:, 1], label='versicolor', marker='x', color='blue')
    plt.scatter(virginica_sample[:, 0], virginica_sample[:, 1], label='virginica', marker='s', color='green')
    plt.subplot(334)
    y_pre = logistic_reg.predict(x_predict)
    plt.plot(y_predict, label='true', color='red')
    plt.subplot(335)
    plt.plot(y_pre, label='predict', color='blue')
    plt.subplot(336)
    plt.plot(y_pre, label='predict', color='blue')
    plt.plot(y_predict, label='true', color='red')
    plt.show()
    print(logistic_reg.score(x_train, y_train))


def main():
    # load data
    data_set = pd.read_table('iris.data.txt', header=None, sep=',')

    # set and get x set
    x_set = data_set.iloc[:, 1:3]
    # set and get y set
    y_set = data_set[4].values
    for i in range(len(y_set)):
        if y_set[i] == 'Iris-setosa':
            y_set[i] = 0
        if y_set[i] == 'Iris-versicolor':
            y_set[i] = 1
        if y_set[i] == 'Iris-virginica':
            y_set[i] = 2
    # split the training set and predict set
    y_set = np.array(y_set, dtype=np.float)
    x_train, x_predict, y_train, y_predict = train_test_split(x_set.values, y_set, test_size=1 / 12,
                                                              random_state=0)
    # show the data distribution
    setosa_sample = x_train[y_train == 0, :]
    versicolor_sample = x_train[y_train == 1, :]
    virginica_sample = x_train[y_train == 2, :]
    plt.subplot(311)
    plt.scatter(setosa_sample[:, 0], setosa_sample[:, 1], label='setosa', marker='o', color='red')
    plt.scatter(versicolor_sample[:, 0], versicolor_sample[:, 1], label='versicolor', marker='x', color='blue')
    plt.scatter(virginica_sample[:, 0], virginica_sample[:, 1], label='virginica', marker='s', color='green')
    # begin to train
    logistic_regression(x_train, x_predict, y_train, y_predict)


if __name__ == '__main__':
    main()
