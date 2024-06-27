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




# # syntax=docker/dockerfile:1
# FROM python:3

# # Environment variables
# ENV PYTHONDONTWRITEBYTECODE=1
# ENV PYTHONUNBUFFERED=1

# # Set working directory
# WORKDIR /code

# # Install PostgreSQL client
# RUN apt-get update && apt-get install -y postgresql-client

# # Copy requirements and install dependencies
# COPY requirements.txt ./
# RUN pip install -r requirements.txt
# RUN pip install python-decouple

# # Copy project files
# COPY ./ ./

# # Expose the port (if not already exposed)
# EXPOSE 8000

# # Command to run the application
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
