import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import numpy as np

mnist = keras.datasets.mnist


def get_train_val(mnist_path):
    # mnist下载地址：https://storage.googleapis.com/tensorflow/tf-keras-datasets/mnist.npz
    (train_images, train_labels), (test_images, test_labels) = mnist.load_data(mnist_path)
    print("train_images nums:{}".format(len(train_images)))
    print("test_images nums:{}".format(len(test_images)))
    return train_images, train_labels, test_images, test_labels


def show_mnist(images, labels):
    for i in range(25):
        plt.subplot(5, 5, i + 1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        plt.imshow(images[i], cmap=plt.cm.gray)
        plt.xlabel(str(labels[i]))
    plt.show()


def one_hot(labels):
    onehot_labels = np.zeros(shape=[len(labels), 10])
    for i in range(len(labels)):
        index = labels[i]
        onehot_labels[i][index] = 1
    return onehot_labels


def mnist_net(input_shape):
    '''
    构建一个简单的全连接层网络模型：
    输入层为28x28=784个输入节点
    隐藏层120个节点
    输出层10个节点
    :param input_shape: 指定输入维度
    :return:
    '''

    model = keras.Sequential()
    model.add(keras.layers.Flatten(input_shape=input_shape))  # 输出层
    model.add(keras.layers.Dense(units=120, activation=tf.nn.relu))  # 隐含层
    model.add(keras.layers.Dense(units=10, activation=tf.nn.softmax))  # 输出层
    return model


def mnist_cnn(input_shape):
    '''
    构建一个CNN网络模型
    :param input_shape: 指定输入维度
    :return:
    '''
    model = keras.Sequential()
    model.add(keras.layers.Conv2D(filters=32, kernel_size=5, strides=(1, 1),
                                  padding='same', activation=tf.nn.relu, input_shape=input_shape))
    model.add(keras.layers.MaxPool2D(pool_size=(2, 2), strides=(2, 2), padding='valid'))
    model.add(keras.layers.Conv2D(filters=64, kernel_size=3, strides=(1, 1), padding='same', activation=tf.nn.relu))
    model.add(keras.layers.MaxPool2D(pool_size=(2, 2), strides=(2, 2), padding='valid'))
    model.add(keras.layers.Dropout(0.25))
    model.add(keras.layers.Flatten())
    model.add(keras.layers.Dense(units=128, activation=tf.nn.relu))
    model.add(keras.layers.Dropout(0.5))
    model.add(keras.layers.Dense(units=10, activation=tf.nn.softmax))
    return model


def trian_model(train_images, train_labels, test_images, test_labels):
    # re-scale to 0~1.0之间
    train_images = train_images / 255.0
    test_images = test_images / 255.0
    # mnist数据转换为四维
    train_images = np.expand_dims(train_images, axis=3)
    test_images = np.expand_dims(test_images, axis=3)
    print("train_images :{}".format(train_images.shape))
    print("test_images :{}".format(test_images.shape))

    train_labels = one_hot(train_labels)
    test_labels = one_hot(test_labels)

    # 建立模型
    # model = mnist_net(input_shape=(28,28))
    model = mnist_cnn(input_shape=(28, 28, 1))
    model.compile(optimizer=tf.train.AdamOptimizer(), loss="categorical_crossentropy", metrics=['accuracy'])
    model.fit(x=train_images, y=train_labels, epochs=5)

    test_loss, test_acc = model.evaluate(x=test_images, y=test_labels)
    print("Test Accuracy %.2f" % test_acc)

    # 开始预测
    cnt = 0
    predictions = model.predict(test_images)
    for i in range(len(test_images)):
        target = np.argmax(predictions[i])
        label = np.argmax(test_labels[i])
        if target == label:
            cnt += 1
    print("correct prediction of total : %.2f" % (cnt / len(test_images)))

    model.save('mnist-model.h5')


if __name__ == "__main__":
    mnist_path = 'D:/MyGit/tensorflow-yolov3/data/mnist.npz'
    train_images, train_labels, test_images, test_labels = get_train_val(mnist_path)
    # show_mnist(train_images, train_labels)
    trian_model(train_images, train_labels, test_images, test_labels)