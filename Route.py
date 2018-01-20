import overpy

api=overpy.Overpass()

class Route:
	
	def __init__(self, track):
		self.name=track.tags.get("name","n/a")
		self.oneway=track.tags.get("oneway","n/a")
		self.sidewalk=track.tags.get("sidewalk","n/a")
		self.surface=track.tags.get("surface","n/a")			self.cycleway=False
		self.rightway=track.tags.get("rightway","n/a")
		self.lit=track.tags.get("lit","n/a")
		self.maxspeed=track.tags.get("maxspeed","n/a")
		self.nodes=[]
		for node in track.nodes:
			self.nodes.append([node.lat,node.lon])


	def getMaxSpeed(self):
		return self.maxspeed

	def getNodes(self):
		return self.nodes	