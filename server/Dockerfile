FROM python:3.8-alpine

LABEL maintainer="Vincent Schmid <schmivin@students.zhaw.ch>"

WORKDIR /app
ADD requirements.txt ./
RUN pip install -r requirements.txt
ADD ./main.py ./
CMD python main.py
