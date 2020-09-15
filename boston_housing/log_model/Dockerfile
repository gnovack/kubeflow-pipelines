FROM python:3.7-slim

WORKDIR /app

RUN pip install -U kubeflow-metadata

COPY log_model.py ./log_model.py

ENTRYPOINT [ "python", "log_model.py" ]