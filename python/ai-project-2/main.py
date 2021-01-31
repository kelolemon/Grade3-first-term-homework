from sklearn import linear_model
from sklearn.svm import SVC
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn import neighbors
from sklearn import linear_model
from sklearn import metrics
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# read data
def load_data():
    data_set = pd.read_table("data_banknote_authentication.txt", header=None, sep=',')
    return data_set[0], data_set[1], data_set[2], data_set[3], data_set[4]


# using four features and split the data set
def use_four_features(x_0_set, x_1_set, x_2_set, x_3_set, y_set):
    x_set = list(zip(x_0_set, x_1_set, x_2_set, x_3_set))
    x_set = np.array(x_set)
    return train_test_split(x_set, y_set, train_size=1200)


def decision_tree(x_train, x_test, y_train, y_test):
    clf = tree.DecisionTreeClassifier()
    clf.fit(x_train, y_train)
    y_predict = clf.predict(x_test)
    print(metrics.precision_score(y_test, y_predict))
    print(metrics.recall_score(y_test, y_predict))


def logistics_classifier(x_train, x_test, y_train, y_test):
    logistics = linear_model.LogisticRegression()
    logistics.fit(x_train, y_train)
    y_predict = logistics.predict(x_test)
    print(metrics.precision_score(y_test, y_predict))
    print(metrics.recall_score(y_test, y_predict))


def svc_classifier(x_train, x_test, y_train, y_test):
    clf = SVC(C=0.8, kernel='rbf', gamma=2, decision_function_shape='ovr')
    clf.fit(x_train, y_train)
    y_predict = clf.predict(x_test)
    print(metrics.precision_score(y_test, y_predict))
    print(metrics.recall_score(y_test, y_predict))


def knn_classifier(x_train, x_test, y_train, y_test):
    knn = neighbors.KNeighborsClassifier(n_neighbors=2, weights='uniform', algorithm='auto')
    knn.fit(x_train, y_train)
    y_predict = knn.predict(x_test)
    print(metrics.precision_score(y_test, y_predict))
    print(metrics.recall_score(y_test, y_predict))


def main():
    load_data()
    x_0_set, x_1_set, x_2_set, x_3_set, y_set = load_data()
    x_train, x_test, y_train, y_test = use_four_features(x_0_set, x_1_set, x_2_set, x_3_set, y_set)
    decision_tree(x_train, x_test, y_train, y_test)
    logistics_classifier(x_train, x_test, y_train, y_test)
    svc_classifier(x_train, x_test, y_train, y_test)
    knn_classifier(x_train, x_test, y_train, y_test)


if __name__ == '__main__':
    main()
