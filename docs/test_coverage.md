## Test Coverage
Realizado por Jesús Rodríguez Pérez

Para mejorar la calidad de los tests dentro de este proyecto, he pensado adecuado añadir un test coverage para poder observar el buen funcionamiento de los tests.

Para la cobertura se ha utilizado el plugin [pytest-cov](https://pytest-cov.readthedocs.io/en/latest/), para ello se ha tenido que añadir en el requirements (para que sea instalado) y se ha añadido en el makefile lo siguiente:

```yaml
coverage: #Cobertura
	pytest --cov-report html:coverage --cov=./ tests/
```

Definimos una regla llamada "coverage" en el makefile, que lo que hace es ejecutar los tests y calcular la cobertura, el resultado es escrito en el directorio /coverage, para visualizarlo a partir del archivo html /coverage/index.html (situado en el directorio raíz de este proyecto).

Para calcular la cobertura basta con "make coverage"

## Añado test

Los resultados sobre las clases relevantes son los siguientes:

```yaml
flask/Jugador.py 	35 	23 	0 	34%

flask/servicio.py 	33 	3 	0 	91%
```

Gracias, a pytest-cov podemos ver que funciones son las que se ejecutan y cuales no, en este caso en Jugador.py (coverage del 34%) falta por testear getPercentil (y alguna otra función como un constructor sin parámetros). 

Por el motivo anterior he decidido añadir un test ( de getPercentil() ) para ampliar la cobertura de los tests:

```yaml
def test_percentil():
    Jugador1= Jugador(2000)
    Jugador2 = Jugador(2800)
    Jugador3 = Jugador(2700)

    
    var1 = Jugador1.getPercentil()
    var2 = Jugador2.getPercentil()
    var3 = Jugador3.getPercentil()

    
    assert var1 == 0.9462 and var2 == 1 and var3 == 0.9998, "Fallo en calculo de percentil"

    return 0
```

Lo que hace el anterior test es comprobar que funciona correctamente gerPercentil() (clase Jugador.py)

Ahora comprobamos la nueva cobertura de los tests tras añadir esto:

```yaml
flask/Jugador.py 	35 	11 	0 	69%
flask/servicio.py 	33 	3 	0 	91%
```

Ha subido del 34% al 69%





 
