import overpy
from Point import Point

api=overpy.Overpass()

class Route(object):

	def __init__(self, nom,points,vitesse):

		self.name = nom
		self.nodes=points
		self.maxspeed=vitesse

	def getMaxSpeed(self):
		return self.maxspeed

	def getNodes(self):
		return self.nodes

	def getNom(self):
		return self.name
