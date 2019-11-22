[Desplegado aquí](https://proyectoivelo.herokuapp.com/)

## Script de configuración del PaaS

Antes que nada, para desplegar en Heroku me he creado una cuenta, me he descargado el cinturón de herramientas de Heroku, me he logueado, he creado el repositorio en heroku con heroku create y después he hecho git push heroku master.

Las órdenes deben hacerse desde el directorio principal de nuestro repositorio.

Instalación: _sudo snap install --classic heroku_
Login: _heroku login_
Creación del repositorio: _heroku create proyectoivelo --buildpack heroku/python_
Desplegar: _git push heroku master_


[Procfile](https://github.com/davidluque1/ProyectoIV/blob/master/Procfile)

web: make start-herokucloud

Descripción: Heroku usa esta orden para ejecutar el servicio. La orden ejecutada en el makefile es _gunicorn wsgi:app -b 0000:$(PORT)_. PORT es la variable de entorno que indica el puerto.

## Configuración de GitHub para despliegue continuo

Navegador -> Login en Heroku -> ProyectoIVelo -> Pestaña Deploy -> Enlazamos repositorio de Heroku con el de GitHub -> Activamos los despliegues automáticos, incluida la opción de que espere al CI antes de desplegar

![Imagen1](https://github.com/davidluque1/RepoPruebas/blob/master/Captura%20de%20pantalla%20de%202019-11-22%2016-32-24.png)

## Bibliografía

http://jj.github.io/IV/documentos/proyecto/4.PaaS

https://www.youtube.com/watch?v=pmRT8QQLIqk


