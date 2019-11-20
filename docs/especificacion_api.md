## Especificación de la API

La api actualmente devuelve la expectancia de un jugador frente a otro, y el nuevo ELO tras una victoria, derrota o empate.

URI

| URI | Método | Parámetros | Respuesta | Datos adicionales |
|:-:|:-:|:-:|:-:|:-:|
|/ |  GET | |json: {'status: OK'} | | 
|/status |  GET | | json: {'status: OK'} | |
|/Expectancia | GET | elojug1, elojug2 |json: {'expectancia'="..."} | La expectancia es la del jugador primero (jug1) |
|/NuevoElo | GET | elojug1, elojug2, k, resultado |json: {'nuevoElo'="..."} | k es un factor que va de 10 a 40; resultado es 0, 0.5 o 1 (perder, empatar, ganar) |
|/PartidasSuperarJugador| GET | elojug1, elojug2| json: {'partidasSuperarJugador'="..."} | |
|/PartidasSuperarElo | GET | elojug1, elojug2 | | json: {'partidasSuperarElo'="..."} |
|/PartidasSuperarEloEst | GET | elojug1, elojug2, elojug3 | json: {'partidasSuperarEloEst'="..."} | |

## Cómo se levanta el servicio

Dos ficheros a comentar:

[wsgi.py](https://github.com/davidluque1/ProyectoIV/blob/master/flask/wsgi.py) -> importa el objeto Flask definido en servicio.py y lo define para que se ejecute en caso de ser wsgi.py el archivo principal

[startsite.sh](https://github.com/davidluque1/ProyectoIV/blob/master/startsite.sh) -> se cambia a la carpeta flask y ejecuta el comando gunicorn --bind 0.0.0.0:5000 wsgi:app -w 10. wsgi se refiere al fichero a ejecutar (wsgi.py) y app al objeto (app). -w 10 simboliza 10 trabajadores

## Sobre las rutas servidas

Las rutas se sirven fácilmente gracias a Flask definiendo métodos asociados a ellas. Para devolver el objeto como json se utiliza json.dumps y Response para que el mimetype sea 'application/json'. Ver [servicio.py](https://github.com/davidluque1/ProyectoIV/blob/master/flask/servicio.py)

## Sobre la importación de las clases en los ficheros test 

Decidí separar los test del código fuente. Para importar las clases almacenadas en la carpeta "Flask" desde la carpeta "Test" (ambas al mismo nivel sobre la carpeta padre ProyectoIV) me hicieron falta estas líneas de código:

```python
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
dirFlask = parentdir+"/flask"
sys.path.insert(0,dirFlask)
```

las cuales indican a Python que al hacer imports busque también en la carpeta flask. 
Ver [test_Jugador.py](https://github.com/davidluque1/ProyectoIV/blob/master/tests/test_Jugador.py)
