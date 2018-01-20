import overpy

api=overpy.Overpass()

class Route(object):

	def __init__(self, track):
		self.name=track.tags.get("name","n/a")
		self.oneway=track.tags.get("oneway","n/a")
		self.sidewalk=track.tags.get("sidewalk","n/a")
		self.surface=track.tags.get("surface","n/a")
		self.cycleway=track.tags.get("cycleway","n/a")
		self.rightway=track.tags.get("rightway","n/a")
		self.lit=track.tags.get("lit","n/a")
		self.maxspeed=track.tags.get("maxspeed","50")
		self.nodes=[]
		for node in track.nodes:
			self.nodes.append([node.lat,node.lon])


	def getMaxSpeed(self):
		return self.maxspeed

	def getNodes(self):
		return self.nodes
