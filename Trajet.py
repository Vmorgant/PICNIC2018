import overpy
from Route import Route
from Dijkstra import *

class Trajet(object):
	def __init__(self, nom, info, depart, arrive):
		self.nom = nom		#nom du trajet
		self.info = info	#textes descriptifs
		self.depart = depart	#position deu départ
		self.arrive = arrive 	#position de l'arrivee
		self.routes = []
		self.trajet = [] #liste de points
		self.construireTrajet()

	#construit le trajet avec la latitude et la longitude des points d'arrivee et de depart
	def construireTrajet(self):
		api = overpy.Overpass()
		# fetch all ways and nodes
		query = """[out:json];way("""+str(self.depart[0])+""","""+str(self.depart[1])+""","""+str(self.arrive[0])+""","""+str(self.arrive[1])+""")[highway];(._;>;);out;"""
		lesRoutesPossible = api.query(query)
		for route in lesRoutesPossible:
			self.routes.append(Route(route))

		graphe = grapheCreer(self.routes,Point("dep",self.depart[0],self.depart[1]),Point("arr",self.arrive[0],self.arrive[1]))
		resDijkstra = dijkstra(graphe,"dep","arr")
		longueur = resDijkstra[0]
		chemin = resDijkstra[1]
		print (chemin)

trajet = Trajet("test","test", [47.9844782,0.2415538],[47.9879051,0.2012927])
