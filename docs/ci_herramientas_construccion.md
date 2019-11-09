## Travis CI

~~~~
language: python
python:  
  - "3.7"
install:
  - make install 

script:
  - make test	
  - make start
  - make show
  - make restart
  - make stop

~~~~

La documentación de esta parte es sencilla: indicamos python como lenguaje, e indicamos después que la versión a usar es la 3.7. En _script_ le indicamos que debe ejecutar _make test_ (ver más abajo) para que se realicen los tests. No es necesario especificar el comando _pip install -r requirements.txt_ ya que travis lo hace automáticamente.

El fichero _requirements.txt_ indica instalar _Flask_, _pytest_ y _gunicorn_ en sus versiones correspondientes: 

~~~~
Flask==1.0.2
pytest==5.2.1
gunicorn==19.5.0
~~~~


## CircleCI

~~~~
# Python CircleCI 2.0 configuration file
#
# Check https://circleci.com/docs/2.0/language-python/ for more details
#
version: 2
jobs:
  build:
    docker:
      # imagen base de docker a usar, python 3.7
      - image: nikolaik/python-nodejs:latest

    working_directory: ~/ProyectoIV

    steps:
      - checkout

      - run:
          name: Install dependencies
          command: |
            python3 -m venv venv
            . venv/bin/activate
            pip3 install -r requirements.txt


      # ejecutar tests
      - run:
          name: Run tests
          command: |
            . venv/bin/activate
            make test

      - run:
          name: Run service
          command: |
            . venv/bin/activate
            make start
            make show
            make restart
            make stop
~~~~

_version: 2_ nos indica que la versión de circleCI a usar es la 2

_jobs:_ indica los trabajos, en este caso el único es _build:_

_docker:_ nos permite indicar una imagen, en este caso indicamos una con python 3.7

_working_directory:_  directorio de trabajo. En mi caso,  _~/ProyectoIV_

_steps:_ indica una serie de pasos a seguir para dicho trabajo. En nuestro caso, un _checkout_ seguido de tres _run_: el primero consta de una barra (|) que indica que hay varias líneas de comando: _python3 -m venv venv_ crea un entorno virtual con python 3; _. venv/bin/activate_ activa dicho entorno y _pip3 install -r requirements.txt_ instala las herramientas indicadas en _requirements.txt_. El segundo _run_ se encarga de la ejecución de los tests con la orden _make test_. El tercer run activa el servicio, muestra que está activo, lo reinicia y finalmente lo para.

He tenido que cambiar la imagen del contenedor a una que además de python tuviera nodeJS y que tuviera npm para poder instalar pm2. La imagen es nikolaik/python-nodejs:latest

## Herramienta de construcción

~~~~
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
~~~~


Actualmente el _makefile_ sirve para eliminar ficheros residuales de python del tipo _.pyc_ o _.pyo_. La directiva _test_ depende de la directiva _clean-pyc_, con lo cual antes de ejecutar los tests con _py.test_ se hace una limpieza y se eliminan dichos archivos residuales. Al ejecutar _py.test_, se buscan tests en el directorio actual y en sus subdirectorios, ejecutándose. También lo he usado para instalar las dependencias necesarias y para crear diferentes secciones de tests (clases/api, o todo) y para arrancar o parar el servicio y otras opciones de pm2. La directiva --name simplemente le asigna un nombre al trabajo con el que es más fácil trabajar. La directiva .ONESHELL hace que todo se ejecute en una misma shell. 

En resumen, tanto _travis_ como _circle_ usan _requirements.txt_, del cual obtienen las dependencias, las cuales instalan en entornos virtuales, y luego ejecutan _make test_ para ejecutar los tests.

