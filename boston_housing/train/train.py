import argparse

def train_model(x_train):
    print(x_train)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--x_train')
    args = parser.parse_args()
    train_model(args.x_train)