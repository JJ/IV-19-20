import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
dirFlask = parentdir+"/flask"
sys.path.insert(0,dirFlask)




from Jugador import *


def test_Expectancia():
		Jugador1 = Jugador(1500)
		Jugador2 = Jugador(1800)
		var1 = Jugador1.getExpectancia(Jugador2.elo)

		assert(var1 > 0.150979557 and var1 < 0.150979558 ), "Fallo en calculo expectancia"
		assert Jugador1.getExpectancia(Jugador1.elo) == 0.5, "Fallo en calculo expectancia"

def test_NuevoElo():
		Jugador1 = Jugador(1500)
		Jugador1.k = 40
		Jugador2 = Jugador(1800) #todo
		var1 = Jugador1.getNuevoElo(Jugador2.elo, 1)
		assert var1 > 1533.96081771 and var1 < 1533.96081772, "Fallo en calculo de nuevo ELO"

def test_Percentil():
		Jugador1= Jugador(2000)
		Jugador2 = Jugador(2800)
		Jugador3 = Jugador(2700)

    
		var1 = Jugador1.getPercentil()
		var2 = Jugador2.getPercentil()
		var3 = Jugador3.getPercentil()

    
		assert var1 == 0.9462 and var2 == 1 and var3 == 0.9998, "Fallo en calculo de percentil"

		return 0

def test_PartidasSuperarJugador():
		Jugador1 = Jugador(2000)
		Jugador2 = Jugador(2800)
		assert (Jugador1.getPartidasSuperarJugador(Jugador2.elo) == 48), "Fallo en cálculo de PartidasSuperarJugador"
		
		

def test_PartidasSuperarElo():
		Jugador1 = Jugador(2000)
		Jugador2 = Jugador(2800)
		assert (Jugador1.getPartidasSuperarElo(Jugador2.elo) == 81), "Fallo en cálculo de PartidasSuperarElo"
		


def test_artidasSuperarEloEst():
		Jugador1 = Jugador(2000)
		Jugador2 = Jugador(3000)
		assert (Jugador1.getPartidasSuperarEloEst(Jugador2.elo, 1800) == 10766), "Fallo en cálculo de PartidasSuperarEloEst"
		



		
