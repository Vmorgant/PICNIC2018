import overpy
from Route import Route
from Dijkstra import *
from Point import Point
import requests

class Trajet(object):
	def __init__(self, nom, info, depart, arrive):
		headers ={'Accept':'text/json; charset=utf-8','Content-Length':'0'}
		api_key="58d904a497c67e00015b45fc5c0d8ccc3c864a39be3e2bf8a90a38bd"
		x1 = depart[0]
		y1 = depart[1]
		x2 = arrive[0]
		y2 = arrive[1]
		request = requests.get('https://api.openrouteservice.org/directions?api_key=58d904a497c67e00015b45fc5c0d8ccc3c864a39be3e2bf8a90a38bd&coordinates='+str(y1)+'%2C'+str(x1)+'%7C'+str(y2)+'%2C'+str(x2)+'&profile=driving-car&geometry_format=geojson&preference=fastest', headers=headers)

		self.nom = nom		#nom du trajet
		self.info = info	#textes descriptifs
		self.depart = depart	#position deu départ
		self.arrive = arrive 	#position de l'arrivee
		self.routes = []
		taille = 0
		#print(request.json())
		for etape in request.json()["routes"][0]["segments"][0]["steps"][:-1]:
			#print(etape)
			vitesseMax = (etape["distance"]/etape["duration"])*3.6
			indDep = etape["way_points"][0]
			indFin = etape["way_points"][1]
			points = request.json()["routes"][0]["geometry"]["coordinates"][indDep:indFin]
			for point in points:
				point.reverse()
			#print(points)
			nom = etape["name"]
			#print(nom)
			self.routes.append(Route(nom,points,vitesseMax))

	def getRoutes(self):
		return self.routes

#Sens unique
#Longueur (petit)
#Rond-point
#Rond-point + sens unique
#Fleuve
#Fleuve + voix férée
#Le mans - Rouen
t = Trajet("test","test",[49.25216, -1.56078],[ 49.25216, -1.56078])
