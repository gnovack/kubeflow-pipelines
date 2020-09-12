from kfp import dsl
def preprocess_op():

    return dsl.ContainerOp(
        name='Preprocess Data',
        image='gnovack/mnist_pipeline_preprocessing:latest',
        arguments=[],
        file_outputs={
            'x_train': 'x_train.npy',
        }
    )