from sklearn import linear_model
from sklearn.svm import SVR
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn import metrics
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def mse_metrics(y_test, y_predict):
    return metrics.mean_squared_error(y_test, y_predict)


def r_mse_metrics(y_test, y_predict):
    return np.sqrt(metrics.mean_squared_error(y_test, y_predict))


def load_data():
    data_set = pd.read_table('quake.dat', header=None, sep=',', comment='@')
    x_0_set = data_set[0].values
    x_1_set = data_set[1].values
    x_2_set = data_set[2].values
    y_set = data_set[3].values
    return x_0_set, x_1_set, x_2_set, y_set


def use_three_features(x_0_set, x_1_set, x_2_set, y_set):
    x_set = list(zip(x_0_set, x_1_set, x_2_set))
    x_set = np.array(x_set)
    return train_test_split(x_set, y_set, train_size=2000)


def use_two_features(x_0_set, x_1_set, y_set):
    x_set = list(zip(x_0_set, x_1_set))
    x_set = np.array(x_set)
    return train_test_split(x_set, y_set, train_size=2000)


def use_one_features(x_set, y_set):
    x_set = x_set.reshape(-1, 1)
    x_set = np.array(x_set)
    return train_test_split(x_set, y_set, train_size=2000)


def draw_compare_line(y_test, y_predict):
    plt.plot(y_test, color='red')
    plt.plot(y_predict, color='blue')
    plt.show()


def linear_regression(x_train, x_test, y_train, y_test):
    line = linear_model.LinearRegression()
    line.fit(x_train, y_train)
    y_predict = line.predict(x_test)
    draw_compare_line(y_test, y_predict)
    print("mse:{}".format(mse_metrics(y_test, y_predict)))
    print("rmse:{}".format(+ r_mse_metrics(y_test, y_predict)))


def svr_regression(x_train, x_test, y_train, y_test):
    clf = SVR(kernel='rbf')
    clf.fit(x_train, y_train)
    y_predict = clf.predict(x_test)
    draw_compare_line(y_test, y_predict)
    print("mse:{}".format(mse_metrics(y_test, y_predict)))
    print("rmse:{}".format(+ r_mse_metrics(y_test, y_predict)))


def neural_network_regression(x_train, x_test, y_train, y_test):
    mpl = MLPRegressor()
    mpl.fit(x_train, y_train)
    y_predict = mpl.predict(x_test)
    draw_compare_line(y_test, y_predict)
    print("mse:{}".format(mse_metrics(y_test, y_predict)))
    print("rmse:{}".format(+ r_mse_metrics(y_test, y_predict)))


def decision_tree(x_train, x_test, y_train, y_test):
    clf = tree.DecisionTreeRegressor()
    clf.fit(x_train, y_train)
    y_predict = clf.predict(x_test)
    draw_compare_line(y_test, y_predict)
    print("mse:{}".format(mse_metrics(y_test, y_predict)))
    print("rmse:{}".format(+ r_mse_metrics(y_test, y_predict)))


def main():
    x_0_set, x_1_set, x_2_set, y_set = load_data()
    x_train, x_test, y_train, y_test = use_three_features(x_0_set, x_1_set, x_2_set, y_set)
    # plt.scatter(x_2_set, x_0_set, c=y_set)
    # plt.show()
    svr_regression(x_train, x_test, y_train, y_test)
    # linear_regression(x_train, x_test, y_train, y_test)
    # neural_network_regression(x_train, x_test, y_train, y_test)
    # decision_tree(x_train, x_test, y_train, y_test)


if __name__ == '__main__':
    main()
