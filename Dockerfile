# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code

# Install PostgreSQL client
RUN apt-get update && apt-get install -y postgresql-client

#COPY requirements.txt /code/
COPY requirements.txt ./
COPY ./ ./
RUN pip install -r requirements.txt
#COPY . /code/
RUN pip install python-decouple

