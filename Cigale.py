import overpy
import requests
import fourmi.py
import trajet.py
import math
"""Classe représentant la cigale qui valide ou invalide les trajets des équipes."""
class Cigale(self, id, colonie) :
    
    def __init__(self, equipe):
        self.erreur=False
        self.message="Aucune erreur"
        self.distanceTot=0
        self.vTraj=0
        self.vFourmi=0
    
    def getListeTrajet(self) :
        """recuperation de la liste des trajets effectués par les autres équipes"""
        return(requests.get("https://f24h2018.herokuapp.com/api/tracks/otherTeams"))
    
    def getPosition(self,trajets) : 
         """recuperation de la liste des positions d'un trajet"""
        return(requests.get("https://f24h2018.herokuapp.com/api/tracks/5a6350688fb12f001481b340/positions")
    
               
    def verifPosition(self,position) :
        #verifie si le trajet est valide et renvoie le message d'erreur
        if (position["highway"]!="primary" && position["highway"]!="secondary" && position["highway"]!="tertiary" && position["highway"]!=["motorway"]) :
            self.erreur=True
            self.message="Route non autorisée à la circulation"
            
        else if (position["surface"]!=asphalt) :
            self.erreur=True
            self.message="Route non autorisée"
        else if(position["access"]!="yes" || position["access"]!="unknown") :
            self.erreur=True
            self.message="Route interdite"
        return (self.erreur)
        
        
    def verifTrajet(self,trajet) :
         #verifie si le trajet est valide et renvoie le message d'erreur
        position=getPosition(trajet)
        arrive=getArrive(trajet)
        depart=getDepart(trajet)
        
        res=requests.get("https://api.openrouteservice.org/directions?api_key=58d904a497c67e00015b45fc5c0d8ccc3c864a39be3e2bf8a90a38bd&coordinates=0.2415538%2C47.9844782%7C0.2222387%2C47.9809281&profile=driving-car&geometry_format=geojson")
        
        i=0
        
        for(position in trajet) :{
            if(position["id"]!= trajet["endSeedId"] :
                lonDepart=position["lon"]
                lonArrive=(position+1)["lon"]
                latDepart=position["lat"]
                latArrive=(position+1)["lat"]
            
                dateDep=position["timestanp"]
                dateArrive=(position+1)["timestanp"]
                
                
                distance=math.sqrt(((lonDepart-lonArrive)**2)+((latDepart-latArrive)**2))
                temps=dateArrive-dateDep
                self.vFourmi=distance/temps
                
            d=res["segments"]["steps"]["distance"]
            t=res["segments"]["steps"]["duration"]
            self.vTraj=d/t
            
            #si stop dateArrive doit au moins avoir 2 sec en plus
            if(position["highway"] == "stop" && dateArrive < dateDep      && i!=1):
                self.erreur = True
                self.message="Stop non respecte"
                i = 1
                
            #si feu dateArrive doit au moins avoir 2 sec en plus
            if(position["highway"] == "traffic_signals" && dateArrive < dateDep           && i!=1):
                self.erreur = True
                self.message="Feu non respecte"
                i = 1
            
            #vitesse en priorites a droite doit etre comprise entre 25 et 10
            if(position["highway"] == "crossing" && vFourmi > 25 || vFourmi < 10 && i!=1 ):
                self.erreur = True
                self.message="priorite non respecter non respecte "+self.vFourmi +" au lieu d'une vitesse comprise entre 10 et 25"
                i = 1
                
            #vitesse < ou egale a 50 = infraction sur une autoroute
            if(position["highway"] == "motorway" && vFourmi <= 50 && i!=1 ):
                self.erreur = True
                self.message="vitesse trop basse en autoroute "+self.vFourmi +"<=50"
                i = 1
                
            if(self.vFourmi > self.vTraj && i!=1):
               self.erreur=True
               self.message="Depassement de vitesse "+self.vFourmi +">"+ self.vTraj
               i = 1
            else
                verifPosition(position)
            
            
            
            if(self.erreur==True)
                return(requests.post("https://f24h2018.herokuapp.com/api/analyses",data = {"trackId : "+ trajet.id+" positionId : "+position+"description : "+self.message}
            
        
        
        
        return(requests.post("https://f24h2018.herokuapp.com/api/analyses",data = {"trackId": trajet.id,"positionId": position,"description": self.message}
                             
                             
        
    
