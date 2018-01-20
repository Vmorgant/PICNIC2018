from Trajet import Trajet

class Fourmi(object):

    """docstring for Fourmi."""
    def __init__(self, id, colonie):

        self.colonie = colonie
        self.id = id
        self.graine = False
        self.route = NULL #liste de
        self.position = 0
        self.etat = "Colonie"
        self.vitesse = 0
        self.aller = NULL
        self.retour = NULL


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

    def lancer(self):
        self.cheminEnCours = self.aller
        self.route = self.aller.getRoutes()[0]
        self.numRoute = 0
        #Tant que la fourmi n'est pas arrivée à destination
        while (self.route.getNodes()[position] != self.cheminEnCours.arrive):
            self.vitesse = self.route.getMaxSpeed()-5
            self.avancer(vitesse)
        self.prendreGraine()
        self.cheminEnCours = self.retour
        while(self.route.getNodes()[position] != self.cheminEnCours.arrive):
            self.vitesse = self.route.getMaxSpeed()-5
            self.position = self.avancer()
        self.deposerGraine()


    def avancer(self,vitesse):
        self.vitesse = vitesse
        if(self.position == len(self.route)-1):
            self.route = self.cheminEnCours.getRoutes()[self.numRoute+1]
            self.position = 0
        else:
            self.position += 1

    def prendreGraine():
        self.graine = True

    def arreter(self,temps):
        self.vitesse = 0
        time.sleep(temps)

    def validerTrajet(self):
        #Requete serveur


    def deposerGraine(self):
        self.vitesse = 0
        self.colonie.ajouterGraine(self.id)
        self.graine = False



aller = Trajet("rfqegzfruqez","info",[47.981339, 0.233318],[47.9844782,0.2415538])
retour = Trajet("rfqegzfruqez","info",[47.9844782,0.2415538],[47.981339, 0.233318])
