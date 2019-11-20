# Tests de la clase

Los archivos con tests se encuentran en la carpeta "test". 

test_Jugador.py es el archivo donde se testea la clase. En este archivo:

* test_Expectancia(): Testea que la expectancia se calcule bien

* test_NuevoElo(): Testea que el nuevo ELO tras ganar/perder/empatar se calcule bien

* test_Percentil(): Testea que un par de percentiles sean los correctos

* test_PartidasSuperarJugador(): Testea que el nº de partidas a ganar de jugA a jugB hasta equilibrarse los ELOs se calcule bien y sea correcto

* test_PartidasSuperarElo(): Testea que el nº de partidas a ganar de jugA contra jugadores de su mismo nivel hasta llegar al elo de jugB sea el correcto

* test_PartidasSuperarEloEst(): Testea que el nº de partidas a ganar de JugA contra un jugador JugB hasta llegar al elo del jugador JugC (el elo de JugB no cambia)

# Test de la API

* test_status(): Testea que el status se devuelva bien y sea el correcto

* test_api_Expectancia(): Testea que la respuesta de la expectancia tenga una respuesta y formato correctos

* test_api_NuevoElo(): Testea que la respuesta del nuevoElo tenga una respuesta y formato correctos

* test_api_PartidasSuperarJugador(): Testea que la respuesta de PartidasSuperarJugador tenga una respuesta y formato correctos

* test_api_PartidasSuperarElo(): Testea que la respuesta de PartidasSuperarElo tenga una respuesta y formato correctos

* test_api_PartidasSuperarJugadorEst(): Testea que la respuesta de PartidasSuperarJugadorEst tenga una respuesta y formato correctos
