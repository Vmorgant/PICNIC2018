import overpy
import requests
import math
from Fourmi import Fourmi
from Trajet import Trajet
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
class Colonie():


    def __init__(self):
        self.seedColonie="5a5e71a2734d1d347185192c"
        self.position = [47.99026,0.23991] #Position de la Colonie
        self.listeFourmis = [Fourmi(0,self),Fourmi(1,self),Fourmi(2,self)] #Liste des fourmis de la colonie
        self.graines = 0 #Nombre de graines actuellement dans la colonie



    #Getter pour la position
    def getPosition(self):
        return self.position


    #Ajoute une graine à la colonie et renvoi une fourmie
    def ajouterGraine(self,id):
        self.graines += 1
        print(self.graines)

    def graineLaPlusProche(self,seedList,token):
        min = 20
        i=0
        seedcoord = []
        for seed in seedList.json():
            if (seed["type"]=="seed"):
                seedcoord.append(seed["location"]["coordinates"])
        for seed in seedcoord:
            if (min > math.sqrt(((seed[0]-self.position[0])**2)+((seed[1]-self.position[1])**2))):
                min = i
            i+=1

        #Declaration du trjet
        header = {'Authorization':"bearer "+token}
        aller = requests.post("https://f24h2018.herokuapp.com/api/tracks",headers=header,data = {"name":"lapin","info":"","startSeedId":self.seedColonie,"endSeedId":seedList.json()[i]["_id"]})
        retour =requests.post("https://f24h2018.herokuapp.com/api/tracks",headers=header,data = {"name":"lapin","info":"","startSeedId":seedList.json()[i]["_id"],"endSeedId":self.seedColonie})
        #(coordSeed,idSeed,[idAller,idRetour])
        return( (seedList.json()[i]["location"]["coordinates"],seedList.json()[i]["_id"],[aller.json()["_id"],retour.json()["_id"]]) )


    #Envoi une fourmi chercher une graine.
    def lancerFourmi(self,idFourmi, seedList):
        #Récup pos arrivée;
        repFourmi =  requests.post("https://f24h2018.herokuapp.com/auth/local",data = {"email":"ant"+str((idFourmi+1))+"@sugar.ant","password":"Baby"})
        token = repFourmi.json()['token']
        header = {'Authorization':"bearer "+token}
        cible = self.graineLaPlusProche(seedList,token)
        nom="lapin"
        aller = Trajet(nom,"",self.position,cible[0])
        retour= Trajet("".join(reversed(nom)),"",cible[0],self.position)
        self.listeFourmis[idFourmi].setAller(aller)
        self.listeFourmis[idFourmi].setRetour(retour)

        me = requests.get("https://f24h2018.herokuapp.com/api/users/me",headers=header)
        antId = me.json()["_id"]
        #print(antId)
        #la foumi fait le trajet
        #print(cible[1])
        idAller = cible[2][0]
        rep = requests.put("https://f24h2018.herokuapp.com/api/users/:"+str(antId)+"/position",headers=header, data={"seedId":cible[1]})
        self.listeFourmis[idFourmi].lancerAller(idAller)

        validTrajet =  requests.put("https://f24h2018.herokuapp.com/api/tracks/:"+idAller+"/end",headers=header,data = {"name":"lapin", "info":""})
        rep = requests.put("https://f24h2018.herokuapp.com/api/users/:"+str(antId)+"/position",headers=header, data={"seedId":self.seedColonie})

        idRetour = cible[2][1]
        graine = self.listeFourmis[idFourmi].lancerRetour(idRetour)
        if(graine):
            self.ajouterGraine(idFourmi)

        validTrajet =  requests.put("https://f24h2018.herokuapp.com/api/tracks/:"+idRetour+"/end",headers=header,data = {"name":"lapin", "info":""})

    def commencer(self):
        #repAnt1 = requests.post("https://f24h2018.herokuapp.com/auth/local",data = {"email":"ant1@sugar.ant","password":"Baby"})
        #repAnt2 = requests.post("https://f24h2018.herokuapp.com/auth/local",data = {"email":"ant2@sugar.ant","password":"Baby"})
        repAnt3 = requests.post("https://f24h2018.herokuapp.com/auth/local",data = {"email":"ant3@sugar.ant","password":"Baby"})
        token = repAnt3.json()['token']
        header = {'Authorization':"bearer "+token}
        seedList = requests.get("https://f24h2018.herokuapp.com/api/seeds/search",headers=header)
        for num,fourmi in enumerate(self.listeFourmis):
            self.lancerFourmi(num,seedList)

c = Colonie()
c.commencer()
