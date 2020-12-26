import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.svm import LinearSVC
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from matplotlib.colors import ListedColormap
from sklearn.model_selection import train_test_split


# 3. build svm.LinearSVC
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


def main():
    # 1.
    # build data
    data, label = make_blobs(n_samples=1000, n_features=2, centers=2, cluster_std=[2.0, 2.0])

    # 2. draw
    plt.subplot(211)
    plt.scatter(data[:, 0], data[:, 1], c=label)
    plt.subplot(212)

    # set the test and train data and stand the data
    data_train, data_test, label_train, label_test = train_test_split(data, label, test_size=1 / 12, random_state=0)

    # Hard Margin SVM : C = 10**9  Soft Margin SVM: C = 0.01
    svc = LinearSVC(C=0.01)
    svc.fit(data_train, label_train)
    print("The accuracy is:")
    print(accuracy_score(label_test, svc.predict(data_test)))
    plot_decision_boundary(svc, data_train)
    plt.scatter(data_train[label_train == 0, 0], data_train[label_train == 0, 1], color='red')
    plt.scatter(data_train[label_train == 1, 0], data_train[label_train == 1, 1], color='blue')
    plt.show()


if __name__ == '__main__':
    main()
