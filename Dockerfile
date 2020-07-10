FROM python:3.7-alpine
MAINTAINER Shreeda Bhat M 


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0


COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app


RUN adduser -D user
USER user

CMD gunicorn app.wsgi:application --bind 0.0.0.0:$PORT
