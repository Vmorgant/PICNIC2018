import requests
from Trajet import Trajet
import time
import datetime

class Fourmi(object):

    """docstring for Fourmi."""
    def __init__(self, id, colonie):

        self.colonie = colonie
        self.id = id
        self.graine = False
        self.route = None #Route actuelle
        self.position = 0
        self.etat = "Colonie"
        self.vitesse = 0
        self.aller = None
        self.retour = None


    def getColonie(self):
        return self.colonie

    def setColonie(self,colonie):
        self.colonie = colonie

    def getId(self):
        return self.id

    def getGraine(self):
        return self.graine

    def setGraine(self,graine):
        self.graine = graine

    def getRoute(self):
        return self.route

    def setRoute(self, route):
        self.route

    def getEtat(self):
        return self.etat

    def setEtat(self, etat):
        self.etat = etat

    def getVitesse(self):
        return self.vitesse

    def setVitesse(self,vitesse):
        self.vitesse = vitesse

    def getAller(self):
        return self.aller

    def setAller(self,aller):
        self.aller = aller

    def getRetour(self):
        return self.retour

    def setRetour(self,retour):
        self.retour=retour

    def lancerAller(self,trackID):
        self.cheminEnCours = self.aller
        self.route = self.aller.getRoutes()[0]
        self.numRoute = 0
        tpsDebut = time.time()
        posColonie = self.colonie.getPosition()
        positions=[{"lat":posColonie[0],"lon":posColonie[1],"timestamp":datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%fZ')}]
        #Tant que la fourmi n'est pas arrivée à destination
        while (self.route.getNodes()[self.position] != (self.aller.getRoutes()[-1]).getNodes()[-1]):
            tpsTic = time.time()
            if((tpsTic - tpsDebut) >= 1):
                positions.append({"lat":self.route.getNodes()[self.position][0],"lon":self.route.getNodes()[self.position][1],"timestamp":datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%fZ')})
                tpsDebut = tpsTic
            self.vitesse = self.route.getMaxSpeed()
            self.avancer(self.vitesse)
        self.prendreGraine()
        repFourmi =  requests.post("https://f24h2018.herokuapp.com/auth/local",data = {"email":"ant"+str((self.id+1))+"@sugar.ant","password":"Baby"})
        token = repFourmi.json()['token']
        header = {'Authorization':"bearer "+token}
        rep = requests.post("https://f24h2018.herokuapp.com/api/positions/bulk",headers=header,data = {"trackId":trackID,"positions":positions})

    def lancerRetour(self,trackID):
        self.cheminEnCours = self.retour
        positions=[{"lat":self.route.getNodes()[self.position][0],"lon":self.route.getNodes()[self.position][1],"timestamp":datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%fZ')}]
        tpsDebut = time.time()
        #La fourmi repart
        while(self.route.getNodes()[self.position] != (self.aller.getRoutes()[-1]).getNodes()[-1]):
            tpsTic = time.time()
            if((tpsTic - tpsDebut) >= 1):
                positions.append({"lat":self.route.getNodes()[self.position][0],"lon":self.route.getNodes()[self.position][1],"timestamp":datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%fZ')})
                tpsDebut = tpsTic
            self.vitesse = self.route.getMaxSpeed()
            self.position = self.avancer()
        repFourmi =  requests.post("https://f24h2018.herokuapp.com/auth/local",data = {"email":"ant"+str((self.id+1))+"@sugar.ant","password":"Baby"})
        token = repFourmi.json()['token']
        header = {'Authorization':"bearer "+token}
        rep = requests.post("https://f24h2018.herokuapp.com/api/positions/bulk",headers=header,data = {"trackId":trackID,"positions":positions})
        return True


    def avancer(self,vitesse):
        self.vitesse = vitesse
        #print("pos"+str(self.position))
        if(self.position == len(self.route.getNodes())-1):
            self.numRoute += 1
            self.route = self.cheminEnCours.getRoutes()[self.numRoute]
            self.position = 0
        else:
            self.position += 1

    def prendreGraine(self):
        self.graine = True

    def arreter(self,temps):
        self.vitesse = 0
        time.sleep(temps)

    def validerTrajet(self):
        #Requete serveur
        return False
