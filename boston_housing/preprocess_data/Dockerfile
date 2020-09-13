FROM python:3.8-slim

WORKDIR /app

RUN pip install -U scikit-learn numpy

COPY preprocess.py ./preprocess.py

ENTRYPOINT [ "python", "preprocess.py" ]