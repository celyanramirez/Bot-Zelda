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
        self.__questions = ["Quel est le nom du 3e jeu Zelda ? 🟢",
                            "Quel est le nom du personnage principal ? 🟢",
                            "Dans Twilight Princess, quel est le nom du 6ème donjon ? 🟠",
                            "Dans quelle branche de la Timeline se trouve Oracle of Ages ? 🟢",
                            "Dans Wind Waker, comment s'appelle la jeune piaf de l'île du Dragon ? 🟢",
                            "En quelle année est sortie The Adventure of Link ? 🟠",
                            "En quelle année est sortie Oracle of Seasons ? 🟠",
                            "En quel mois et année est sortie TriForce Heroes ? 🔴",
                            "Quel est le bon ordre (chronologiquement) des différents jeux ? 🔴",
                            "Dans Majora's Mask 3D, où est installé le banquier ? 🟠",
                            "Dans Majora's Mask 3D, combien il y a-t-il de flacons ? 🔴",
                            "Dans Wind Waker HD, combien il y a-t-il d'îles ? 🔴",
                            "Dans Minish Cap, où obtient-on le bouclier miroir ? 🔴",
                            "Dans Breath of the Wild, quel est le nom de notre premier sanctuaire ? 🔴",
                            "Dans Twilight Princess, comment s'appelle le Dieu qui vit près de Toal ? 🟢",
                            "Qui a composé les musiques du jeu Link's Awakening ? 🔴",
                            "Dans Link's Awakening, parmis ces 4 emplacements de téléporteur 1 n'existe pas, lequel c'est ? 🔴"]

        self.__reponses = {0 : ["1️⃣ OOT", "2️⃣ ALTTP", "3️⃣ ALBW", "4️⃣ LA"],
                           1 : ["1️⃣ Link", "2️⃣ Zelda", "3️⃣ Tingle", "4️⃣ Linkle"],
                           2 : ["1️⃣ Tour du Jugement", "2️⃣ Château des Pics Blancs", "3️⃣ Célestia", "4️⃣ Ruines des Pics Blancs"],
                           3 : ["1️⃣ Timeline de la défaite", "2️⃣ Timeline de l'enfance", "3️⃣ Timeline de Link Adulte", "4️⃣ Début de la légende"],
                           4 : ["1️⃣ Romanie","2️⃣ Melodie", "3️⃣ Elwing", "4️⃣ Medolie"],
                           5 : ["1️⃣ 1986", "2️⃣ 1987", "3️⃣ 1985", "4️⃣ 1988"],
                           6 : ["1️⃣ 1999", "2️⃣ 1989", "3️⃣ 2003", "4️⃣ 2001"],
                           7 : ["1️⃣ Août 2015", "2️⃣ Janvier 2016", "3️⃣ Octobre 2015", "4️⃣ Novembre 2015"],
                           8 : ["1️⃣ SS-MC-FS-OOT", "2️⃣ SS-FS-MC-OOT", "3️⃣ SS-OOT-MC-FS", "4️⃣ SS-OOT-FS-MC"],
                           9 : ["1️⃣ A l'Ouest de Bourg-Clocher", "2️⃣ A l'Est de Bourg-Clocher", "3️⃣ Derrière la tour de l'Horloge", "4️⃣ Devant la tour de l'Horloge"],
                           10 : ["1️⃣ 7", "2️⃣ 6", "3️⃣ 8", "4️⃣ 5"],
                           11 : ["1️⃣ 45", "2️⃣ 49", "3️⃣ 50", "4️⃣ 38"],
                           12 : ["1️⃣ Par un Zora", "2️⃣ Dans un donjon", "3️⃣ Par un Goron", "4️⃣ Par un marchand"],
                           13 : ["1️⃣ Gu'Achitoh", "2️⃣ Moa'Kishito", "3️⃣ Ma'Ohnu", "4️⃣ Shora'Ha"],
                           14 : ["1️⃣ Lanelle", "2️⃣ Ordin", "3️⃣ Latouane", "4️⃣ Firone"],
                           15 : ["1️⃣ Satoru Iwata", "2️⃣ Minako Hamano", "3️⃣ Kazumi Totaka", "4️⃣ Shigefumi Hino"],
                           16 : ["1️⃣ Au Nord du village des Animaux", "2️⃣ A l'Est du village des Mouettes", "3️⃣ Au Sud de l'Abîme du poisson", "4️⃣ Dans le plateau Tartare Ouest"]}

        self.__bonneReponse = ["2️⃣ ALTTP",
                               "1️⃣ Link",
                               "4️⃣ Ruines des Pics Blancs",
                               "1️⃣ Timeline de la défaite",
                               "4️⃣ Medolie",
                               "2️⃣ 1987",
                               "4️⃣ 2001",
                               "3️⃣ Octobre 2015",
                               "1️⃣ SS-MC-FS-OOT",
                               "3️⃣ Derrière la tour de l'Horloge",
                               "1️⃣ 7",
                               "2️⃣ 49",
                               "3️⃣ Par un Goron",
                               "3️⃣ Ma'Ohnu",
                               "3️⃣ Latouane",
                               "2️⃣ Minako Hamano",
                               "1️⃣ Au Nord du village des Animaux"]

        self.__tab = ['1️⃣' , '2️⃣', '3️⃣', '4️⃣', '❌']
        self.__lancer = False
        self.place = 0

    def getQuestions(self):
        return self.__questions
 
    def getReponses(self):
        return self.__reponses

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


class Joueur:

    def __init__(self,user):
        self.user = user
        self.points = 0
        self.jouer = 0

    def getUser(self):
        return self.user.name
    
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
    

class Classement:

    def __init__(self):
        self.tabJoueursObjet = [] #Tableau de "Joueur"
        self.tabClassement = []

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

            for i in range(len(self.tabJoueursObjet)):
                tab.append(self.tabJoueursObjet[i])

            joueurMax = Joueur
            for i in liste:
                if max < i.getPoints():
                    max = i.getPoints()
                    joueurMax = i
            tab.remove(joueurMax)
            print(joueurMax.getUser())
            self.tabClassement.append(joueurMax)
            return tab

    def getTabClassement(self):
        return self.tabClassement

    def getPlaceJoueurClassementEtPoints(self, joueur):
        j = 0
        for i in self.tabClassement:
            j+=1
            if i.getUser() == joueur:
                return j, i.getPoints()
        return 0,0


'''
@bot.command()
async def combat(ctx, mec, mec2):
    attaque = ["Foudre", "Feu", "Attaque standard", "Kamikaze", "bouclier"]
    dégât = [50, 20, 10, 0, 0]
    mecvie = 100
    mec2vie = 100
    persos = [mec, mec2]
    rdm = random.randint(0,1)
    savebouclier = False
    while mecvie > 0 or mec2vie > 0:
        if mecvie <= 0:
            await ctx.send(f"{mec2} gagne !")
            break
        elif mec2vie <= 0:
            await ctx.send(f"{mec} gagne !")
            break
        a = persos[rdm]
        await ctx.send(f"C'est au tour de {a} de jouer !")
        await asyncio.sleep(1)
        if a == mec:
            rdm = random.randint(0,3)
            attack = attaque[rdm]
            if attack == "bouclier":
                await ctx.send(f"{a} utilise bouclier !")
                await asyncio.sleep(1)
                savebouclier = True
                k = 1
            elif attack == "Kamikaze":
                await ctx.send(f"{a} attaque avec Kamikaze !...")
                await ctx.send(f"Ah bah vous êtes tous mort")
                break
            else:
                mec2vie = mec2vie - dégât[rdm]
                await ctx.send(f"{a} attaque avec {attack} ! {mec2} perd {dégât[rdm]}pv !")
                await asyncio.sleep(1)
                k = 1
        elif a == mec2:
            rdm = random.randint(0,3)
            attack = attaque[rdm]
            if attack == "bouclier":
                await ctx.send(f"{a} utilise bouclier !")
                await asyncio.sleep(1)
                k = 0
            elif attack == "Kamikaze":
                await ctx.send(f"{a} attaque avec Kamikaze !...")
                await ctx.send(f"Ah bah vous êtes tous mort")
                break
            else:
                mecvie = mecvie - dégât[rdm]
                await ctx.send(f"{a} attaque avec {attack} ! {mec} perd {dégât[rdm]}pv !")
                await asyncio.sleep(1)
                k = 0
        #####################################################Prochain Tour
        b = persos[k]     
        await ctx.send(f"C'est au tour de {b} de jouer !")
        if b == mec:
            rdm = random.randint(0,3)
            attack = attaque[rdm]
            if attack == "bouclier":
                await ctx.send(f"{b} utilise bouclier !")
                await asyncio.sleep(1)
                savebouclier = True
            elif savebouclier == True:
                await ctx.send(f"L'adversaire ayant utilisé un bouclier, {b} ne peut pas attaquer !")
                await asyncio.sleep(1)
                savebouclier = False
            elif attack == "Kamikaze":
                await ctx.send(f"{b} attaque avec Kamikaze !...")
                await ctx.send(f"Ah bah vous êtes tous mort")
                break
            else:
                mec2vie = mec2vie - dégât[rdm]
                await ctx.send(f"{b} attaque avec {attack} ! {mec2} perd {dégât[rdm]}pv !")
                await asyncio.sleep(1)
        elif b == mec2:
            rdm = random.randint(0,3)
            attack = attaque[rdm]
            if attack == "bouclier":
                await ctx.send(f"{b} utilise bouclier !")
                await asyncio.sleep(1)
                savebouclier = True
            elif savebouclier == True:
                await ctx.send(f"L'adversaire ayant utilisé un bouclier, {b} ne peut pas attaquer !")
                await asyncio.sleep(1)
                savebouclier = False
            elif attack == "Kamikaze":
                await ctx.send(f"{b} attaque avec Kamikaze !...")                
                await ctx.send(f"Ah bah vous êtes tous mort")
                break
            else:
                mec2vie = mec2vie - dégât[rdm]
                await ctx.send(f"{b} attaque avec {attack} ! {mec} perd {dégât[rdm]}pv !")
                await asyncio.sleep(1)
'''