import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np


def one_hot(labels):
    one_hot_labels = np.zeros(shape=[len(labels), 10])
    for i in range(len(labels)):
        index = labels[i]
        one_hot_labels[i][index] = 1
    return one_hot_labels


def cnn_model(input_shape):
    model = tf.keras.Sequential()
    # the first
    model.add(tf.keras.layers.Conv2D(filters=32, kernel_size=5, strides=(1, 1),
                                     padding='same', activation=tf.nn.relu, input_shape=input_shape))

    model.add(tf.keras.layers.MaxPool2D(pool_size=(2, 2), strides=(2, 2), padding='valid'))
    model.add(tf.keras.layers.Conv2D(filters=64, kernel_size=3, strides=(1, 1), padding='same', activation=tf.nn.relu))
    model.add(tf.keras.layers.MaxPool2D(pool_size=(2, 2), strides=(2, 2), padding='valid'))
    model.add(tf.keras.layers.Dropout(0.25))
    model.add(tf.keras.layers.Flatten())

    model.add(tf.keras.layers.Dense(units=128, activation=tf.nn.relu))
    model.add(tf.keras.layers.Dropout(0.5))
    model.add(tf.keras.layers.Dense(units=10, activation=tf.nn.softmax))
    return model


def train_model(train_images, train_labels, test_images, test_labels):
    # resize the images
    train_images = train_images / 255.0
    test_images = test_images / 255.0
    # print images
    train_images = np.expand_dims(train_images, axis=3)
    test_images = np.expand_dims(test_images, axis=3)
    print("train_images :{}".format(train_images.shape))
    print("test_images :{}".format(test_images.shape))

    train_labels = one_hot(train_labels)
    test_labels = one_hot(test_labels)
    # create model
    # using cnn model
    model = cnn_model(input_shape=(28, 28, 1))
    model.compile(metrics=['accuracy'], optimizer="adam", loss="categorical_crossentropy")
    model.fit(x=train_images, y=train_labels, epochs=5)
    test_loss, test_acc = model.evaluate(x=test_images, y=test_labels)
    print("Test Accuracy %.2f" % test_acc)

    # begin to predict
    cnt = 0
    predictions = model.predict(test_images)
    for i in range(len(test_images)):
        target = np.argmax(predictions[i])
        label = np.argmax(test_labels[i])
        if target == label:
            cnt += 1
    print("correct prediction of total : %.2f" % (cnt / len(test_images)))

    # save model
    model.save('mnist-model.h5')


def main():
    # load data from mnist model
    (train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()
    # begin training
    train_model(train_images, train_labels, test_images, test_labels)


if __name__ == '__main__':
    main()
