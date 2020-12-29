from sklearn.linear_model import LinearRegression
from sklearn.linear_model import logistic
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import pandas as pd


def main():
    data_set = pd.read_table('quake.dat', header=None, sep=',', comment='@')
    x_1_set = data_set[2]
    x_1_set = x_1_set.values
    y_set = data_set[3]
    y_set = y_set.values
    line = LinearRegression()
    line.fit(x_1_set[:2100].reshape(-1, 1), y_set[:2100])
    y_pre = line.predict(x_1_set[2100:].reshape(-1, 1))
    plt.plot(y_pre, color='red')
    plt.plot(y_set[2100:], color='blue')
    print(line.score(x_1_set[:2100].reshape(-1, 1), y_set[:2100]))
    plt.show()


if __name__ == '__main__':
    main()
