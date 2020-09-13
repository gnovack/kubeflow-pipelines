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
    x_test,
    y_train,
    y_test
):

    return dsl.ContainerOp(
        name='Train Model',
        image='gnovack/boston_pipeline_train:latest',
        arguments=[
            '--x_train', x_train,
            '--x_test', x_test,
            '--y_train', y_train,
            '--y_train', y_test
        ]
    )

@dsl.pipeline(
   name='Boston Housing Pipeline',
   description='A toy pipeline that performs arithmetic calculations.'
)
def boston_pipeline():
    preprocess_task = preprocess_op()
    
    train_op(
        dsl.InputArgumentPath(preprocess_task.outputs['x_train']),
        dsl.InputArgumentPath(preprocess_task.outputs['x_test']),
        dsl.InputArgumentPath(preprocess_task.outputs['y_train']),
        dsl.InputArgumentPath(preprocess_task.outputs['y_test'])
    ).after(preprocess_task)

client = kfp.Client()
#Specify pipeline argument values
arguments = {} 
#Submit a pipeline run
client.create_run_from_pipeline_func(boston_pipeline, arguments=arguments)