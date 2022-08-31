from discord.ext import commands
import discord
import asyncio
import random
import time

class Botdisc:

    def __init__(self):
        self.check = False
        self.garde = False
        self.def_open = False
        self.participants = []
        self.points = []
        
class Quizz:
    
    def __init__(self):
        
        self.__questions = [
                            "Combien de vœux ont été exaucés par la Triforce jusqu'à présent dans toute la série ? 🔴",

                            "/img0De quel opus provient cette Zelda ? 🟠",
                            "/img1Dans un des Zelda, il y a exactement ce son qui se lance quand on récupère une clé dans un coffre. Lequel c'est ? 🔴",
                            "/img2Dans The Wind Waker, comment débloque-t-on cette technique ? 🟠",
                            "/img3De quel jeu vient cet Artwork de Link ? 🟢",
                            "/img4De quel jeu vient cet Artwork de Ganondorf ? 🟠",
                            "/img5Dans quelle région de BOTW se trouve ce Relais ? 🟠"]

        self.__reponses = {
                           0 : ["6", "3", "1", "5"],
                           1 : ["A Link to the Past", "Zelda I", "Zelda II", "A Link Between Worlds"],
                           2 : ["A Link Between Worlds", "Link's Awakening HD", "Ocarina of Time 3D", "TriForce Heroes"],
                           3 : ["En donnant 10 blasons d'épéiste à Orco", "En donnant 10 fragments du bonheur à Orco", "En libérant une Grande Fée", "On le débloque en post-game"],
                           4 : ["Hyrule Warriors", "Hyrule Warriors : l'Ere du Fléau", "Majora's Mask", "Ocarina of Time"],
                           5 : ["Super Smash Bros Wii U/3DS", "Super Smash Bros Brawl", "Twilight Princess", "Hyrule Warriors"],
                           6 : ["Akkala", "Elimih", "Ordinn", "Lanelle"]}
                           
        self.__bonneReponse = [
                               "6",
                               "A Link to the Past",
                               "A Link Between Worlds",
                               "En donnant 10 blasons d'épéiste à Orco",
                               "Hyrule Warriors",
                               "Super Smash Bros Wii U/3DS",
                               "Akkala"]

        self.__images = ["images/zelda_gba.png",
                         "images/cle_obtenue.mp3",
                         "images/technique.mp4",
                         "images/ylink.png",
                         "images/ganondorf.png",
                         "images/relais.png"]

        self.__tab = ['<:AA:946480160830554123>' , '<:BB:946480160763437056>', '<:CC:946480160922828850>', '<:DD:946480161304506428>', '❌']
        self.__lancer = False
        self.place = 0
        self.quizzEnCours = False
        self.contientImage = False
        self.lienImage = ""

    def getQuestions(self):
        return self.__questions
 
    def getReponses(self):
        return self.__reponses

    def getImages(self):
        return self.__images

    def getLancer(self):
        return self.__lancer

    def setLancer(self, boolean):
        assert boolean in [True,False]
        self.__lancer = boolean
        
    def getBonneReponse(self):
        return self.__bonneReponse

    def getTab(self):
        return self.__tab

    def getPlace(self):
        return self.place

    def setPlace(self,x):
        self.place = x

    def setQuizzEnCours(self, boolean):
        assert boolean in [True,False]
        self.quizzEnCours = boolean

    def getQuizzEnCours(self):
        return self.quizzEnCours

    def getContientImage(self):
        return self.contientImage
    
    def setContientImage(self, val):
        self.contientImage = val
    
    def setLienImage(self, val):
        self.lienImage = val

    def getLienImage(self):
        return self.lienImage


class Joueur:

    def __init__(self,user):
        self.user = user
        self.points = 0
        self.jouer = 0
        self.aPerduPoint = False

    def getUser(self):
        return self.user.name

    def getUserId(self):
        return self.user.id
    
    def getPoints(self):
        return self.points

    def setPointsToUser(self, pt):
        self.points += pt

    def rmPointsToUser(self):
        test = self.points - 1
        if test < 0:
            self.points = 0
        else:
            self.points = test
        return test

    def setJouer(self):
        self.jouer += 1

    def restartJouer(self):
        self.jouer = 0

    def getJouer(self):
        return self.jouer

    def donnerNombrePoint(self,x):
        self.points = x

    def setAPerduPoint(self, x):
        assert x in [True,False]
        self.aPerduPoint = x

    def getAPerduPoint(self):
        return self.aPerduPoint
    

class Classement:

    def __init__(self):
        self.tabJoueursObjet = [] #Tableau de "Joueur"
        self.tabClassement = []
        self.tabJoueursId = []

    def ajouterJoueurs(self, joueur):
        self.tabJoueursObjet.append(joueur)

    def getTabJoueursObjet(self):
        return self.tabJoueursObjet

    def resetClassement(self):
        self.tabClassement = []

    def ajoutMaxAListe(self, liste):
        if len(liste) < 1:
            return None
        else:
            max = 0
            tab = []

            joueurMax = Joueur
            for i in liste:
                if max < i.getPoints():
                    max = i.getPoints()
                    joueurMax = i
            if len(liste) > 1 and joueurMax != Joueur: #Je vérifie si joueurMax != Joueur car sinon si dans la liste
                liste.remove(joueurMax)                #il y a un joueur qui a 0 point, il sera considéré juste comme "Joueur"
                self.tabClassement.append(joueurMax)   #et n'aura donc pas de self. Ce qui fait crash le classement.
            elif joueurMax != Joueur:
                self.tabClassement.append(joueurMax)
                liste = self.tabJoueursObjet
            return liste

    def getTabClassement(self):
        return self.tabClassement

    def getPlaceJoueurClassementEtPoints(self, joueur):
        j = 0
        for i in self.tabClassement:
            j+=1
            if i.getUser() == joueur:
                return j, i.getPoints()
        return 0,0

    def getTabJoueursId(self):
        return self.tabJoueursId
    
    def ajouterJoueursId(self, id):
        self.tabJoueursId.append(id)
