from kfp import dsl
def preprocess_op():

    return dsl.ContainerOp(
        name='Preprocess Data',
        image='mnist-pipeline/preprocess_data:latest',
        arguments=[],
        file_outputs={
            'x_train': '/x_train.npy',
        }
    )