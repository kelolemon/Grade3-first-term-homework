import tensorflow as tf
import numpy as np


def one_hot(labels):
    one_hot_labels = np.zeros(shape=[len(labels), 10])
    for i in range(len(labels)):
        index = labels[i]
        one_hot_labels[i][index] = 1
    return one_hot_labels


def cnn_model(input_shape):
    model = tf.keras.Sequential()
    # the first Convolutional layer and pooling layer
    # kernel size is defined classically 5 * 5, strides is 1 and using the relu algorithm, using 0 to pade the margin.
    # the input shape is (image_height, image_width, color_channels), the pictures is black and white,
    # so the color_channels is 1, the image height and width is output by former initialize we can discover that is
    # 28 * 28, so the input shape is (28, 28, 1)
    # filters is 32 means that there are 32 kernels and the output depths are 32.
    # using classical 2 * 2 pool size pooling layer
    # after these two layers, the output is (14, 14, 32)
    model.add(tf.keras.layers.Conv2D(filters=16, kernel_size=5, strides=(1, 1),
                                     padding='same', activation=tf.nn.relu, input_shape=input_shape))
    model.add(tf.keras.layers.MaxPool2D(pool_size=(2, 2), strides=(2, 2), padding='valid'))
    # the second Convolutional layer and pooling layer
    # kernel size is defined classically 3 * 3, strides is 1 and using the relu algorithm, using 0 to pade the margin.
    # the input shape is 14 * 14 * 32
    # filters is 64 means that there are 64 kernels and the output depths are 64.
    # using classical 2 * 2 pool size pooling layer
    # after these two layers, the output is (7， 7， 64)
    model.add(tf.keras.layers.Conv2D(filters=32, kernel_size=3, strides=(1, 1), padding='same', activation=tf.nn.relu))
    model.add(tf.keras.layers.MaxPool2D(pool_size=(2, 2), strides=(2, 2), padding='valid'))
    # using dropout layer to allow mistakes and predict over fit
    # model.add(tf.keras.layers.Dropout(0.25))
    # using flatten layer to make multi dimensions data to one dimension data.
    # this layer is to make preparation for the later full connecting layers
    # after this layer the output is (7 * 7 * 64) equals (3136)
    model.add(tf.keras.layers.Flatten())
    # the first full-connecting layer, input is 3136, output is 128
    model.add(tf.keras.layers.Dense(units=128, activation=tf.nn.relu))
    # using dropout layer to allow mistakes and predict over fit
    # model.add(tf.keras.layers.Dropout(0.5))
    # the second full-connecting layer, input is 128, output is 10
    # the output is 10. the reason is that the answer is between 0 and 9.
    model.add(tf.keras.layers.Dense(units=10, activation=tf.nn.softmax))
    # return the model
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
    print(model.summary())
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


def main():
    # load data from mnist model
    (train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()
    # begin training
    train_model(train_images, train_labels, test_images, test_labels)


if __name__ == '__main__':
    main()
