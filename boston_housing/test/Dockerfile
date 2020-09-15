FROM python:3.8-slim

WORKDIR /app

RUN pip install -U scikit-learn numpy

COPY test.py ./test.py

ENTRYPOINT [ "python", "test.py" ]