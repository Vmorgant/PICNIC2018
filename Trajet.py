class Trajet():
	def __init__(self, nom, info, depart, arrive):
		self.nom = nom		#nom du trajet
		self.info = info	#textes descriptifs
		self.depart = depart	#position deu départ
		self.arrive = arrive 	#position de l'arrivee
		self.routes
		
		
	def construireTrajet(self):
		api = overpy.Overpass()

		# fetch all ways and nodes
		result = api.query("""
			way("""+depart["lat"]+""","""+depart["lon"]+""","""+arrive["lat"]+""","""+arrive["lon"]+""") ["highway"];
			(._;>;);
			out body;
			""")
		self.construireRoutes(result)
	
	def construireRoutes(self, trajet):
		for route in trajet.way:
			self.routes.append(Route(route))
