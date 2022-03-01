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
                            "Quel est le bon ordre (chronologiquement) de ces différents jeux ? 🔴",
                            "Dans Majora's Mask 3D, où est installé le banquier ? 🟠",
                            "Dans Majora's Mask 3D, combien il y a-t-il de flacons ? 🔴",
                            "Dans Wind Waker HD, combien il y a-t-il d'îles ? 🔴",
                            "Dans Minish Cap, où obtient-on le bouclier miroir ? 🔴",
                            "Dans Breath of the Wild, quel est le nom de notre premier sanctuaire ? 🔴",
                            "Dans Twilight Princess, comment s'appelle le Dieu qui vit près de Toal ? 🟢",
                            "Qui a composé les musiques du jeu Link's Awakening ? 🔴",
                            "Dans Link's Awakening, parmis ces 4 emplacements de téléporteur 1 n'existe pas, lequel c'est ? 🔴",
                            "Au début de Wind Waker, qui enlève la petite soeur de Link ? 🟢",
                            "Dans Wind Waker, sur quel île ne se trouve pas de blob bleu ? 🔴",
                            "Dans Wind Waker (NGC), comment obtient-on la plus grande barre de magie ? 🟠",
                            "Dans Wind Waker (NGC), où obtient-on la voile rapide ? 🟢",
                            "Dans Wind Waker HD, où obtient-on la voile rapide ? 🟢",
                            "Dans Breath of the Wild, combien existe-t-il de catégories différentes de flèches ? 🟠",
                            "Dans Super Smash Bros Ultimate, combien il y a-t-il de Link ? 🟠",
                            "Dans Super Smash Bros Ultimate, combien il y a-t-il de personnages de Zelda ? 🟠",
                            "Dans Breath of the Wild, que trouve-t-on dans le coffre de fin des labyrinthes d'Edale ? 🟠",
                            "Dans Breath of the Wild, quel est le pouvoir le plus rapide à se charger ? 🟠",
                            "Dans Breath of the Wild, quel est le pouvoir le plus long à se charger ? 🟠",
                            "Dans quel Zelda apparaît le boss Odolwa ? 🟢",
                            "Dans quel Zelda apparaît le boss Kaskhirma ? 🟠",
                            "Hyrule Warriors fait suite à quel jeu Zelda ? 🟢",
                            "Combien de morceaux de miroir sont à récupérer dans Twilight Princess ? 🟠",
                            "Combien de souvenirs peut-on trouver dans Breath of the Wild (Sans DLC) ? 🟠",
                            "Dans quel Zelda peut-on entendre le Totoka's song ? 🔴",
                            "En combien de temps a été développé Zelda Majora's Mask ? 🔴",
                            "Comment Fay appelle-t-elle le robot Récupix ? 🔴",
                            "Dans la Raffinerie de Skyward Sword, que voit-on sur un tableau sur un mur ? 🔴",
                            "Combien existe-t-il de jeux Tingle ? 🟠",
                            "Dans Twilight Princess, combien il y a-t-il de quart de coeurs ? 🟠",
                            "Dans Twilight Princess, comment se nomme le deuxième boss du jeu ? 🟠",
                            "Dans Twilight Princess, la première phase du boss final c'est... 🟢",
                            "Dans Twilight Princess, où se déroule la troisième phase du boss final ? 🟢",
                            "En quelle année est sortie Twilight Princess HD ? 🟠",
                            "Dans Twilight Princess HD, où peut-on trouver le tampon de Midona Surprise ? 🔴",
                            "Dans Twilight Princess, en quoi Link peut se transformer ? 🟢",
                            "Comment s'appelle la fée qui nous suit dans Phantom Hourglass ? 🟢",
                            "Dans Phantom Hourglass, quel est le nom du marin qui nous accompagne ? 🟢",
                            "Dans Phantom Hourglass, combien il y a-t-il d'îles ? 🔴",
                            "Dans Breath of the Wild, combien il y a-t-il de Korogu ? 🟢",
                            "Dans A Link Between Worlds, combien il y a-t-il de Ti'Gornaux ? 🟠",
                            "Que dit la princesse Hilda à chaque fois que l'on arrive dans une nouvelle contrée de Lorule ? 🔴",
                            "Dans A Link Between Worlds, comment se prénomme la jeune sorcière qui décide de veiller sur toi ? 🟠",
                            "Dans Wind Waker, quel est le boss à battre pour obtenir la perle de Nayru ? 🟠",
                            "Dans Wind Waker, comment s'appelle la soeur de Link ? 🟢",
                            "Dans Breath of the Wild, la monture alpha est-elle enregistrable ? 🟠",
                            "Dans Wind Waker HD, peut-on avoir une photo de Jabu Jabu ? 🟠",
                            "Parmi cette liste, quel personnage n'existe pas ? 🔴",
                            "Parmi cette liste, quel boss n'existe pas ? 🔴",
                            "Dans Breath of the Wild, que peut-on trouver sur la tour Sylvestre ? 🟠",
                            "Dans Ocarina of Time, Malon porte un médaillon, à quoi ressemble-t-il ? 🟠"]

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
                           16 : ["1️⃣ Au Nord du village des Animaux", "2️⃣ A l'Est du village des Mouettes", "3️⃣ Au Sud de l'Abîme du poisson", "4️⃣ Dans le plateau Tartare Ouest"],
                           17 : ["1️⃣ Ganondorf", "2️⃣ Roi Cuirasse", "3️⃣ Tetra", "4️⃣ Des pirates"],
                           18 : ["1️⃣ L'île étoilée", "2️⃣ L'île du croissant", "3️⃣ L'île de la rocaille", "4️⃣ L'île de Link"],
                           19 : ["1️⃣ Grâce à une grande fée", "2️⃣ Grâce à une quête secondaire", "3️⃣ En éliminant un Kalamar", "4️⃣ Grâce à Tingle"],
                           20 : ["1️⃣En l'achetant en magasin", "2️⃣ En gagnant aux enchères", "3️⃣ En battant un boss", "4️⃣ Il n'y en a pas"],
                           21 : ["1️⃣En l'achetant en magasin", "2️⃣ En gagnant aux enchères", "3️⃣ En battant un boss", "4️⃣ Il n'y en a pas"],
                           22 : ["1️⃣ 6", "2️⃣ 5", "3️⃣ 7", "4️⃣ 4"],
                           23 : ["1️⃣ 4", "2️⃣ 3", "3️⃣ 1", "4️⃣ 5"],
                           24 : ["1️⃣ 5", "2️⃣ 4", "3️⃣ 6", "4️⃣ 7"],
                           25 : ["1️⃣ La tenue barbare", "2️⃣ La tenue isolante", "3️⃣ La tenue nox", "4️⃣ La tenue archéonique"],
                           26 : ["1️⃣ Le pouvoir de Mipha", "2️⃣ Le pouvoir de Revali", "3️⃣ Le pouvoir de Urbosa", "4️⃣ Le pouvoir de Daruk"],
                           27 : ["1️⃣ Le pouvoir de Daruk", "2️⃣ Le pouvoir de Revali", "3️⃣ Le pouvoir de Urbosa", "4️⃣ Le pouvoir de Mipha"],
                           28 : ["1️⃣ Majora's Mask", "2️⃣ Twilight Princess", "3️⃣ Oracle of Seasons", "4️⃣ Aucun d'entre eux"],
                           29 : ["1️⃣ Oracle of Ages", "2️⃣ Oracle of Seasons", "3️⃣Four Sword Adventures", "4️⃣ Aucun d'entre eux"],
                           30 : ["1️⃣ Breath of the Wild", "2️⃣ Ocarina of Time", "3️⃣ Twilight Princess", "4️⃣ Aucun jeu"],
                           31 : ["1️⃣ 2", "2️⃣ 4", "3️⃣ 3", "4️⃣ 5"],
                           32 : ["1️⃣ 12", "2️⃣ 13", "3️⃣ 14", "4️⃣ 15"],
                           33 : ["1️⃣ The Adventure of Link", "2️⃣ Oracle of Ages", "3️⃣ Link's Awakening", "4️⃣ A Link Between Worlds"],
                           34 : ["1️⃣ 1 an et 5 mois", "2️⃣ 2 ans et 6 mois", "3️⃣ 1 an et 2 mois", "4️⃣ 2 ans et 1 mois"],
                           35 : ["1️⃣ Par ondes spirituelles", "2️⃣ Par télépathie", "3️⃣ Par ondes psychiques", "4️⃣ Par message"],
                           36 : ["1️⃣ Un schéma de la salle aux tapis roulants", "2️⃣ 3 petits robots", "3️⃣ 2 statues Armos", "4️⃣ Une photo de robot"],
                           37 : ["1️⃣ 2","2️⃣ 3","3️⃣ 4","4️⃣ 5"],
                           38 : ["1️⃣ 46", "2️⃣ 38", "3️⃣ 50", "4️⃣ 0"],
                           39 : ["1️⃣ Magolor", "2️⃣ Magmaudit", "3️⃣ Magrock", "4️⃣ Magmalor"],
                           40 : ["1️⃣ Le combat contre Zelda", "2️⃣ Le combat contre Ganon", "3️⃣ Le combat à cheval", "4️⃣ Le combat contre Ganondorf"],
                           41 : ["1️⃣ Dans le château d'Hyrule", "2️⃣ Dans la plaine d'Hyrule", "3️⃣ Dans Toal", "4️⃣ Au crépuscule"],
                           42 : ["1️⃣ 2014", "2️⃣ 2015", "3️⃣ 2016", "4️⃣ 2017"],
                           43 : ["1️⃣ Dans le palais du Crépuscule", "2️⃣ Dans la tour du jugement", "3️⃣ Dans le Désert Gerudo", "4️⃣ La rivière Zora"],
                           44 : ["1️⃣ En lapin", "2️⃣ En lion", "3️⃣ En loup", "4️⃣ En chien"],
                           45 : ["1️⃣ Navi", "2️⃣ Taya", "3️⃣ Proxie", "4️⃣ Ciela"],
                           46 : ["1️⃣ Bellum", "2️⃣ Linebeck", "3️⃣ Martin", "4️⃣ Hergo"],
                           47 : ["1️⃣ 14", "2️⃣ 15", "3️⃣ 16", "4️⃣ 17"],
                           48 : ["1️⃣ 900", "2️⃣ 800", "3️⃣ 950", "4️⃣ 1000"],
                           49 : ["1️⃣ 50", "2️⃣ 80", "3️⃣ 90", "4️⃣ 100"],
                           50 : ["1️⃣ Je t'en supplie, sauve Lorule", "2️⃣ Sais-tu où se trouve le lapin ?", "3️⃣ N'oublie pas, je suis Hilda de Lorule", "4️⃣ Je suis Hilda"],
                           51 : ["1️⃣ Aëline", "2️⃣ Maple", "3️⃣ Syrup", "4️⃣ Sabrina"],
                           52 : ["1️⃣ Jabu Jabu", "2️⃣ Goldias", "3️⃣ La bâteau fantome", "4️⃣ Aucun"],
                           53 : ["1️⃣ Ariel", "2️⃣ Anna", "3️⃣ Tetra", "4️⃣ Iria"],
                           54 : ["1️⃣ Oui, dans un relais spécifique", "2️⃣ Oui, mais si on a déjà attrapé 10 chevaux", "3️⃣ Oui, avec un amiibo", "4️⃣ Non"],
                           55 : ["1️⃣ Oui, en le prenant en photo au moment opportun", "2️⃣ Oui, en l'achetant", "3️⃣ Oui, en l'obtenant sur une île", "4️⃣ Non"],
                           56 : ["1️⃣ Bill les Mains d'Or", "2️⃣ Henriko", "3️⃣ Martha", "4️⃣ Monique la Lunatique"],
                           57 : ["1️⃣ Armoghoma", "2️⃣ Eyesoar", "3️⃣ Malkanadus", "4️⃣ Manhandla"],
                           58 : ["1️⃣ Un espadon royal", "2️⃣ Un coffre", "3️⃣ Une épée de chevalier", "4️⃣ Rien"],
                           59 : ["1️⃣ À la Triforce", "2️⃣ À son père", "3️⃣ À un Goron", "4️⃣ À Bowser"]}

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
                               "1️⃣ Au Nord du village des Animaux",
                               "2️⃣ Roi Cuirasse",
                               "4️⃣ L'île de Link",
                               "3️⃣ En éliminant un Kalamar",
                               "4️⃣ Il n'y en a pas",
                               "2️⃣ En gagnant aux enchères",
                               "1️⃣ 6",
                               "2️⃣ 3",
                               "3️⃣ 6",
                               "1️⃣ La tenue barbare",
                               "2️⃣ Le pouvoir de Revali",
                               "4️⃣ Le pouvoir de Mipha",
                               "1️⃣ Majora's Mask",
                               "4️⃣ Aucun d'entre eux",
                               "4️⃣ Aucun jeu",
                               "3️⃣ 3",
                               "2️⃣ 13",
                               "3️⃣ Link's Awakening",
                               "1️⃣ 1 an et 5 mois",
                               "3️⃣ Par ondes psychiques",
                               "2️⃣ 3 petits robots",
                               "3️⃣ 4",
                               "4️⃣ 0",
                               "2️⃣ Magmaudit",
                               "1️⃣ Le combat contre Zelda",
                               "2️⃣ Dans la plaine d'Hyrule",
                               "3️⃣ 2016",
                               "2️⃣ Dans la tour du jugement",
                               "3️⃣ En loup",
                               "4️⃣ Ciela",
                               "2️⃣ Linebeck",
                               "3️⃣ 16",
                               "1️⃣ 900",
                               "4️⃣ 100",
                               "3️⃣ N'oublie pas, je suis Hilda de Lorule",
                               "1️⃣ Aëline",
                               "4️⃣ Aucun",
                               "1️⃣ Ariel",
                               "4️⃣ Non",
                               "2️⃣ Oui, en l'achetant",
                               "2️⃣ Henriko",
                               "3️⃣ Malkanadus",
                               "1️⃣ Un espadon royal",
                               "4️⃣ À Bowser"]

        self.__tab = ['1️⃣' , '2️⃣', '3️⃣', '4️⃣', '❌']
        self.__lancer = False
        self.place = 0
        self.quizzEnCours = False

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

    def setQuizzEnCours(self, boolean):
        assert boolean in [True,False]
        self.quizzEnCours = boolean

    def getQuizzEnCours(self):
        return self.quizzEnCours



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