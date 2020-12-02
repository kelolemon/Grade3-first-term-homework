import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt


def main():
    line = LinearRegression()
    x = np.loadtxt('x.data')
    x_train = x[:400, 2]
    x_train = np.array(x_train).reshape(-1, 1)
    y_train = x[:400, -1]
    y_train = np.array(y_train).reshape(-1, 1)
    line.fit(x_train, y_train)
    y_pre = line.predict(np.array(x[400:, 2]).reshape(-1, 1))
    print(r2_score(x[400:, -1], y_pre))
    plt.plot(x[400:, -1], label='ture')
    plt.plot(y_pre, label='predict')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
