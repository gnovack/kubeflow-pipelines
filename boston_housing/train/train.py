import argparse
import numpy as np

def train_model(x_train):
    x_train_data = np.load(x_train)
    print(x_train_data)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--x_train')
    args = parser.parse_args()
    train_model(args.x_train)