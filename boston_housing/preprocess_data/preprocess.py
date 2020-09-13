from sklearn import datasets
import numpy as np

def load_data():
     X, y = datasets.load_boston(return_X_y=True)
     np.save('X.npy', X)

print('Loading data...')
load_data()