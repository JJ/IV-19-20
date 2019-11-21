cd flask
gunicorn wsgi:app -b 0000:5000 -w 10


