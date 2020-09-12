FROM python:3.8-slim

WORKDIR /app

RUN pip install -U scikit-learn numpy

COPY main.py ./main.py

ENTRYPOINT [ "python", "main.py" ]