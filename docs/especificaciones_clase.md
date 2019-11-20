# Especificaciones de la clase

## Atributos

 - nombre: nombre del jugador

 - elo: puntuación elo

 - k: factor k del jugador

## Métodos

 - getExpectancia(self, eloB): Devuelve la expectancia del jugador de la clase contra un jugador con eloB
 
 - getNuevoElo(self, eloB, resultado): Devuelve el nuevo elo del jugador de la clase tras una partida contra un jugador con elo B y un resultado (1 es ganar, 0.5 tablas, 0 perder)

 - getPercentil(): Devuelve el percentil de la puntuación ELO del jugador

 - getPartidasSuperarJugador(self, eloB): Calcula el nº de partidas ganadas consecutivas necesarias para que el jugador de la clase alcance en ELO a un jugador con eloB, teniendo en cuenta que en cada partida el jugador con eloB va a ir perdiendo ELO

 - getPartidasSuperarElo(self, eloObjetivo): Calcula el nº de partidas ganadas consecutivas necesarias para que el jugador de la clase alcance eloObjetivo. En cada partida, el jugador se enfrenta a jugadores con su mismo ELO. Por ejemplo primero sube a 1500 y se enfrenta con uno de 1500, luego sube a 1550 y se enfrenta con uno de 1550, etc.

 - getPartidasSuperarEloEst(self, eloObjetivo, eloOponentes): Calcula el nº de partidas ganadas consecutivas necesarias para que el jugador de la clase alcance eloObjetivo. En todas las partidas el jugador se enfrenta siempre a jugadores con un elo eloOponentes, independientemente de cuál sea su elo.

[Clase Jugador](https://github.com/davidluque1/ProyectoIV/blob/master/flask/Jugador.py)
