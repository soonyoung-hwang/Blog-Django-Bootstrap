# pull official base image
FROM python:3.11-slim

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /usr/src/app/
# install dependencies
RUN pip install pipenv==2023.9.1
RUN pipenv install --system --deploy --ignore-pipfile

