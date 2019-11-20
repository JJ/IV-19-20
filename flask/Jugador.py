class Jugador:

	def __init__(self, elo, nombre=None):
		self.nombre = nombre
		self.elo = elo

		if (elo < 2100):
			self.k = 32
		elif (2100 <= elo <= 2400):
			self.k = 24
		else:
			self.k = 16

		self.nombre = nombre
		
	def getExpectancia(self, eloB):
		return 1/(1+10**((eloB - self.elo)/400))

	def getNuevoElo(self, eloB, resultado):
		return self.elo + self.k*(resultado-self.getExpectancia(eloB))

	def getPartidasSuperarJugador(self, eloB): 
		copia1 = Jugador(self.elo)
		copia2 = Jugador(eloB)
		
		if (copia1.elo > copia2.elo):
			return 0

		else: 
			contador=0

			while copia1.elo <= copia2.elo:
				nuevo_elo_copia1 = self.getNuevoElo(copia2.elo, 1) # copia 1 gana
				nuevo_elo_copia2 = copia2.getNuevoElo(copia1.elo, 0) # copia 2 pierde

				copia1 = Jugador(nuevo_elo_copia1)
				copia2 = Jugador(nuevo_elo_copia2)

				contador+=1
	
			return contador
			
			

	def getPartidasSuperarElo(self, eloObjetivo):
		copia1 = Jugador(self.elo)
		
		if (copia1.elo > eloObjetivo):
			return 0

		else:
			contador = 0

			while copia1.elo <= eloObjetivo:
				nuevo_elo = copia1.getNuevoElo(copia1.elo, 1)
				
				copia1 = Jugador(nuevo_elo)
				contador+=1

			return contador


			
	def getPartidasSuperarEloEst(self, eloObjetivo, eloOponentes):
		copia1 = Jugador(self.elo)
		
		assert((eloObjetivo - eloOponentes) < 2200), "Diferencia de ELO demasiado grande"
			
		if (copia1.elo > eloObjetivo):
			return 0

		else:
			contador = 0

			while copia1.elo <= eloObjetivo:
				nuevo_elo = copia1.getNuevoElo(eloOponentes, 1)
				copia1 = Jugador(nuevo_elo)
				contador+=1

			return contador
	
				
	
	def getPercentil(self):
		if (self.elo > 2700):
			return 1
		elif (self.elo > 2600):
			return 0.9998
		elif (self.elo > 2500):
			return 0.9988
		elif (self.elo > 2400):
			return 0.9974
		elif (self.elo > 2300):
			return 0.9954
		elif (self.elo > 2200):
			return 0.9919
		elif (self.elo > 2100):
			return 0.9813
		elif (self.elo > 2000):
			return 0.9694
		elif (self.elo > 1900):
			return 0.9462
		else: return 0 #todo http://www.uschess.org/archive/ratings/ratedist.php

