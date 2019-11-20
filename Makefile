clean-pyc: # limpiado de ficheros basura de python
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*.pyo' -exec rm --force {} +

.ONESHELL:

install: # -g para global en npm. pm2 es nuestro gestor de procesos.
	npm install -g pm2
	pip3 install -r requirements.txt

test_jugador: # testear sólo la clase jugador
	pytest tests/Jugador.py

test_api: # testear la API
	pytest tests/test_Api.py

test: # testear todo
	pytest

start: # inicio del servicio. Ver contenido de startsite.sh para ver la orden específica de gunicorn
	pm2 start startsite.sh --name "servicio"

stop: # parar servicio
	pm2 stop servicio

restart: # reiniciar servicio
	pm2 restart servicio

show: # mostrar servicio
	pm2 show servicio

delete: # borrar el servicio
	pm2 delete servicio

coverage: #Cobertura
	pytest --cov-report html:coverage --cov=./ tests/
