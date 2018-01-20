

class Point():

    def __init__(self,nom, node, route):
        self.nom = nom
        self.latitude = node.lat
        self.longitude = node.lon
        self.route = route

    def getLatitude(self):
        return self.latitude

    def getLongitude(self):
        return self.longitude

    def distance(p2):
        return math.sqrt( ( (self.latitude-p2.getLatitude() )**2) + ( (self.longitude-p2.getLongitude() )**2) )

    def getNom():
        return self.nom
