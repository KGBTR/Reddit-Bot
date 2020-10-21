FROM python:3.9-alpine as development-stage

WORKDIR /app

RUN apk add --no-cache --update git

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt