import argparse
import numpy as np
from sklean.linear_model import SGDRegressor

def train_model(x_train, y_train):
    x_train_data = np.load(x_train)
    y_train_data = np.load(y_train)

    model = SGDRegressor()
    model.fit(x_train_data, y_train_data)
    print(model.coef_)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--x_train')
    parser.add_argument('--y_train')
    args = parser.parse_args()
    train_model(args.x_train, args.y_train)