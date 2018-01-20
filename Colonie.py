import overpy
import requests
import math
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
        self.seedColonie="5a5e71a2734d1d347185192c"
        self.position = [47.99026,0.23991] #Position de la Colonie
        self.listeFourmis = [Fourmi(0,self,tokens[0]),Fourmi(1,self,tokens[1]),Fourmi(2,self,tokens[2]),Fourmi(3,self,tokens[3])] #Liste des fourmis de la colonie
        self.graines = 0 #Nombre de graines actuellement dans la colonie



    #Getter pour la position
    def getPosition(self):
        return "5a5e71a2734d1d347185192c"
    #Ajoute une graine à la colonie et renvoi une fourmie
    def ajouterGraine(self,id):
        self.graines += 1
        self.listeFourmis[id].lancer()

    def graineLaPlusProche(self,seedList,token):
        i=0
        min = 20
        for seed in seedList:
            if (seed["type"]="seed"):
                seedcoord[i]={seed["location"]["coordinates"]}
                i+=1
        i=0
        for seed in seedcoord:
            if (min > math.sqrt(((seed[0]-self.position[0])**2)+((seed[1]-self.position[1])**2))):
                min = i
            i+=1;

        requests.post("https://f24h2018.herokuapp.com/api/tracks",data = {"name":"lapin","info":"","startSeedId":self.seedColonie,"endSeedId":seedList[i]["_id"]}
        requests.post("https://f24h2018.herokuapp.com/api/tracks",data = {"name":"lapin","info":"","startSeedId":seedList[i]["_id"],"endSeedId":self.seedColonie}
        return(seedList[i]["location"]["coordinates"])


    #Envoi une fourmi chercher une graine.
    def lancerFourmi(self,idFourmi):
        #
        token = tokens[idFourmi]
        header = headers{'Authorization':token}
        seedList = request.get("https://f24h2018.herokuapp.com/api/seeds/search",headers=header)

        r = requests.post(url,headers=header)

        api=overpy.Overpass()
        #Récup pos arrivée;
        cible = graineLaPlusProche(self,seedlist,token)

        nom="lapin"

        aller = Trajet(nom,"",self.position,cible)
        retour= Trajet("".join(reversed(nom)),"",cible,self.position)
        self.listeFourmis[idFourmi].setAller(aller)
        self.listeFourmis[idFourmi].setRetour(retour)
        self.listeFourmis[idFourmi].lancer()
