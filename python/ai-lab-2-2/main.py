from sklearn import datasets
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_recall_curve
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from matplotlib.colors import ListedColormap


# draw the decision boundary
def plot_decision_boundary(model, x_train):
    h = .02
    x_min, x_max = x_train[:, 0].min() - .5, x_train[:, 0].max() + .5
    y_min, y_max = x_train[:, 1].min() - .5, x_train[:, 1].max() + .5
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    zz = model.predict(np.c_[xx.ravel(), yy.ravel()])
    zz = zz.reshape(xx.shape)
    custom_cmap = ListedColormap(['#A0FFA0', '#FFA0A0', '#A0A0FF'])
    plt.pcolormesh(xx, yy, zz, cmap=custom_cmap, shading='auto')


def main():
    # load the datasets and separate the test and train data
    data_set = datasets.load_iris()
    x_train = data_set.data[:130, 0:2]
    y_train = data_set.target[:130]
    x_test = data_set.data[130:, 0:2]
    y_test = data_set.target[130:]

    # set the model and train the data
    clf = SVC(C=0.8, kernel='rbf', gamma=20, decision_function_shape='ovr')
    clf.fit(x_train, y_train)
    plt.subplot(211)
    plot_decision_boundary(clf, x_train)
    my_cmap = ListedColormap(['g', 'r', 'b'])
    plt.scatter(x_train[:, 0], x_train[:, 1], c=y_train, edgecolors='k', s=50, cmap=my_cmap)
    plt.subplot(212)

    # get the accuracy, precision and recall
    print('高斯核函数SVM的精度为:{}'.format(accuracy_score(y_test, clf.predict(x_test))))
    precision, recall, _ = precision_recall_curve(y_test, clf.predict(x_test), pos_label=2)
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.figure(1)
    plt.plot(precision, recall)
    plt.show()


if __name__ == '__main__':
    main()
