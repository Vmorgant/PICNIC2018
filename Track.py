import requests
from Fourmi import Fourmi

headers ={'Accept':'text/json; charset=utf-8','Content-Length':'0'}
api_key="58d904a497c67e00015b45fc5c0d8ccc3c864a39be3e2bf8a90a38bd"
x1 = 47.9809281
y1 = 0.2222387
x2 = 47.9844782
y2 = 0.2415538
request = requests.get('https://api.openrouteservice.org/directions?api_key=58d904a497c67e00015b45fc5c0d8ccc3c864a39be3e2bf8a90a38bd&coordinates='+str(y1)+'%2C'+str(x1)+'%7C'+str(y2)+'%2C'+str(x2)+'&profile=driving-car&geometry_format=geojson', headers=headers)


print("cf")
f = Fourmi(1,"bleu")
f.setAller(request.json()["routes"][0]["geometry"]["coordinates"])
f.suivre()

taille = 0
lesRoutes = []
for etape in request.json()["routes"][0]["segments"][0]["steps"][:-1]:
    #print(etape)
    vitesseMax = (etape["distance"]/etape["duration"])*3.6
    indDep = etape["way_points"][0]
    indFin = etape["way_points"][1]
    points = request.json()["routes"][0]["geometry"]["coordinates"][indDep:indFin]
    nom = etape["name"]
    lesRoutes.append(Route(nom,points,vitesseMax))
