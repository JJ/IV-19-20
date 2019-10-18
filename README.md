[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![Build Status](https://travis-ci.org/davidluque1/ProyectoIV.svg?branch=master)](https://travis-ci.org/davidluque1/ProyectoIV)

# ProyectoIV

Proyecto para IV para el curso 2019/2020.


## Descripción

El microservicio a desarrollar formaría parte de un proyecto mayor dedicado a la competición en [juegos de suma cero](https://en.wikipedia.org/wiki/Zero-sum_game). Concretamente, este microservicio se encargaría del cálculo del [valor de habilidad](https://en.wikipedia.org/wiki/Elo_rating_system) de los jugadores de la plataforma según sus victorias/derrotas, del cambio al valor de habilidad tras perder/ganar y de la expectativa de un jugador a ganar contra otro. En resumen, de cálculos relacionados con el nivel de habilidad del jugador. Mi idea inicial es usar el modelo de la USCF.




## Desarrollo del proyecto

### Herramientas


· **Lenguaje**: [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) será el lenguaje a usar gracias a su versatilidad, sintaxis cómoda y librería estándar muy amplia.

· **Framework**: [Flask](https://en.wikipedia.org/wiki/Flask_(web_framework)) ha sido el framework elegido ya que parece ser beginner-friendly, especialmente para el desarrollo de un microservicio relativamente simple.

· **Entorno virtual**: [virtualenv](https://virtualenv.pypa.io/en/latest/) nos permitirá resolver posibles problemas de dependencias de nuestra aplicación y crear entornos virtuales aislados.

· **Base de datos**: [MariaDB](https://mariadb.org/) se usará como base de datos.

· **Sistema de logging**: [Logging](https://realpython.com/python-logging/#the-logging-module), el módulo para logs por defecto en Python. Nos ofrece diferentes niveles dependiendo de la relevancia del evento, así como diferentes clases como Logger, Handler y Formatter para manejar logs y acciones relacionadas con ellos.

· **Framework para testeo**: [pytest](https://docs.pytest.org/en/latest/) me ha parecido tener bastante documentación además de ser muy usado.

· **Integración continua**: [Travis CI](https://travis-ci.org/) 

