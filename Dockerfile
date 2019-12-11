FROM  python:3.7-slim-stretch

WORKDIR /app

COPY /flask /flask

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD gunicorn flask/wsgi:app -b 0000:${PORT}
