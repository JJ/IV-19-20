FROM  python:3.7-slim-buster

WORKDIR /app

COPY /flask /flask

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD gunicorn wsgi:app -b 0.0.0.0:${PORT} --chdir /flask
