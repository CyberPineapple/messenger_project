FROM python:3.7-alpine
WORKDIR /app
COPY ./requirements.txt /
RUN apk add --virtual .build-deps gcc musl-dev postgresql-dev libpq py3-gunicorn
RUN pip install -r /requirements.txt
COPY ./ /app
CMD ["gunicorn", "-c", "settings.ini", "server:main", "--worker-class aiohttp.worker.GunicornWebWork"]

