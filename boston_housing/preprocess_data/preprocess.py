from sklearn import datasets
from sklearn.model_selection import train_test_split
import numpy as np

def _preprocess_data():
     X, y = datasets.load_boston(return_X_y=True)
     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)
     np.save('x_train.npy', X_train)
     np.save('x_test.npy', X_test)
     np.save('y_train.npy', y_train)
     np.save('y_test.npy', y_test)
     
if __name__ == '__main__':
     print('Preprocessing data...')
     _preprocess_data()