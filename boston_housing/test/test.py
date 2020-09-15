import argparse
import joblib
import numpy as np

def test_model(x_test, y_test, model_path):
    x_test_data = np.load(x_test)
    y_test_data = np.load(y_test)

    model = joblib.load(model_path)
    score = model.score(x_test_data, y_test_data)
    print(score)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--x_test')
    parser.add_argument('--y_test')
    parser.add_argument('--model')
    args = parser.parse_args()
    test_model(args.x_test, args.y_test, args.model_path)