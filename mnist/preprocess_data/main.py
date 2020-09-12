def load_data():
    #(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
    #np.save('x_train.npy', x_train)
    with open("output.txt", "a") as f:
        f.write('hello world')

print('Loading data...')
load_data()