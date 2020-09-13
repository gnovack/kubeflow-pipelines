import kfp
from kfp import dsl

def preprocess_op():

    return dsl.ContainerOp(
        name='Preprocess Data',
        image='gnovack/boston_pipeline_preprocessing:latest',
        arguments=[],
        file_outputs={
            'x_train': '/app/x_train.npy',
            'x_test': '/app/x_test.npy',
            'y_train': '/app/y_train.npy',
            'y_test': '/app/y_test.npy',
        }
    )

def train_op(
    x_train,
    y_train
):

    return dsl.ContainerOp(
        name='Train Model',
        image='gnovack/boston_pipeline_train:latest',
        arguments=[
            '--x_train', x_train,
            '--y_train', y_train
        ]
    )

@dsl.pipeline(
   name='Boston Housing Pipeline',
   description='A toy pipeline that performs arithmetic calculations.'
)
def boston_pipeline():
    _preprocess_op = preprocess_op()
    
    train_op(
        dsl.InputArgumentPath(_preprocess_op.outputs['x_train']),
        dsl.InputArgumentPath(_preprocess_op.outputs['y_train'])
    ).after(_preprocess_op)

client = kfp.Client()
client.create_run_from_pipeline_func(boston_pipeline)