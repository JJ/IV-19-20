[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![Build Status](https://travis-ci.org/davidluque1/ProyectoIV.svg?branch=master)](https://travis-ci.org/davidluque1/ProyectoIV) [![CircleCI](https://circleci.com/gh/davidluque1/ProyectoIV.svg?style=svg)](https://circleci.com/gh/davidluque1/ProyectoIV.svg?style=svg)

# ProyectoIV

Proyecto para IV para el curso 2019/2020.


## Descripción

El microservicio a desarrollar formaría parte de un proyecto mayor dedicado a la competición en [juegos de suma cero](https://en.wikipedia.org/wiki/Zero-sum_game). Concretamente, este microservicio se encargaría del cálculo del [valor de habilidad](https://en.wikipedia.org/wiki/Elo_rating_system) de los jugadores de la plataforma según sus victorias/derrotas, del cambio al valor de habilidad tras perder/ganar y de la expectativa de un jugador a ganar contra otro. En resumen, de cálculos relacionados con el nivel de habilidad del jugador. Mi idea inicial es usar el modelo de la USCF.

## Funcionalidades

La API implementada permitirá:

· Obtener la expectancia de un jugador A frente a un jugador B

· Obtener el nuevo elo del jugador A tras ganar, perder o empatar una partida contra un jugador B

· Obtener el nº de victorias consecutivas necesarias para que jugador A supere en elo al jugador B (el elo de B desciende, el de A aumenta hasta equilibrarse)

· Obtener el nº de victorias consecutivas necesarias para que un jugador A llegue a un elo B jugando siempre contra jugadores de su mismo elo (que va cambiando)

· Obtener el nº de victorias consecutivas necesarias para que un jugador A llegue a un elo B jugando siempre contra jugadores con elo C

· Obtener el percentil del Elo del jugador A (no implementado todavía)

La implementación de estas historias de usuario se encuentra [aquí](https://github.com/davidluque1/ProyectoIV/blob/master/docs/especificacion_api.md)


## Requisitos

* Python 3.7 

* pip3 (instalado por defecto en Python 3.4 o superior)

* NodeJS. Puede haber problemas si la versión de nodeJS está muy desactualizada

## Instalación

Descargar el repositorio con `git clone`. Situarse en el directorio y ejecutar `make install`. 

## Set-up

Ejecutar `make test` para lanzar todos los tests, `make start` para lanzar el servicio, `make stop` para pararlo, `make restart` para reiniciarlo, `make show` para mostrar información de nuestro proceso y `make delete` para eliminar el servicio de la lista de procesos. En 0.0.0.0:5000 se accederá al servicio.

## Peticiones

Ver la [especificación de la api](https://github.com/davidluque1/ProyectoIV/blob/master/docs/especificacion_api.md)


## Herramienta de construcción
[Archivo Makefile](https://github.com/davidluque1/ProyectoIV/blob/master/Makefile)

> buildtool: Makefile

## Información adicional

· [Entorno de desarrollo](https://github.com/davidluque1/ProyectoIV/blob/master/docs/entorno.md)

· [Integración continua y herramientas de construcción](https://github.com/davidluque1/ProyectoIV/blob/master/docs/ci_herramientas_construccion.md)

· [Especificaciones matemáticas](https://github.com/davidluque1/ProyectoIV/blob/master/docs/especificaciones_matematicas.md)

· [Especificación API](https://github.com/davidluque1/ProyectoIV/blob/master/docs/especificacion_api.md)

· [Especificación de la clase](https://github.com/davidluque1/ProyectoIV/blob/master/docs/especificaciones_clase.md)

· [Especificación de los tests](https://github.com/davidluque1/ProyectoIV/blob/master/docs/especificaciones_tests.md)




