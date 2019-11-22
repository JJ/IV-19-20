from flask import Flask, request, jsonify, Response
import json
from Jugador import Jugador
import os


app = Flask(__name__)


@app.route('/', methods=['GET'])
def inicio():
	status = {"status": "OK"}
	return json.dumps(status)

@app.route('/status', methods=['GET'])
def estado():
	status = {"status": "OK"}
	return json.dumps(status)

@app.errorhandler(404)
def page_not_found(e):
	return jsonify(error=str(e)), 404

#http://0.0.0.0:5000/Expectancia?elojug1=1500&elojug2=1800
@app.route('/Expectancia', methods=['GET'])
def func1():
	parametro1 = request.args.get('elojug1')
	parametro2 = request.args.get('elojug2')

	Jugador1 = Jugador(int(parametro1))
	Jugador2 = Jugador(int(parametro2))
	
	valor = str(Jugador1.getExpectancia(Jugador2.elo))
	data = {}
	data['expectancia'] = valor

	return Response(json.dumps(data), mimetype='application/json')

#http://0.0.0.0:5000/NuevoElo?elojug1=1500&elojug2=1800&k=40&resultado=1
@app.route('/NuevoElo')
def nuevo_elo():
	parametro1 = request.args.get('elojug1')
	parametro2 = request.args.get('elojug2')
	parametro4 = request.args.get('resultado')

	Jugador1 = Jugador(int(parametro1))
	Jugador2 = Jugador(int(parametro2))
	
	valor = str(Jugador1.getNuevoElo(int(parametro2), int(parametro4) ))
	data = {}
	
	data['nuevoElo'] = valor

	return Response(json.dumps(data), mimetype='application/json')



@app.route('/PartidasSuperarJugador')
def partidas_superar_jugador():
	parametro1 = request.args.get('elojug1')
	parametro2 = request.args.get('elojug2')

	Jugador1 = Jugador(int(parametro1))
	
	valor = str(Jugador1.getPartidasSuperarJugador(int(parametro2)) )
	
	data = {}
	
	data['partidasSuperarJugador'] = valor

	return Response(json.dumps(data), mimetype='application/json')


@app.route('/PartidasSuperarElo')
def partidas_superar_elo():
	parametro1 = request.args.get('elojug1')
	parametro2 = request.args.get('elojug2')

	Jugador1 = Jugador(int(parametro1))
	
	valor = str(Jugador1.getPartidasSuperarElo(int(parametro2)))
	
	data = {}
	
	data['partidasSuperarElo'] = valor

	return Response(json.dumps(data), mimetype='application/json')


@app.route('/PartidasSuperarEloEst')
def partidas_superar_elo_est():
	parametro1 = request.args.get('elojug1')
	parametro2 = request.args.get('elojug2')
	parametro3 = request.args.get('elojug3')
	
	Jugador1 = Jugador(int(parametro1))
	

	valor = str(Jugador1.getPartidasSuperarEloEst(int(parametro2), int(parametro3)))
	
	data = {}
	
	data['partidasSuperarEloEst'] = valor

	return Response(json.dumps(data), mimetype='application/json')


@app.route('/Jugadores')
def conseguir_jugadores():
	path = 'fichero_prueba.json'
	with open(path) as data_file:
		jugadores = json.load(data_file)

	
	return Response(json.dumps(jugadores), mimetype='application/json')

@app.route('/AniadirJugador', methods = ['PUT'])
def aniadir_jugador():

	path = 'fichero_prueba.json'
	with open(path) as data_file:
		data = json.load(data_file)

	data_file.close()
	data['jugadores'].append({'nombre': request.args['nombre'], 'elo': '0', 'k': '0'})


	with open('fichero_prueba.json', 'w') as outfile:
		json.dump(data, outfile)

	outfile.close()

	return ""

@app.route('/EliminarJugador', methods = ['DELETE'])
def eliminar_jugador():

	path = 'fichero_prueba.json'
	with open(path) as data_file:
		data = json.load(data_file)

	data_file.close()



	contador = 0
	for attrs in data['jugadores']:
		for key,value in attrs.items():
			if (key=="nombre" and value == request.args['nombre']):
				del data['jugadores'][contador]
		
		contador+=1

	with open('fichero_prueba.json', 'w') as outfile:
		json.dump(data, outfile)

	outfile.close()

	return ""


