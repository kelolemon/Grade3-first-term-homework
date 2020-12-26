import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.svm import LinearSVC
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score


# 3. build svm.LinearSVC
# draw the decision boundary
def plot_decision_boundary(model, axis):
    x0, x1 = np.meshgrid(
        np.linspace(axis[0], axis[1], int((axis[1] - axis[0]) * 100)).reshape(-1, 1),
        np.linspace(axis[2], axis[3], int((axis[3] - axis[2]) * 100)).reshape(-1, 1)
    )
    X_new = np.c_[x0.ravel(), x1.ravel()]

    y_predict = model.predict(X_new)
    zz = y_predict.reshape(x0.shape)

    from matplotlib.colors import ListedColormap
    custom_cmap = ListedColormap(['#EF9A9A', '#FFF59D', '#90CAF9'])

    plt.contourf(x0, x1, zz, cmap=custom_cmap)


def main():
    # 1.
    # build data
    data, label = make_blobs(n_samples=1000, n_features=2, centers=2, cluster_std=[2.0, 2.0])

    # 2. draw

    plt.scatter(data[:, 0], data[:, 1], c=label)
    plt.show()

    # set the test and train data and stand the data
    rate_test_of_all = 0.2
    test_sum = int(rate_test_of_all * len(data))
    data_test = data[-test_sum:]
    data_train = data[:-test_sum]
    label_test = label[-test_sum:]
    label_train = label[:-test_sum]
    standardScaler = StandardScaler()
    len_test = int(len(data) * 0.2)
    standardScaler.fit(data_train)
    data_standard = standardScaler.transform(data_train)
    standardScaler.fit(data_test)
    data_test = standardScaler.transform(data_test)
    # Hard Margin SVM : C = 10**9  Soft Margin SVM: C = 0.01
    svc = LinearSVC(C=10 ** 9)
    svc.fit(data_standard, label_train)
    print("The accuracy is:")
    print(accuracy_score(label_test, svc.predict(data_test)))
    plot_decision_boundary(svc, axis=[-3, 3, -3, 3])
    plt.scatter(data_standard[label_train == 0, 0], data_standard[label_train == 0, 1], color='red')
    plt.scatter(data_standard[label_train == 1, 0], data_standard[label_train == 1, 1], color='blue')
    plt.show()


if __name__ == '__main__':
    main()
