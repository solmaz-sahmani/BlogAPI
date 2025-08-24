FROM python:3.11-slim

RUN mkdir /app

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE =1
ENV PYTHONUNBUFFERED =1

RUN apt-get update && apt-get install -y gcc libpq-dev

COPY requirements.txt /app/requirements.txt

RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /app