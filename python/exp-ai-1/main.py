from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pandas as pd


def linear_regression(x_train, x_predict, y_train, y_predict):
    line = LinearRegression()
    line.fit(x_train, y_train)
    # using model to predict
    y_pre = line.predict(x_predict)
    # judge the scores of model predict using R^2
    print(line.score(x_train, y_train))
    # draw the picture
    plt.subplot(211)
    plt.plot(y_predict, label='true')
    plt.plot(y_pre, label='predict')
    plt.subplot(212)
    plt.scatter(x_train, y_train, color="red")
    plt.plot(x_train, line.predict(x_train), color="blue")
    plt.show()


def main():
    # read the data
    data_set = pd.read_table('diabetes.tab.txt')
    # get x data
    x_set = data_set['BMI']
    # get y data
    y_set = data_set['Y']
    # split the training set and predict set
    x_train, x_predict, y_train, y_predict = train_test_split(x_set.values, y_set.values, test_size=1/10, random_state=0)
    x_train = x_train.reshape(-1, 1)
    x_predict = x_predict.reshape(-1, 1)
    # using linear regression model
    linear_regression(x_train, x_predict, y_train, y_predict)


if __name__ == '__main__':
    main()
