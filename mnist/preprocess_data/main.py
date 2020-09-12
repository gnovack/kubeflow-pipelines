import tensorflow as tf
import numpy as np

def load_data():
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
    np.save('x_train.npy', x_train)

print('Loading MNIST data...')
load_data()