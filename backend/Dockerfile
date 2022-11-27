FROM tiangolo/meinheld-gunicorn-flask:python3.9

WORKDIR /app

ENV FLASK_APP app.py

ENV FLASK_RUN_HOST 0.0.0.0

RUN apt-get update && apt-get install -y pandoc

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./src .

EXPOSE 9000
