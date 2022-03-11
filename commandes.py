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
                            "Dans Ocarina of Time, Malon porte un médaillon, à quoi ressemble-t-il ? 🟠",
                            "Dans Majora's Mask, combien de masque change votre corps/apparence ? 🟠",
                            "Dans Majora's Mask, qu'est-ce que les aliens veulent enlever au Ranch ? 🟢",
                            "Dans Four Swords, qu'est-ce qui se passe au tout début du jeu ? 🟢",
                            "Dans Link's Awakening HD, combien il y a-t-il de figurine Mario ? 🔴"]

        self.__reponses = {0 : ["<:AAA:949033966848049223> OOT", "<:BBB:949032944134148176> ALTTP", "<:CCC:949032944121573467> ALBW", "<:DDD:949032944125747279> LA"],
                           1 : ["<:AAA:949033966848049223> Link", "<:BBB:949032944134148176> Zelda", "<:CCC:949032944121573467> Tingle", "<:DDD:949032944125747279> Linkle"],
                           2 : ["<:AAA:949033966848049223> Tour du Jugement", "<:BBB:949032944134148176> Château des Pics Blancs", "<:CCC:949032944121573467> Célestia", "<:DDD:949032944125747279> Ruines des Pics Blancs"],
                           3 : ["<:AAA:949033966848049223> Timeline de la défaite", "<:BBB:949032944134148176> Timeline de l'enfance", "<:CCC:949032944121573467> Timeline de Link Adulte", "<:DDD:949032944125747279> Début de la légende"],
                           4 : ["<:AAA:949033966848049223> Romanie","<:BBB:949032944134148176> Melodie", "<:CCC:949032944121573467> Elwing", "<:DDD:949032944125747279> Medolie"],
                           5 : ["<:AAA:949033966848049223> 1986", "<:BBB:949032944134148176> 1987", "<:CCC:949032944121573467> 1985", "<:DDD:949032944125747279> 1988"],
                           6 : ["<:AAA:949033966848049223> 1999", "<:BBB:949032944134148176> 1989", "<:CCC:949032944121573467> 2003", "<:DDD:949032944125747279> 2001"],
                           7 : ["<:AAA:949033966848049223> Août 2015", "<:BBB:949032944134148176> Janvier 2016", "<:CCC:949032944121573467> Octobre 2015", "<:DDD:949032944125747279> Novembre 2015"],
                           8 : ["<:AAA:949033966848049223> SS-MC-FS-OOT", "<:BBB:949032944134148176> SS-FS-MC-OOT", "<:CCC:949032944121573467> SS-OOT-MC-FS", "<:DDD:949032944125747279> SS-OOT-FS-MC"],
                           9 : ["<:AAA:949033966848049223> A l'Ouest de Bourg-Clocher", "<:BBB:949032944134148176> A l'Est de Bourg-Clocher", "<:CCC:949032944121573467> Derrière la tour de l'Horloge", "<:DDD:949032944125747279> Devant la tour de l'Horloge"],
                           10 : ["<:AAA:949033966848049223> 7", "<:BBB:949032944134148176> 6", "<:CCC:949032944121573467> 8", "<:DDD:949032944125747279> 5"],
                           11 : ["<:AAA:949033966848049223> 45", "<:BBB:949032944134148176> 49", "<:CCC:949032944121573467> 50", "<:DDD:949032944125747279> 38"],
                           12 : ["<:AAA:949033966848049223> Par un Zora", "<:BBB:949032944134148176> Dans un donjon", "<:CCC:949032944121573467> Par un Goron", "<:DDD:949032944125747279> Par un marchand"],
                           13 : ["<:AAA:949033966848049223> Gu'Achitoh", "<:BBB:949032944134148176> Moa'Kishito", "<:CCC:949032944121573467> Ma'Ohnu", "<:DDD:949032944125747279> Shora'Ha"],
                           14 : ["<:AAA:949033966848049223> Lanelle", "<:BBB:949032944134148176> Ordin", "<:CCC:949032944121573467> Latouane", "<:DDD:949032944125747279> Firone"],
                           15 : ["<:AAA:949033966848049223> Satoru Iwata", "<:BBB:949032944134148176> Minako Hamano", "<:CCC:949032944121573467> Kazumi Totaka", "<:DDD:949032944125747279> Shigefumi Hino"],
                           16 : ["<:AAA:949033966848049223> Au Nord du village des Animaux", "<:BBB:949032944134148176> A l'Est du village des Mouettes", "<:CCC:949032944121573467> Au Sud de l'Abîme du poisson", "<:DDD:949032944125747279> Dans le plateau Tartare Ouest"],
                           17 : ["<:AAA:949033966848049223> Ganondorf", "<:BBB:949032944134148176> Roi Cuirasse", "<:CCC:949032944121573467> Tetra", "<:DDD:949032944125747279> Des pirates"],
                           18 : ["<:AAA:949033966848049223> L'île étoilée", "<:BBB:949032944134148176> L'île du croissant", "<:CCC:949032944121573467> L'île de la rocaille", "<:DDD:949032944125747279> L'île de Link"],
                           19 : ["<:AAA:949033966848049223> Grâce à une grande fée", "<:BBB:949032944134148176> Grâce à une quête secondaire", "<:CCC:949032944121573467> En éliminant un Kalamar", "<:DDD:949032944125747279> Grâce à Tingle"],
                           20 : ["<:AAA:949033966848049223>En l'achetant en magasin", "<:BBB:949032944134148176> En gagnant aux enchères", "<:CCC:949032944121573467> En battant un boss", "<:DDD:949032944125747279> Il n'y en a pas"],
                           21 : ["<:AAA:949033966848049223>En l'achetant en magasin", "<:BBB:949032944134148176> En gagnant aux enchères", "<:CCC:949032944121573467> En battant un boss", "<:DDD:949032944125747279> Il n'y en a pas"],
                           22 : ["<:AAA:949033966848049223> 6", "<:BBB:949032944134148176> 5", "<:CCC:949032944121573467> 7", "<:DDD:949032944125747279> 4"],
                           23 : ["<:AAA:949033966848049223> 4", "<:BBB:949032944134148176> 3", "<:CCC:949032944121573467> 1", "<:DDD:949032944125747279> 5"],
                           24 : ["<:AAA:949033966848049223> 5", "<:BBB:949032944134148176> 4", "<:CCC:949032944121573467> 6", "<:DDD:949032944125747279> 7"],
                           25 : ["<:AAA:949033966848049223> La tenue barbare", "<:BBB:949032944134148176> La tenue isolante", "<:CCC:949032944121573467> La tenue nox", "<:DDD:949032944125747279> La tenue archéonique"],
                           26 : ["<:AAA:949033966848049223> Le pouvoir de Mipha", "<:BBB:949032944134148176> Le pouvoir de Revali", "<:CCC:949032944121573467> Le pouvoir de Urbosa", "<:DDD:949032944125747279> Le pouvoir de Daruk"],
                           27 : ["<:AAA:949033966848049223> Le pouvoir de Daruk", "<:BBB:949032944134148176> Le pouvoir de Revali", "<:CCC:949032944121573467> Le pouvoir de Urbosa", "<:DDD:949032944125747279> Le pouvoir de Mipha"],
                           28 : ["<:AAA:949033966848049223> Majora's Mask", "<:BBB:949032944134148176> Twilight Princess", "<:CCC:949032944121573467> Oracle of Seasons", "<:DDD:949032944125747279> Aucun d'entre eux"],
                           29 : ["<:AAA:949033966848049223> Oracle of Ages", "<:BBB:949032944134148176> Oracle of Seasons", "<:CCC:949032944121573467>Four Sword Adventures", "<:DDD:949032944125747279> Aucun d'entre eux"],
                           30 : ["<:AAA:949033966848049223> Breath of the Wild", "<:BBB:949032944134148176> Ocarina of Time", "<:CCC:949032944121573467> Twilight Princess", "<:DDD:949032944125747279> Aucun jeu"],
                           31 : ["<:AAA:949033966848049223> 2", "<:BBB:949032944134148176> 4", "<:CCC:949032944121573467> 3", "<:DDD:949032944125747279> 5"],
                           32 : ["<:AAA:949033966848049223> 12", "<:BBB:949032944134148176> 13", "<:CCC:949032944121573467> 14", "<:DDD:949032944125747279> 15"],
                           33 : ["<:AAA:949033966848049223> The Adventure of Link", "<:BBB:949032944134148176> Oracle of Ages", "<:CCC:949032944121573467> Link's Awakening", "<:DDD:949032944125747279> A Link Between Worlds"],
                           34 : ["<:AAA:949033966848049223> 1 an et 5 mois", "<:BBB:949032944134148176> 2 ans et 6 mois", "<:CCC:949032944121573467> 1 an et 2 mois", "<:DDD:949032944125747279> 2 ans et 1 mois"],
                           35 : ["<:AAA:949033966848049223> Par ondes spirituelles", "<:BBB:949032944134148176> Par télépathie", "<:CCC:949032944121573467> Par ondes psychiques", "<:DDD:949032944125747279> Par message"],
                           36 : ["<:AAA:949033966848049223> Un schéma de la salle aux tapis roulants", "<:BBB:949032944134148176> 3 petits robots", "<:CCC:949032944121573467> 2 statues Armos", "<:DDD:949032944125747279> Une photo de robot"],
                           37 : ["<:AAA:949033966848049223> 2","<:BBB:949032944134148176> 3","<:CCC:949032944121573467> 4","<:DDD:949032944125747279> 5"],
                           38 : ["<:AAA:949033966848049223> 46", "<:BBB:949032944134148176> 38", "<:CCC:949032944121573467> 50", "<:DDD:949032944125747279> 0"],
                           39 : ["<:AAA:949033966848049223> Magolor", "<:BBB:949032944134148176> Magmaudit", "<:CCC:949032944121573467> Magrock", "<:DDD:949032944125747279> Magmalor"],
                           40 : ["<:AAA:949033966848049223> Le combat contre Zelda", "<:BBB:949032944134148176> Le combat contre Ganon", "<:CCC:949032944121573467> Le combat à cheval", "<:DDD:949032944125747279> Le combat contre Ganondorf"],
                           41 : ["<:AAA:949033966848049223> Dans le château d'Hyrule", "<:BBB:949032944134148176> Dans la plaine d'Hyrule", "<:CCC:949032944121573467> Dans Toal", "<:DDD:949032944125747279> Au crépuscule"],
                           42 : ["<:AAA:949033966848049223> 2014", "<:BBB:949032944134148176> 2015", "<:CCC:949032944121573467> 2016", "<:DDD:949032944125747279> 2017"],
                           43 : ["<:AAA:949033966848049223> Dans le palais du Crépuscule", "<:BBB:949032944134148176> Dans la tour du jugement", "<:CCC:949032944121573467> Dans le Désert Gerudo", "<:DDD:949032944125747279> La rivière Zora"],
                           44 : ["<:AAA:949033966848049223> En lapin", "<:BBB:949032944134148176> En lion", "<:CCC:949032944121573467> En loup", "<:DDD:949032944125747279> En chien"],
                           45 : ["<:AAA:949033966848049223> Navi", "<:BBB:949032944134148176> Taya", "<:CCC:949032944121573467> Proxie", "<:DDD:949032944125747279> Ciela"],
                           46 : ["<:AAA:949033966848049223> Bellum", "<:BBB:949032944134148176> Linebeck", "<:CCC:949032944121573467> Martin", "<:DDD:949032944125747279> Hergo"],
                           47 : ["<:AAA:949033966848049223> 14", "<:BBB:949032944134148176> 15", "<:CCC:949032944121573467> 16", "<:DDD:949032944125747279> 17"],
                           48 : ["<:AAA:949033966848049223> 900", "<:BBB:949032944134148176> 800", "<:CCC:949032944121573467> 950", "<:DDD:949032944125747279> 1000"],
                           49 : ["<:AAA:949033966848049223> 50", "<:BBB:949032944134148176> 80", "<:CCC:949032944121573467> 90", "<:DDD:949032944125747279> 100"],
                           50 : ["<:AAA:949033966848049223> Je t'en supplie, sauve Lorule", "<:BBB:949032944134148176> Sais-tu où se trouve le lapin ?", "<:CCC:949032944121573467> N'oublie pas, je suis Hilda de Lorule", "<:DDD:949032944125747279> Je suis Hilda"],
                           51 : ["<:AAA:949033966848049223> Aëline", "<:BBB:949032944134148176> Maple", "<:CCC:949032944121573467> Syrup", "<:DDD:949032944125747279> Sabrina"],
                           52 : ["<:AAA:949033966848049223> Jabu Jabu", "<:BBB:949032944134148176> Goldias", "<:CCC:949032944121573467> La bâteau fantome", "<:DDD:949032944125747279> Aucun"],
                           53 : ["<:AAA:949033966848049223> Ariel", "<:BBB:949032944134148176> Anna", "<:CCC:949032944121573467> Tetra", "<:DDD:949032944125747279> Iria"],
                           54 : ["<:AAA:949033966848049223> Oui, dans un relais spécifique", "<:BBB:949032944134148176> Oui, mais si on a déjà attrapé 10 chevaux", "<:CCC:949032944121573467> Oui, avec un amiibo", "<:DDD:949032944125747279> Non"],
                           55 : ["<:AAA:949033966848049223> Oui, en le prenant en photo au moment opportun", "<:BBB:949032944134148176> Oui, en l'achetant", "<:CCC:949032944121573467> Oui, en l'obtenant sur une île", "<:DDD:949032944125747279> Non"],
                           56 : ["<:AAA:949033966848049223> Bill les Mains d'Or", "<:BBB:949032944134148176> Henriko", "<:CCC:949032944121573467> Martha", "<:DDD:949032944125747279> Monique la Lunatique"],
                           57 : ["<:AAA:949033966848049223> Armoghoma", "<:BBB:949032944134148176> Eyesoar", "<:CCC:949032944121573467> Malkanadus", "<:DDD:949032944125747279> Manhandla"],
                           58 : ["<:AAA:949033966848049223> Un espadon royal", "<:BBB:949032944134148176> Un coffre", "<:CCC:949032944121573467> Une épée de chevalier", "<:DDD:949032944125747279> Rien"],
                           59 : ["<:AAA:949033966848049223> À la Triforce", "<:BBB:949032944134148176> À son père", "<:CCC:949032944121573467> À un Goron", "<:DDD:949032944125747279> À Bowser"],
                           60 : ["<:AAA:949033966848049223> 3", "<:BBB:949032944134148176> 4", "<:CCC:949032944121573467> 5", "<:DDD:949032944125747279> 6"],
                           61 : ["<:AAA:949033966848049223> Les habitants", "<:BBB:949032944134148176> Du lait", "<:CCC:949032944121573467> Romani", "<:DDD:949032944125747279> Les vaches"],
                           62 : ["<:AAA:949033966848049223> Des bandits s'introduisent dans une maison", "<:BBB:949032944134148176> Zelda est capturée par Vaati", "<:CCC:949032944121573467> Link est mangé par Vaati", "<:DDD:949032944125747279> Link dort"],
                           63 : ["<:AAA:949033966848049223> 8", "<:BBB:949032944134148176> 10", "<:CCC:949032944121573467> 12", "<:DDD:949032944125747279> 15"]}

        self.__bonneReponse = ["<:BBB:949032944134148176> ALTTP",
                               "<:AAA:949033966848049223> Link",
                               "<:DDD:949032944125747279> Ruines des Pics Blancs",
                               "<:AAA:949033966848049223> Timeline de la défaite",
                               "<:DDD:949032944125747279> Medolie",
                               "<:BBB:949032944134148176> 1987",
                               "<:DDD:949032944125747279> 2001",
                               "<:CCC:949032944121573467> Octobre 2015",
                               "<:AAA:949033966848049223> SS-MC-FS-OOT",
                               "<:CCC:949032944121573467> Derrière la tour de l'Horloge",
                               "<:AAA:949033966848049223> 7",
                               "<:BBB:949032944134148176> 49",
                               "<:CCC:949032944121573467> Par un Goron",
                               "<:CCC:949032944121573467> Ma'Ohnu",
                               "<:CCC:949032944121573467> Latouane",
                               "<:BBB:949032944134148176> Minako Hamano",
                               "<:AAA:949033966848049223> Au Nord du village des Animaux",
                               "<:BBB:949032944134148176> Roi Cuirasse",
                               "<:DDD:949032944125747279> L'île de Link",
                               "<:CCC:949032944121573467> En éliminant un Kalamar",
                               "<:DDD:949032944125747279> Il n'y en a pas",
                               "<:BBB:949032944134148176> En gagnant aux enchères",
                               "<:AAA:949033966848049223> 6",
                               "<:BBB:949032944134148176> 3",
                               "<:CCC:949032944121573467> 6",
                               "<:AAA:949033966848049223> La tenue barbare",
                               "<:BBB:949032944134148176> Le pouvoir de Revali",
                               "<:DDD:949032944125747279> Le pouvoir de Mipha",
                               "<:AAA:949033966848049223> Majora's Mask",
                               "<:DDD:949032944125747279> Aucun d'entre eux",
                               "<:DDD:949032944125747279> Aucun jeu",
                               "<:CCC:949032944121573467> 3",
                               "<:BBB:949032944134148176> 13",
                               "<:CCC:949032944121573467> Link's Awakening",
                               "<:AAA:949033966848049223> 1 an et 5 mois",
                               "<:CCC:949032944121573467> Par ondes psychiques",
                               "<:BBB:949032944134148176> 3 petits robots",
                               "<:CCC:949032944121573467> 4",
                               "<:DDD:949032944125747279> 0",
                               "<:BBB:949032944134148176> Magmaudit",
                               "<:AAA:949033966848049223> Le combat contre Zelda",
                               "<:BBB:949032944134148176> Dans la plaine d'Hyrule",
                               "<:CCC:949032944121573467> 2016",
                               "<:BBB:949032944134148176> Dans la tour du jugement",
                               "<:CCC:949032944121573467> En loup",
                               "<:DDD:949032944125747279> Ciela",
                               "<:BBB:949032944134148176> Linebeck",
                               "<:CCC:949032944121573467> 16",
                               "<:AAA:949033966848049223> 900",
                               "<:DDD:949032944125747279> 100",
                               "<:CCC:949032944121573467> N'oublie pas, je suis Hilda de Lorule",
                               "<:AAA:949033966848049223> Aëline",
                               "<:DDD:949032944125747279> Aucun",
                               "<:AAA:949033966848049223> Ariel",
                               "<:DDD:949032944125747279> Non",
                               "<:BBB:949032944134148176> Oui, en l'achetant",
                               "<:BBB:949032944134148176> Henriko",
                               "<:CCC:949032944121573467> Malkanadus",
                               "<:AAA:949033966848049223> Un espadon royal",
                               "<:DDD:949032944125747279> À Bowser",
                               "<:CCC:949032944121573467> 5",
                               "<:DDD:949032944125747279> Les vaches",
                               "<:BBB:949032944134148176> Zelda est capturée par Vaati",
                               "<:BBB:949032944134148176> 10"]

        self.__tab = ['<:AAA:949033966848049223>' , '<:BBB:949032944134148176>', '<:CCC:949032944121573467>', '<:DDD:949032944125747279>', '❌']
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