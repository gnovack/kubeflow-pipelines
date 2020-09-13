import kfp
from kfp import dsl

def preprocess_op():

    return dsl.ContainerOp(
        name='Preprocess Data',
        image='gnovack/boston_pipeline_preprocessing:latest',
        arguments=[],
        file_outputs={
            'x_train': '/app/X.npy',
        }
    )

def train_op(x_train):

    return dsl.ContainerOp(
        name='Train Model',
        image='gnovack/boston_pipeline_train:latest',
        arguments=[
            '--x_train', x_train
        ]
    )

@dsl.pipeline(
   name='Boston Housing Pipeline',
   description='A toy pipeline that performs arithmetic calculations.'
)
def boston_pipeline():
    preprocess_task = preprocess_op()
    train_op(preprocess_task.outputs['x_train']).after(preprocess_task)

client = kfp.Client()
#Specify pipeline argument values
arguments = {} 
#Submit a pipeline run
client.create_run_from_pipeline_func(boston_pipeline, arguments=arguments)