import os,sys,inspect, json

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
dirFlask = parentdir+"/flask"
sys.path.insert(0,dirFlask)
import servicio

servicio.app.testing = True


def test_status():
	response = servicio.app.test_client().get('/')
	assert response.status_code == 200, "Código de estado erróneo"
	assert json.loads(response.data.decode())['status'] == 'OK'
	

def test_api_Expectancia():
	response = servicio.app.test_client().get('/Expectancia?elojug1=1500&elojug2=1800')
	assert response.status_code == 200, "Código de estado erróneo"
	assert response.content_type == 'application/json'

def test_api_NuevoElo():
	response = servicio.app.test_client().get('/NuevoElo?elojug1=1500&elojug2=1800&k=40&resultado=1')
	assert response.status_code == 200, "Código de estado erróneo"
	assert response.content_type == 'application/json'

def test_api_PartidasSuperarJugador():
	response = servicio.app.test_client().get('/PartidasSuperarJugador?elojug1=2000&elojug2=2500')
	assert response.status_code == 200, "Código de estado erróneo"
	assert response.content_type == 'application/json'

def  test_api_PartidasSuperarElo():
	response = servicio.app.test_client().get('/PartidasSuperarElo?elojug1=2300&elojug2=2500')
	assert response.status_code == 200, "Código de estado erróneo"
	assert response.content_type == 'application/json'

def  test_api_PartidasSuperarJugadorEst():
	response = servicio.app.test_client().get('/PartidasSuperarEloEst?elojug1=2300&elojug2=2500&elojug3=2000')
	assert response.status_code == 200, "Código de estado erróneo"
	assert response.content_type == 'application/json'

