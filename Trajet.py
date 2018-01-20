import overpy
from Route import Route

class Trajet(object):
	def __init__(self, nom, info, depart, arrive):
		self.nom = nom		#nom du trajet
		self.info = info	#textes descriptifs
		self.depart = depart	#position deu départ
		self.arrive = arrive 	#position de l'arrivee
		self.routes = []
		self.construireTrajet()

	#construit le trajet avec la latitude et la longitude des points d'arrivee et de depart
	def construireTrajet(self):
		api = overpy.Overpass()
		# fetch all ways and nodes
		query = """[out:json];way("""+str(self.depart[0])+""","""+str(self.depart[1])+""","""+str(self.arrive[0])+""","""+str(self.arrive[1])+""")[highway];(._;>;);out;"""
		lesCheminsPossibles = api.query(query)
		print(lesCheminsPossibles)
		leChemin = self.chercherMeilleurChemin(lesCheminsPossibles)
		self.construireRoutes(leChemin)


	def chercherMeilleurChemin(self,lesChemins):
		lesCheminsBon = []
		for chemin in lesChemins.ways:
			type = chemin.tags.get("highway")
			print(chemin.tags.get("oneway"))
			if( (type == "tertiary" or type == "secondary" or type == "primary") and (chemin.tags.get("oneway") != None)):
				lesCheminsBon.append(chemin)
		minLong=900
		meilleurChemin = None
		for chemin in lesCheminsBon:
			if(len(chemin.nodes) < minLong):
				minLong = len(chemin.nodes)
				meilleurChemin = chemin
		return meilleurChemin

	#construit le tableau des routes nécessaire au trajet en rajoutant les routes a la fin du tableau
	def construireRoutes(self, trajet):
			self.routes = Route(trajet)

	#return tableau de routes pour classe fourmis
	def getRoutes(self):
		return self.routes
#trajet = Trajet("rfqegzfruqez","info",[47.984393,0.236012],[47.984946,0.238951])
#trajet = Trajet("rfqegzfruqez","info",[47.9844782,0.2415538],[47.981339, 0.233318])
#print(trajet.routes)

import overpy

api = overpy.Overpass()

# fetch all ways and nodes
result = api.query("""
    way(50.746,7.154,50.748,7.157) ["highway"];
    (._;>;);
    out body;
    """)
print(result.areas())
for way in result.ways:
    print("Name: %s" % way.tags.get("name", "n/a"))
    print("  Highway: %s" % way.tags.get("highway", "n/a"))
    print("  Nodes:")
    for node in way.nodes:
        print("    Lat: %f, Lon: %f" % (node.lat, node.lon))
