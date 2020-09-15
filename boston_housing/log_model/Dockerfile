FROM python:3.8-slim

WORKDIR /app

RUN pip install -U kubeflow-metadata

COPY log_model.py ./log_model.py

ENTRYPOINT [ "log_model", "log_model.py" ]