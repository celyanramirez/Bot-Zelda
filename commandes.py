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
                            "Dans Ocarina of Time, Malon porte un médaillon, à quoi ressemble-t-il ? 🔴",
                            "Dans Majora's Mask, combien de masque change votre corps/apparence ? 🟠",
                            "Dans Majora's Mask, qu'est-ce que les aliens veulent enlever au Ranch ? 🟢",
                            "Dans Four Swords, qu'est-ce qui se passe au tout début du jeu ? 🟢",
                            "Dans Link's Awakening HD, combien il y a-t-il de figurine Mario ? 🔴",
                            "Dans Ocarina of Time, quel est le nom de ton premier ocarina ? 🟢",
                            "Dans Majora's Mask, quelle potion doit-on donner à Koume pour qu'elle se sente mieux ? 🟢",
                            "Dans Breath of the Wild, quel module obtient-on dans le premier sanctuaire ? 🟢",
                            "Dans Breath of the Wild, combien il y a-t-il de prodiges ? 🟢",
                            "Dans Twiligt Princess, quel est le surnom du premier boss, Dionéa ? 🔴",
                            "Dans Skyward Sword, le célestrier de Link est appelé... 🟠",
                            "Dans quel jeu Tingle fait-il sa première apparition ? 🟢",
                            "Parmi ces jeux, quel est celui où le bateau est notre moyen de locomotion principal ? 🟢",
                            "Dans Ocarina of Time, qu'est-ce qui se trouve en réalité dans le puit de Cocorico ? 🟢",
                            "Dans Breath of the Wild, combien il y a-t-il de sanctuaire (hors DLC) ? 🟢",
                            "Dans Breath of the Wild, combien il y a-t-il de sanctuaire (DLC inclus) ? 🔴",
                            "Dans Majora's Mask, que gagnons-nous en arrivant premier à la course Goron ? 🟠",
                            "Dans Breath of the Wild, où se trouve le bouclier d'Hylia ? 🟠",
                            "Dans combien de jeu TLOZ Ganondorf/Ganon n'est pas le vilain principal ? 🔴"]

        self.__reponses = {0 : ["🇦 OOT", "🇧 ALTTP", "🇨 ALBW", "🇩 LA"],
                           1 : ["🇦 Link", "🇧 Zelda", "🇨 Tingle", "🇩 Linkle"],
                           2 : ["🇦 Tour du Jugement", "🇧 Château des Pics Blancs", "🇨 Célestia", "🇩 Ruines des Pics Blancs"],
                           3 : ["🇦 Timeline de la défaite", "🇧 Timeline de l'enfance", "🇨 Timeline de Link Adulte", "🇩 Début de la légende"],
                           4 : ["🇦 Romanie","🇧 Melodie", "🇨 Elwing", "🇩 Medolie"],
                           5 : ["🇦 1986", "🇧 1987", "🇨 1985", "🇩 1988"],
                           6 : ["🇦 1999", "🇧 1989", "🇨 2003", "🇩 2001"],
                           7 : ["🇦 Août 2015", "🇧 Janvier 2016", "🇨 Octobre 2015", "🇩 Novembre 2015"],
                           8 : ["🇦 SS-MC-FS-OOT", "🇧 SS-FS-MC-OOT", "🇨 SS-OOT-MC-FS", "🇩 SS-OOT-FS-MC"],
                           9 : ["🇦 A l'Ouest de Bourg-Clocher", "🇧 A l'Est de Bourg-Clocher", "🇨 Derrière la tour de l'Horloge", "🇩 Devant la tour de l'Horloge"],
                           10 : ["🇦 7", "🇧 6", "🇨 8", "🇩 5"],
                           11 : ["🇦 45", "🇧 49", "🇨 50", "🇩 38"],
                           12 : ["🇦 Par un Zora", "🇧 Dans un donjon", "🇨 Par un Goron", "🇩 Par un marchand"],
                           13 : ["🇦 Gu'Achitoh", "🇧 Moa'Kishito", "🇨 Ma'Ohnu", "🇩 Shora'Ha"],
                           14 : ["🇦 Lanelle", "🇧 Ordin", "🇨 Latouane", "🇩 Firone"],
                           15 : ["🇦 Satoru Iwata", "🇧 Minako Hamano", "🇨 Kazumi Totaka", "🇩 Shigefumi Hino"],
                           16 : ["🇦 Au Nord du village des Animaux", "🇧 A l'Est du village des Mouettes", "🇨 Au Sud de l'Abîme du poisson", "🇩 Dans le plateau Tartare Ouest"],
                           17 : ["🇦 Ganondorf", "🇧 Roi Cuirasse", "🇨 Tetra", "🇩 Des pirates"],
                           18 : ["🇦 L'île étoilée", "🇧 L'île du croissant", "🇨 L'île de la rocaille", "🇩 L'île de Link"],
                           19 : ["🇦 Grâce à une grande fée", "🇧 Grâce à une quête secondaire", "🇨 En éliminant un Kalamar", "🇩 Grâce à Tingle"],
                           20 : ["🇦En l'achetant en magasin", "🇧 En gagnant aux enchères", "🇨 En battant un boss", "🇩 Il n'y en a pas"],
                           21 : ["🇦En l'achetant en magasin", "🇧 En gagnant aux enchères", "🇨 En battant un boss", "🇩 Il n'y en a pas"],
                           22 : ["🇦 6", "🇧 5", "🇨 7", "🇩 4"],
                           23 : ["🇦 4", "🇧 3", "🇨 1", "🇩 5"],
                           24 : ["🇦 5", "🇧 4", "🇨 6", "🇩 7"],
                           25 : ["🇦 La tenue barbare", "🇧 La tenue isolante", "🇨 La tenue nox", "🇩 La tenue archéonique"],
                           26 : ["🇦 Le pouvoir de Mipha", "🇧 Le pouvoir de Revali", "🇨 Le pouvoir de Urbosa", "🇩 Le pouvoir de Daruk"],
                           27 : ["🇦 Le pouvoir de Daruk", "🇧 Le pouvoir de Revali", "🇨 Le pouvoir de Urbosa", "🇩 Le pouvoir de Mipha"],
                           28 : ["🇦 Majora's Mask", "🇧 Twilight Princess", "🇨 Oracle of Seasons", "🇩 Aucun d'entre eux"],
                           29 : ["🇦 Oracle of Ages", "🇧 Oracle of Seasons", "🇨Four Sword Adventures", "🇩 Aucun d'entre eux"],
                           30 : ["🇦 Breath of the Wild", "🇧 Ocarina of Time", "🇨 Twilight Princess", "🇩 Aucun jeu"],
                           31 : ["🇦 2", "🇧 4", "🇨 3", "🇩 5"],
                           32 : ["🇦 12", "🇧 13", "🇨 14", "🇩 15"],
                           33 : ["🇦 The Adventure of Link", "🇧 Oracle of Ages", "🇨 Link's Awakening", "🇩 A Link Between Worlds"],
                           34 : ["🇦 1 an et 5 mois", "🇧 2 ans et 6 mois", "🇨 1 an et 2 mois", "🇩 2 ans et 1 mois"],
                           35 : ["🇦 Par ondes spirituelles", "🇧 Par télépathie", "🇨 Par ondes psychiques", "🇩 Par message"],
                           36 : ["🇦 Un schéma de la salle aux tapis roulants", "🇧 3 petits robots", "🇨 2 statues Armos", "🇩 Une photo de robot"],
                           37 : ["🇦 2","🇧 3","🇨 4","🇩 5"],
                           38 : ["🇦 46", "🇧 38", "🇨 50", "🇩 0"],
                           39 : ["🇦 Magolor", "🇧 Magmaudit", "🇨 Magrock", "🇩 Magmalor"],
                           40 : ["🇦 Le combat contre Zelda", "🇧 Le combat contre Ganon", "🇨 Le combat à cheval", "🇩 Le combat contre Ganondorf"],
                           41 : ["🇦 Dans le château d'Hyrule", "🇧 Dans la plaine d'Hyrule", "🇨 Dans Toal", "🇩 Au crépuscule"],
                           42 : ["🇦 2014", "🇧 2015", "🇨 2016", "🇩 2017"],
                           43 : ["🇦 Dans le palais du Crépuscule", "🇧 Dans la tour du jugement", "🇨 Dans le Désert Gerudo", "🇩 La rivière Zora"],
                           44 : ["🇦 En lapin", "🇧 En lion", "🇨 En loup", "🇩 En chien"],
                           45 : ["🇦 Navi", "🇧 Taya", "🇨 Proxie", "🇩 Ciela"],
                           46 : ["🇦 Bellum", "🇧 Linebeck", "🇨 Martin", "🇩 Hergo"],
                           47 : ["🇦 14", "🇧 15", "🇨 16", "🇩 17"],
                           48 : ["🇦 900", "🇧 800", "🇨 950", "🇩 1000"],
                           49 : ["🇦 50", "🇧 80", "🇨 90", "🇩 100"],
                           50 : ["🇦 Je t'en supplie, sauve Lorule", "🇧 Sais-tu où se trouve le lapin ?", "🇨 N'oublie pas, je suis Hilda de Lorule", "🇩 Je suis Hilda"],
                           51 : ["🇦 Aëline", "🇧 Maple", "🇨 Syrup", "🇩 Sabrina"],
                           52 : ["🇦 Jabu Jabu", "🇧 Goldias", "🇨 La bâteau fantome", "🇩 Aucun"],
                           53 : ["🇦 Ariel", "🇧 Anna", "🇨 Tetra", "🇩 Iria"],
                           54 : ["🇦 Oui, dans un relais spécifique", "🇧 Oui, mais si on a déjà attrapé 10 chevaux", "🇨 Oui, avec un amiibo", "🇩 Non"],
                           55 : ["🇦 Oui, en le prenant en photo au moment opportun", "🇧 Oui, en l'achetant", "🇨 Oui, en l'obtenant sur une île", "🇩 Non"],
                           56 : ["🇦 Bill les Mains d'Or", "🇧 Henriko", "🇨 Martha", "🇩 Monique la Lunatique"],
                           57 : ["🇦 Armoghoma", "🇧 Eyesoar", "🇨 Malkanadus", "🇩 Manhandla"],
                           58 : ["🇦 Un espadon royal", "🇧 Un coffre", "🇨 Une épée de chevalier", "🇩 Rien"],
                           59 : ["🇦 À la Triforce", "🇧 À son père", "🇨 À un Goron", "🇩 À Bowser"],
                           60 : ["🇦 3", "🇧 4", "🇨 5", "🇩 6"],
                           61 : ["🇦 Les habitants", "🇧 Du lait", "🇨 Romani", "🇩 Les vaches"],
                           62 : ["🇦 Des bandits s'introduisent dans une maison", "🇧 Zelda est capturée par Vaati", "🇨 Link est mangé par Vaati", "🇩 Link dort"],
                           63 : ["🇦 8", "🇧 10", "🇨 12", "🇩 15"],
                           64 : ["🇦 L'Ocarina", "🇧 L'Ocarina des Fées", "🇨 L'Ocarina de Saria","🇩 L'Ocarina du Temps"],
                           65 : ["🇦 Potion rouge", "🇧 Potion verte", "🇨 Potion bleue", "🇩 Potion jaune"],
                           66 : ["🇦 Polaris", "🇧 Cryonis", "🇨 Cinétis", "🇩 Bombes à distance"],
                           67 : ["🇦 2", "🇧 3", "🇨 4","🇩 5"],
                           68 : ["🇦 Parasyte du Crépuscule", "🇧 Mauvaise herbe du Crépuscule", "🇨 Créature maléfique du Crépuscule", "🇩 Plante Crépusculaire"],
                           69 : ["🇦 Célestrier rouge", "🇧 Célestrier Vermeil", "🇨 Célestrier Vermeille", "🇩 Célestrier Merveille"],
                           70 : ["🇦 Dans A Link to The Past", "🇧 Dans Ocarina of Time", "🇨 Dans Majora's Mask", "🇩 Dans Wind Waker"],
                           71 : ["🇦 Wind Waker", "🇧 Minish Cap","🇨 Breath of the Wild", "🇩 Spirit Traks"],
                           72 : ["🇦 Un coffre", "🇧 Un quart de coeur", "🇨 Un donjon", "🇩 Un mort"],
                           73 : ["🇦 100", "🇧 95", "🇨 125", "🇩 120"],
                           74 : ["🇦 128", "🇧 135", "🇨 136", "🇩 130"],
                           75 : ["🇦 De la poudre dorée", "🇧 Une épée améliorée", "🇨 Le Monocle de Vérité", "🇩 Un quart de coeur"],
                           76 : ["🇦 Au pied d'un dragon", "🇧 Dans les chambres du château d'Hyrule", "🇨 Dans les geôles du château d'Hyrule", "🇩 Au sommet du château d'Hyrule"],
                           77 : ["🇦 8", "🇧 9", "🇨 10", "🇩 11"]}
                           
        self.__bonneReponse = ["🇧 ALTTP",
                               "🇦 Link",
                               "🇩 Ruines des Pics Blancs",
                               "🇦 Timeline de la défaite",
                               "🇩 Medolie",
                               "🇧 1987",
                               "🇩 2001",
                               "🇨 Octobre 2015",
                               "🇦 SS-MC-FS-OOT",
                               "🇨 Derrière la tour de l'Horloge",
                               "🇦 7",
                               "🇧 49",
                               "🇨 Par un Goron",
                               "🇨 Ma'Ohnu",
                               "🇨 Latouane",
                               "🇧 Minako Hamano",
                               "🇦 Au Nord du village des Animaux",
                               "🇧 Roi Cuirasse",
                               "🇩 L'île de Link",
                               "🇨 En éliminant un Kalamar",
                               "🇩 Il n'y en a pas",
                               "🇧 En gagnant aux enchères",
                               "🇦 6",
                               "🇧 3",
                               "🇨 6",
                               "🇦 La tenue barbare",
                               "🇧 Le pouvoir de Revali",
                               "🇩 Le pouvoir de Mipha",
                               "🇦 Majora's Mask",
                               "🇩 Aucun d'entre eux",
                               "🇩 Aucun jeu",
                               "🇨 3",
                               "🇧 13",
                               "🇨 Link's Awakening",
                               "🇦 1 an et 5 mois",
                               "🇨 Par ondes psychiques",
                               "🇧 3 petits robots",
                               "🇨 4",
                               "🇩 0",
                               "🇧 Magmaudit",
                               "🇦 Le combat contre Zelda",
                               "🇧 Dans la plaine d'Hyrule",
                               "🇨 2016",
                               "🇧 Dans la tour du jugement",
                               "🇨 En loup",
                               "🇩 Ciela",
                               "🇧 Linebeck",
                               "🇨 16",
                               "🇦 900",
                               "🇩 100",
                               "🇨 N'oublie pas, je suis Hilda de Lorule",
                               "🇦 Aëline",
                               "🇩 Aucun",
                               "🇦 Ariel",
                               "🇩 Non",
                               "🇧 Oui, en l'achetant",
                               "🇧 Henriko",
                               "🇨 Malkanadus",
                               "🇦 Un espadon royal",
                               "🇩 À Bowser",
                               "🇨 5",
                               "🇩 Les vaches",
                               "🇧 Zelda est capturée par Vaati",
                               "🇧 10",
                               "🇧 L'Ocarina des Fées",
                               "🇦 Potion rouge",
                               "🇦 Polaris",
                               "🇩 5",
                               "🇧 Mauvaise herbe du Crépuscule",
                               "🇧 Célestrier Vermeil",
                               "🇨 Dans Majora's Mask",
                               "🇦 Wind Waker",
                               "🇨 Un donjon",
                               "🇩 120",
                               "🇨 136",
                               "🇦 De la poudre dorée",
                               "🇨 Dans les geôles du château d'Hyrule",
                               "🇨 10"]

        self.__tab = ['🇦' , '🇧', '🇨', '🇩', '❌']
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
        self.aPerduPoint = False

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
    
    def ajouterJoueursId(self, id:int):
        self.tabJoueursId.append(id)


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