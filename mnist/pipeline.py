import kfp
from kfp import dsl

from preprocess_data.component import preprocess_op

@dsl.pipeline(
   name='MNIST Pipeline',
   description='A toy pipeline that performs arithmetic calculations.'
)
def mnist_pipeline():
    step = preprocess_op()

client = kfp.Client()
#Specify pipeline argument values
arguments = {} 
#Submit a pipeline run
client.create_run_from_pipeline_func(mnist_pipeline, arguments=arguments)