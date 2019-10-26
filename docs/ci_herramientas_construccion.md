## Travis CI

~~~~
language: python
python:  
  - "3.7"
script: make test
~~~~

La documentación de esta parte es sencilla: indicamos python como lenguaje, e indicamos después que la versión a usar es la 3.7. En _script_ le indicamos que debe ejecutar _make test_ (ver más abajo) para que se realicen los tests. No es necesario especificar el comando _pip install -r requirements.txt_ ya que travis lo hace automáticamente.

El fichero _requirements.txt_ indica instalar _Flask_ y _pytest_ en sus versiones correspondientes: 

~~~~
Flask==1.0.2
pytest==5.2.1
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
      - image: circleci/python:3.7

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
~~~~

_version: 2_ nos indica que la versión de circleCI a usar es la 2

_jobs:_ indica los trabajos, en este caso el único es _build:_

_docker:_ nos permite indicar una imagen, en este caso indicamos una con python 3.7

_working_directory:_  directorio de trabajo. En mi caso,  _~/ProyectoIV_

_steps:_ indica una serie de pasos a seguir para dicho trabajo. En nuestro caso, un _checkout_ seguido de dos _run_: el primero consta de una barra (|) que indica que hay varias líneas de comando: _python3 -m venv venv_ crea un entorno virtual con python 3; _. venv/bin/activate_ activa dicho entorno y _pip3 install -r requirements.txt_ instala las herramientas indicadas en _requirements.txt_. El segundo _run_ se encarga de la ejecución de los tests con la orden _make test_.

## Herramienta de construcción

~~~~
clean-pyc:
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*.pyo' -exec rm --force {} +

test: clean-pyc
	py.test
~~~~


Actualmente el _makefile_ sirve para eliminar ficheros residuales de python del tipo _.pyc_ o _.pyo_. La directiva _test_ depende de la directiva _clean-pyc_, con lo cual antes de ejecutar los tests con _py.test_ se hace una limpieza y se eliminan dichos archivos residuales. Al ejecutar _py.test_, se buscan tests en el directorio actual y en sus subdirectorios, ejecutándose. 

En resumen, tanto _travis_ como _circle_ usan _requirements.txt_, del cual obtienen las dependencias, las cuales instalan en entornos virtuales, y luego ejecutan _make test_ para ejecutar los tests.

