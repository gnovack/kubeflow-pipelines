import argparse, datetime
from kubeflow.metadata import metadata

METADATA_STORE_HOST = "metadata-grpc-service.kubeflow" # default DNS of Kubeflow Metadata gRPC serivce.
METADATA_STORE_PORT = 8080

def log_model(model_path):

    workspace = metadata.Workspace(
        store=metadata.Store(grpc_host=METADATA_STORE_HOST, grpc_port=METADATA_STORE_PORT),
        name="my_workspace",
        description="my development workspace"
    )
    
    run = metadata.Run(
        workspace=workspace,
        name="run-" + datetime.utcnow().isoformat("T"),
        description="a run in my workspace",
    )

    execution = metadata.Execution(
        name = "execution" + datetime.utcnow().isoformat("T") ,
        workspace=workspace,
        run=run,
        description="execution",
    )

    exec.log_output(
        metadata.Model(
            name="Boston_Housing",
            description="model used to predict median home value",
            uri=model_path,
            model_type="SGD Regressor",
            hyperparameters={
                "learning_rate": 0.5,
                "layers": [10, 3, 1],
                "early_stop": True
            },
            version='v1'
        )
    )

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--model')
    args = parser.parse_args()
    log_model(args.model)