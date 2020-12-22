FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8-alpine3.10-2020-12-19

LABEL maintainer="Vincent Schmid <schmivin@students.zhaw.ch>"

WORKDIR /app
ADD requirements.txt ./
RUN pip install -r requirements.txt
ADD ./main.py ./
