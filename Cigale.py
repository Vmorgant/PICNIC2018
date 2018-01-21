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
        sel.distanceTot=0
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
        if (position["highway"]!="primary" && position["highway"]!="secondary" && position["highway"]!="tertiary") :
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
            
            if(self.vFourmi > self.vTraj
               self.erreur=True
               self.message="Depassement de vitesse "+self.vFourmi +">"+ self.vTraj
            else
                verifPosition(position)
            if(self.erreur==True)
                return(requests.post("https://f24h2018.herokuapp.com/api/analyses",data = {"trackId : "+ trajet.id+" positionId : "+position+"description : "+self.message}
        
        return(requests.post("https://f24h2018.herokuapp.com/api/analyses",data = {"trackId": trajet.id,"positionId": position,"description": self.message}
                             
                             
        
    
