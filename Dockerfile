FROM python:3.9-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/web

COPY requirements.txt .
COPY entrypoint.sh .

RUN apk --update add
RUN apk add gcc libc-dev libffi-dev jpeg-dev zlib-dev libjpeg libwebp-dev
RUN apk add postgresql-dev

RUN pip install --upgrade pip
RUN pip install psycopg2-binary
RUN pip install -r requirements.txt
RUN pip install -vvv django-recaptcha3
RUN pip install django-recaptcha3 --upgrade


RUN chmod +x entrypoint.sh

COPY . .

ENTRYPOINT ["sh", "/usr/src/web/entrypoint.sh"]
