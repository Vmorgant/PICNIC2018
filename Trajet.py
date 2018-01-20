class Trajet():
	def __init__(self, nom, info, depart, arrive):
		self.nom = nom		#nom du trajet
		self.info = info	#textes descriptifs
		self.depart = depart	#position deu départ
		self.arrive = arrive 	#position de l'arrivee
		self.routes
		
	#construit le trajet avec la latitude et la longitude des points d'arrivee et de depart
	def construireTrajet(self):
		api = overpy.Overpass()

		# fetch all ways and nodes
		result = api.query("""
			way("""+depart["lat"]+""","""+depart["lon"]+""","""+arrive["lat"]+""","""+arrive["lon"]+""") ["highway"];
			(._;>;);
			out body;
			""")
		self.construireRoutes(result)
		
	#construit le tableau des routes nécessaire au trajet en rajoutant les routes a la fin du tableau
	def construireRoutes(self, trajet):
		for route in trajet.way:
			self.routes.append(Route(route))
	
	#return tableau de routes pour classe fourmis		
	def getRoutes(self)
		return routes
