import overpy
import requests
import fourmi.py
import trajet.py
"""Classe représentant la cigale qui valide ou invalide les trajets des équipes."""
class Cigale(self, id, colonie) :
    
    def __init__(self, equipe):
        self.erreur=False
    
    def getListeTrajet(self) :
        return(requests.get("https://f24h2018.herokuapp.com/api/tracks/otherTeams"))
    
    def getPosition(self,trajets) : 
        return(requests.get("https://f24h2018.herokuapp.com/api/tracks/:5a6350688fb12f001481b340/positions")
    
    def verifPosition(self,position) :
        
        #envoyer id trajet+erreur
               
    def verifPosition(self,position) :
        position["lon"]
        if (position["highway"]!="primary" && position["highway"]!="secondary" && position["highway"]!="tertiary") :
            self.erreur=True
        else if (position["surface"]!=asphalt) :
            self.erreur=True
        else if(position["access"]!="yes" || position["access"]!="unknown") :
            self.erreur=True

    
    
