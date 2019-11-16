class Jugador:
		
	def __init__(self, elo, k=None, nombre=None):
		self.nombre = nombre
		self.elo = elo
		self.k = k

	def __init__(self, elo):
		self.elo = elo
		self.nombre = "noasignado"
		self.k = 10

	def getExpectancia(self, eloB):
		return 1/(1+10**((eloB - self.elo)/400))

	def getNuevoElo(self, eloB, resultado):
		return self.elo + self.k*(resultado-self.getExpectancia(eloB))
	
	def testMetodo(self):
		return 8/5
	
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
	
	

