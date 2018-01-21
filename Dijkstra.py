from collections import defaultdict
from heapq import *
import overpy
import overpy.helper

def dijkstra(edges, f, t):
    g = defaultdict(list)
    for l,r,c in edges:
        g[l].append((c,r))

    q, seen = [(0,f,())], set()
    while q:
        (cost,v1,path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = (v1, path)
            if v1 == t: return (cost, path)

            for c, v2 in g.get(v1, ()):
                if v2 not in seen:
                    heappush(q, (cost+c, v2, path))

    return "Pas de chemin"

def calculPoids(route,P1,P2,):
    distance=P1.distance(P2)
    if((route.getHighway() != "tertiary" or route.getHighway() != "secondary" or route.getHighway() != "primary") or (route.getOneway == None)):
        distance = 9999
    Poids = distance/route.getMaxSpeed()
    return Poids

def memeroute(P1,P2,routes):
    point1 = False
    point2 = False
    for route in routes:
        for point in route.getNodes():
            if P1.getLatitude()==point.getLatitude() and P1.getLongitude() == point.getLongitude():
                point1=True
            if P2.getLatitude()==point.getLatitude() and P2.getLongitude() == point.getLongitude():
                point2=True
            if (point1 and point2):
                return (True,route)
        point1=False
        point2=False
    return (False,None)


def grapheCreer(routes,Pdep,Parr):
    routesNom = []
    edges = []
    pointRoute = []
    for route in routes:
        routesNom.append(route.getNom())
    intersections = []
    aFaire=routesNom[1:]
    for route in routesNom:
        for route2 in aFaire:
            intersections.append(overpy.helper.get_intersection(route,route2,3601403916))

        aFaire.remove(route)

    for (num,node) in enumerate(intersections):
        pointRoute.append(Point("P"+num,node.lat,node.lon))

    pointRoute.append(Pdep)
    pointRoute.append(Parr)
    aFaire=pointRoute
    for point in pointRoute:
        for point2 in aFaire:
            resMemRoute = memeroute(point,point2,routes)
            if resMemRoute[0]:
                edges.append((point.getNom(),point2.getNom(),calculPoids(resMemRoute[1],point,point2)))
    return edges
