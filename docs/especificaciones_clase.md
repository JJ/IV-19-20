# Especificaciones de la clase

## Atributos

 - nombre: nombre del jugador

 - elo: puntuación elo

 - k: factor k del jugador

## Métodos

 - getExpectancia(self, eloB): Devuelve la expectancia del jugador de la clase contra un jugador con eloB
 
 - getNuevoElo(self, eloB, resultado): Devuelve el nuevo elo del jugador de la clase tras una partida contra un jugador con elo B y un resultado (1 es ganar, 0.5 tablas, 0 perder)

 - getPercentil(): Devuelve el percentil de la puntuación ELO del jugador

[Clase Jugador](https://github.com/davidluque1/ProyectoIV/blob/master/flask/Jugador.py)
