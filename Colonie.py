import overpy
import requests

#COLONIE

#{"_id":"5a5e71a2734d1d347185192c",
#"name":"La fourmilière",
#"info":"Colonie","active":true,
#"type":"home",
#"location":{
#   "type":"Point",
#   "coordinates":[47.9844782,0.2415538]}},

#SEED

#{"_id":"5a5e7207734d1d347185195c",
#"name":"Epau",
#"info":"pas trop loin",
#"active":true,
#"type":"seed",
#"location":{
#   "type":"Point",
#   "coordinates":[47.99026,0.23991]}},

"""Classe représentant la colonie de départ, l'endroit d'ou partent les fourmis et l'endroit ou elles déposent les graines"""
class Colonie(self,args[]):


    def __init__(self):
        self.tokens=[requests.post("https://f24h2018.herokuapp.com/auth/local",data = {"email":"ant1@sugar.ant","password":"Baby"}),
        requests.post("https://f24h2018.herokuapp.com/auth/local",data = {"email":"ant2@sugar.ant","password":"Baby"}),
        requests.post("https://f24h2018.herokuapp.com/auth/local",data = {"email":"ant3@sugar.ant","password":"Baby"}),
        requests.post("https://f24h2018.herokuapp.com/auth/local",data = {"email":"ant4@sugar.ant","password":"Baby"})]
        self.seedColonie=
        self.position = {lon:x,lat:y,time:t} #Position de la Colonie
        self.listeFourmis = [Fourmi(0,self),Fourmi(1,self),Fourmi(2,self),Fourmi(3,self)] #Liste des fourmis de la colonie
        self.graines = 0 #Nombre de graines actuellement dans la colonie



    #Getter pour la position
    def getPosition(self):
        return self.position

    def ajouterGraine(self,id):
        self.graines += 1
        self.listeFourmis[id].lancer()
    #Envoi une fourmi chercher une graine.
    def lancerFourmi(self,idFourmi):
        #
        token = tokens[idFourmi]
        u
        header = headers{'Authorization':token}

        r = requests.post(url,headers=header)

        api=overpy.Overpass()
        #Récup pos arrivée;

        nom="lapin"
        aller = Trajet(nom,"",self.position,arrive)
        retour= Trajet("".join(reversed(nom)),"",arrive,self.position)
        self.listeFourmis[idFourmi].setAller(aller)
        self.listeFourmis[idFourmi].setRetour(retour)
        self.listeFourmis[idFourmi].lancer()
