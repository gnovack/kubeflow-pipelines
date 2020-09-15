FROM python:3.8-slim

WORKDIR /app

RUN pip install -U scikit-learn numpy

COPY train.py ./train.py

ENTRYPOINT [ "python", "train.py" ]