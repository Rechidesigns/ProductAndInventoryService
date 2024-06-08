# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
#COPY requirements.txt /code/
COPY requirements.txt ./
COPY ./ ./
RUN pip install -r requirements.txt
#COPY . /code/
RUN pip install python-decouple
