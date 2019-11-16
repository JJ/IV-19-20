##Test Coverage
Realizado por Jesús Rodríguez Pérez

Para mejorar la calidad de los tests dentro de este proyecto, he pensado adecuado añadir un test coverage para poder observar el buen funcionamiento de los tests.

Para la cobertura se ha utilizado el plugin [pytest-cov](https://pytest-cov.readthedocs.io/en/latest/), para ello se ha tenido que añadir en el requirements (para que sea instalado) y se ha añadido en el makefile lo siguiente:

```yaml
coverage: #Cobertura
	pytest --cov-report html:coverage --cov=./ tests/
```

Definimos una regla llamada "coverage" en el makefile, que lo que hace es ejecutar los tests y calcular la cobertura, el resultado es escrito en el directorio /coverage, para visualizarlo basta con ver el archivo /coverage/index.html (situado en el directorio raíz de este proyecto).

##Añado test

Los resultados sobre las clases relevantes son los siguientes:

flask/Jugador.py 	35 	23 	0 	34%
flask/servicio.py 	33 	3 	0 	91%

Gracias, a pytest-cov podemos ver que funciones son las que se ejecutan y cuales no, en este caso en Jugador.py (coverage del 34%) falta por testear getPercentil (y alguna otra función como un constructor sin parámetros). 

Por el motivo anterior he decidido añadir un test ( de getPercentil() ) para ampliar la cobertura de los tests:



 
