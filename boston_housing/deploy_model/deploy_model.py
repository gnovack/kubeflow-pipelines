import argparse

def deploy_model(model_path):
    print(f'deploying model {model_path}...')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--model')
    args = parser.parse_args()
    deploy_model(args.model)