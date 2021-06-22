FROM python:3.8.5-alpine

RUN pip install --upgrade pip

COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client jpeg-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps \
      gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps


RUN pip install -r requirements.txt

COPY ./app /app

WORKDIR /app


CMD ["gunicorn", "app.wsgi", ":application", "--bind", "0.0.0.0:8081"]

