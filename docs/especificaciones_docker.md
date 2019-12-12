# Creación del contenedor

Ver [Dockerfile](https://github.com/davidluque1/ProyectoIV/blob/master/Dockerfile)

La línea "FROM  python:3.7-slim-buster" indica que usaremos como imagen base la del usuario python llamada 3.7-slim-buster, una muy ligera con python3.7

La línea "WORKDIR /app" pone el directorio de trabajo en la carpeta /app y hace que comandos como RUN, COPY o CMD se ejecuten desde dicha carpeta

La línea "COPY /flask /flask" copia la carpeta /flask en la carpeta /flask (del contenedor), teniendo en cuenta el comando WORKDIR antes especificado

La línea "COPY requirements.txt ." copia requirements.txt en "." lo cual equivale a copiar requirements.txt en la carpeta especificada en WORKDIR

La línea "RUN pip install --no-cache-dir -r requirements.txt" ejecuta pip install sobre requirements.txt

La línea "EXPOSE 5000" expone el puerto 5000 del contenedor

La línea "CMD gunicorn wsgi:app -b 0.0.0.0:${PORT} --chdir /flask" ejecuta gunicorn para lanzar el servicio web. La opción _--chdir /flask_ le indica que se coloque en la carpeta /flask

Al hacer _docker-build -t proyectoiv ._ construimos el contenedor. Para ejecutarlo, usamos _docker run -p 5000:5000 proyectoiv_. El puerto 5000 del contenedor ha sido expuesto antes y ahora indicamos que las peticiones que lleguen a nuestra máquina al puerto 5000 se redirijan al puerto 5000 del contenedor


# Despliegue en Heroku

Ver [Dockerfile](https://github.com/davidluque1/ProyectoIV/blob/master/heroku.yml)
[Despliegue](https://proyectoivelo-docker.herokuapp.com)

En dicho archivo le indicamos a heroku que tenemos un servicio web que se despliega mediante un contenedor. Al no tener una sección run, ejecuta el comando asociado a "CMD" en el Dockerfile

Los pasos seguidos han sido:

1) Creación del fichero heroku.yml

2) Login en heroku con _heroku login_

3) Creación del repositorio de Heroku con _heroku create_

4) Configurar la imagen como un contenedor con heroku _stack:set container_

5) Hacer push a nuestro repositorio de Heroku con git _push heroku master_

En caso de querer actualizar el repositorio debemos loguearnos y usar el comando _heroku git:remote -a proyectoivelo-docker_ para añadir el repositorio de Heroku como remote


# Despliegue en Azure


[Despliegue](https://http://proyectoivelo.azurewebsites.net)

El despliegue en Azure se ha hecho mediante la interfaz del navegador web. En este caso, al crear la aplicación especificamos simplemente nuestro id de dockerhub y la imagen. Tras crearlo, en sección "atributos" del servicio vemos que es un contenedor obtenido de nuestro dockerhub: 

![Imagen1](https://github.com/davidluque1/RepoPruebas/blob/master/azure_prueba_docker1.png)


# Prueba en local

Para desplegarlo como contenedor en local, simplemente debemos definir la variable PORT. Podemos crear un dockerfile para esto y establecer la variable $PORT ahí o dejar el dockerfile tal y como lo tenemos y definir la variable al ejecutar la orden run: _docker run --env PORT=5000 -p 5000:5000 proyectoiv_



