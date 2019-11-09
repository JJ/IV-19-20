[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![Build Status](https://travis-ci.org/davidluque1/ProyectoIV.svg?branch=master)](https://travis-ci.org/davidluque1/ProyectoIV) [![CircleCI](https://circleci.com/gh/davidluque1/ProyectoIV.svg?style=svg)](https://circleci.com/gh/davidluque1/ProyectoIV.svg?style=svg)

# ProyectoIV

Proyecto para IV para el curso 2019/2020.


## Descripción

El microservicio a desarrollar formaría parte de un proyecto mayor dedicado a la competición en [juegos de suma cero](https://en.wikipedia.org/wiki/Zero-sum_game). Concretamente, este microservicio se encargaría del cálculo del [valor de habilidad](https://en.wikipedia.org/wiki/Elo_rating_system) de los jugadores de la plataforma según sus victorias/derrotas, del cambio al valor de habilidad tras perder/ganar y de la expectativa de un jugador a ganar contra otro. En resumen, de cálculos relacionados con el nivel de habilidad del jugador. Mi idea inicial es usar el modelo de la USCF.


## Prerequisitos

· Python 3.7 

· pip (instalado por defecto en Python 3.4 o superior)


## Instalación

Descargar el repositorio con `git clone`. Situarse en el directorio y ejecutar `make install`. Ejecutar `make tests` para lanzar todos los tests, `make start` para lanzar el servicio, `make stop` para pararlo, `make restart` para reiniciarlo, `make show` para mostrar información de nuestro proceso y `make delete` para eliminar el servicio de la lista de procesos.

## Herramienta de construcción
> buildtool: Makefile

## Información adicional

· [Entorno de desarrollo](https://github.com/davidluque1/ProyectoIV/blob/master/docs/entorno.md)

· [Integración continua y herramientas de construcción](https://github.com/davidluque1/ProyectoIV/blob/master/docs/ci_herramientas_construccion.md)

· [Especificaciones matemáticas](https://github.com/davidluque1/ProyectoIV/blob/master/docs/especificaciones_matematicas.md)





