FROM python:3.11

ENV PYTHONUNBUFFERED=1

ENV PYTHONDONTWRITEBYTECODE=1

RUN mkdir /code \
    /code/tsl_crldownloader \
    /code/tsl_crldownloader/tsl

RUN apt-get update \
    && apt-get install -y cron \
    && apt-get clean

WORKDIR /code

COPY requirements.txt /code/

RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

RUN touch /var/log/django_cron.log  \
    && touch /var/log/cron.log

COPY . /code/

ENTRYPOINT ["sh", "./entrypoint.sh"]

#CMD python manage.py runserver 0.0.0.0:8000
