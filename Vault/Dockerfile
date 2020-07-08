FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV DOCKER 1

# Setup Postgres Devtools
RUN apt-get update
RUN apt-get install -y libpq-dev gcc

# Setup Directory
RUN mkdir /code
WORKDIR /code
RUN mkdir static

# Install Dependencies
COPY requirements-prod.txt /code/
RUN pip install -r requirements-prod.txt

# Copy Entrypoint
COPY entrypoint.sh /code/
