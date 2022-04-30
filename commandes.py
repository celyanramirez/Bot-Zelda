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
                            "Dans combien de jeu TLOZ Ganondorf/Ganon n'est pas le vilain principal ? 🔴",
                            "Dans Zelda I, le vieux monsieur vous donne au début du jeu... 🟢",
                            "De quel jeu Zelda vient cette phrase mythique : 'It's dangerous to go alone, take this !' 🟢",
                            "Dans Breath of the Wild, où sont situé les fameux 'Spectacle Rock', rochers emblématiques de la saga ? 🔴",
                            "Parmi ces items, lequel est achetable chez Terry dans Skyward Sword ? 🔴",
                            "Parmi ces instruments, duquel d'entre eux ne s'est jamais servi Link ? 🟠",
                            "Dans lequel de ces opus notre héros ne voyage-t-il pas dans les cieux ? 🟠",
                            "Dans la chronologie OFFICIELLE Zelda, à partir dequel jeu celle-ci se divise en plusieurs partie ? 🟢",
                            "Dans la chronologie OFFICIELLE Zelda, quel jeu clôture la timeline de l'enfance ? 🟠",
                            "Comment s'appelle le monde où se déroule Link's Awakening ? 🟢",
                            "Dans Link's Awakening, quel animal dit à Link de réveiller le Poisson Rêve ? 🟠",
                            "Dans lequel de ces jeux Link n'apparaît pas ? 🔴",
                            "Combien il y a-t-il de grenouilles dorées dans Phantom Hourglass ? 🔴",
                            "Dans Phantom Hourglass, combien il y a-t-il de type d'équipements de bateau ? (Ex : Démon, Or...) 🔴",
                            "Dans Zelda II, où peut-on trouver les bottes permettant de marcher sur l'eau ? 🔴",
                            "Dans Zelda II, qui est le boss final ? 🟠",
                            "Dans Triforce Heroes, quel est le nom du boss du Temple du Désert ? 🔴",
                            "Combien il y a-t-il de mondes différents dans Triforce Heroes ? 🟠",
                            "Dans Triforce Heroes, quelle est la tunique renforçant l'arc ? 🟠",
                            "Dans Majora's Mask, qui représente le Masque Mojo ? 🟠",
                            "Dans Majora's Mask 3D, quel est l'objet principal pour effectuer le bug du 4ème jour ? 🔴",
                            "Dans Majora's Mask, pourquoi Lulu a-t-elle perdu sa voix ? 🟢",
                            "Dans Ocarina of Time, quel est le premier donjon du jeu ? 🟢"]

        self.__reponses = {0 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  OOT", "<:BB:946480160763437056> <:STX1:946414240699408466>  ALTTP", "<:CC:946480160922828850> <:STX1:946414240699408466>  ALBW", "<:DD:946480161304506428> <:STX1:946414240699408466>  LA"],
                           1 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  Link", "<:BB:946480160763437056> <:STX1:946414240699408466>  Zelda", "<:CC:946480160922828850> <:STX1:946414240699408466>  Tingle", "<:DD:946480161304506428> <:STX1:946414240699408466>  Linkle"],
                           2 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  Tour du Jugement", "<:BB:946480160763437056> <:STX1:946414240699408466>  Château des Pics Blancs", "<:CC:946480160922828850> <:STX1:946414240699408466>  Célestia", "<:DD:946480161304506428> <:STX1:946414240699408466>  Ruines des Pics Blancs"],
                           3 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  Timeline de la défaite", "<:BB:946480160763437056> <:STX1:946414240699408466>  Timeline de l'enfance", "<:CC:946480160922828850> <:STX1:946414240699408466>  Timeline de Link Adulte", "<:DD:946480161304506428> <:STX1:946414240699408466>  Début de la légende"],
                           4 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  Romanie","<:BB:946480160763437056> <:STX1:946414240699408466>  Melodie", "<:CC:946480160922828850> <:STX1:946414240699408466>  Elwing", "<:DD:946480161304506428> <:STX1:946414240699408466>  Medolie"],
                           5 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  1986", "<:BB:946480160763437056> <:STX1:946414240699408466>  1987", "<:CC:946480160922828850> <:STX1:946414240699408466>  1985", "<:DD:946480161304506428> <:STX1:946414240699408466>  1988"],
                           6 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  1999", "<:BB:946480160763437056> <:STX1:946414240699408466>  1989", "<:CC:946480160922828850> <:STX1:946414240699408466>  2003", "<:DD:946480161304506428> <:STX1:946414240699408466>  2001"],
                           7 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  Août 2015", "<:BB:946480160763437056> <:STX1:946414240699408466>  Janvier 2016", "<:CC:946480160922828850> <:STX1:946414240699408466>  Octobre 2015", "<:DD:946480161304506428> <:STX1:946414240699408466>  Novembre 2015"],
                           8 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  SS-MC-FS-OOT", "<:BB:946480160763437056> <:STX1:946414240699408466>  SS-FS-MC-OOT", "<:CC:946480160922828850> <:STX1:946414240699408466>  SS-OOT-MC-FS", "<:DD:946480161304506428> <:STX1:946414240699408466>  SS-OOT-FS-MC"],
                           9 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  A l'Ouest de Bourg-Clocher", "<:BB:946480160763437056> <:STX1:946414240699408466>  A l'Est de Bourg-Clocher", "<:CC:946480160922828850> <:STX1:946414240699408466>  Derrière la tour de l'Horloge", "<:DD:946480161304506428> <:STX1:946414240699408466>  Devant la tour de l'Horloge"],
                           10 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  7", "<:BB:946480160763437056> <:STX1:946414240699408466>  6", "<:CC:946480160922828850> <:STX1:946414240699408466>  8", "<:DD:946480161304506428> <:STX1:946414240699408466>  5"],
                           11 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  45", "<:BB:946480160763437056> <:STX1:946414240699408466>  49", "<:CC:946480160922828850> <:STX1:946414240699408466>  50", "<:DD:946480161304506428> <:STX1:946414240699408466>  38"],
                           12 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  Par un Zora", "<:BB:946480160763437056> <:STX1:946414240699408466>  Dans un donjon", "<:CC:946480160922828850> <:STX1:946414240699408466>  Par un Goron", "<:DD:946480161304506428> <:STX1:946414240699408466>  Par un marchand"],
                           13 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  Gu'Achitoh", "<:BB:946480160763437056> <:STX1:946414240699408466>  Moa'Kishito", "<:CC:946480160922828850> <:STX1:946414240699408466>  Ma'Ohnu", "<:DD:946480161304506428> <:STX1:946414240699408466>  Shora'Ha"],
                           14 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  Lanelle", "<:BB:946480160763437056> <:STX1:946414240699408466>  Ordin", "<:CC:946480160922828850> <:STX1:946414240699408466>  Latouane", "<:DD:946480161304506428> <:STX1:946414240699408466>  Firone"],
                           15 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  Satoru Iwata", "<:BB:946480160763437056> <:STX1:946414240699408466>  Minako Hamano", "<:CC:946480160922828850> <:STX1:946414240699408466>  Kazumi Totaka", "<:DD:946480161304506428> <:STX1:946414240699408466>  Shigefumi Hino"],
                           16 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  Au Nord du village des Animaux", "<:BB:946480160763437056> <:STX1:946414240699408466>  A l'Est du village des Mouettes", "<:CC:946480160922828850> <:STX1:946414240699408466>  Au Sud de l'Abîme du poisson", "<:DD:946480161304506428> <:STX1:946414240699408466>  Dans le plateau Tartare Ouest"],
                           17 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  Ganondorf", "<:BB:946480160763437056> <:STX1:946414240699408466>  Roi Cuirasse", "<:CC:946480160922828850> <:STX1:946414240699408466>  Tetra", "<:DD:946480161304506428> <:STX1:946414240699408466>  Des pirates"],
                           18 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  L'île étoilée", "<:BB:946480160763437056> <:STX1:946414240699408466>  L'île du croissant", "<:CC:946480160922828850> <:STX1:946414240699408466>  L'île de la rocaille", "<:DD:946480161304506428> <:STX1:946414240699408466>  L'île de Link"],
                           19 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  Grâce à une grande fée", "<:BB:946480160763437056> <:STX1:946414240699408466>  Grâce à une quête secondaire", "<:CC:946480160922828850> <:STX1:946414240699408466>  En éliminant un Kalamar", "<:DD:946480161304506428> <:STX1:946414240699408466>  Grâce à Tingle"],
                           20 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  En l'achetant en magasin", "<:BB:946480160763437056> <:STX1:946414240699408466>  En gagnant aux enchères", "<:CC:946480160922828850> <:STX1:946414240699408466>  En battant un boss", "<:DD:946480161304506428> <:STX1:946414240699408466>  Il n'y en a pas"],
                           21 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  En l'achetant en magasin", "<:BB:946480160763437056> <:STX1:946414240699408466>  En gagnant aux enchères", "<:CC:946480160922828850> <:STX1:946414240699408466>  En battant un boss", "<:DD:946480161304506428> <:STX1:946414240699408466>  Il n'y en a pas"],
                           22 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  6", "<:BB:946480160763437056> <:STX1:946414240699408466>  5", "<:CC:946480160922828850> <:STX1:946414240699408466>  7", "<:DD:946480161304506428> <:STX1:946414240699408466>  4"],
                           23 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  4", "<:BB:946480160763437056> <:STX1:946414240699408466>  3", "<:CC:946480160922828850> <:STX1:946414240699408466>  1", "<:DD:946480161304506428> <:STX1:946414240699408466>  5"],
                           24 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  5", "<:BB:946480160763437056> <:STX1:946414240699408466>  4", "<:CC:946480160922828850> <:STX1:946414240699408466>  6", "<:DD:946480161304506428> <:STX1:946414240699408466>  7"],
                           25 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  La tenue barbare", "<:BB:946480160763437056> <:STX1:946414240699408466>  La tenue isolante", "<:CC:946480160922828850> <:STX1:946414240699408466>  La tenue nox", "<:DD:946480161304506428> <:STX1:946414240699408466>  La tenue archéonique"],
                           26 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  Le pouvoir de Mipha", "<:BB:946480160763437056> <:STX1:946414240699408466>  Le pouvoir de Revali", "<:CC:946480160922828850> <:STX1:946414240699408466>  Le pouvoir de Urbosa", "<:DD:946480161304506428> <:STX1:946414240699408466>  Le pouvoir de Daruk"],
                           27 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  Le pouvoir de Daruk", "<:BB:946480160763437056> <:STX1:946414240699408466>  Le pouvoir de Revali", "<:CC:946480160922828850> <:STX1:946414240699408466>  Le pouvoir de Urbosa", "<:DD:946480161304506428> <:STX1:946414240699408466>  Le pouvoir de Mipha"],
                           28 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  Majora's Mask", "<:BB:946480160763437056> <:STX1:946414240699408466>  Twilight Princess", "<:CC:946480160922828850> <:STX1:946414240699408466>  Oracle of Seasons", "<:DD:946480161304506428> <:STX1:946414240699408466>  Aucun d'entre eux"],
                           29 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  Oracle of Ages", "<:BB:946480160763437056> <:STX1:946414240699408466>  Oracle of Seasons", "<:CC:946480160922828850> <:STX1:946414240699408466> Four Sword Adventures", "<:DD:946480161304506428> <:STX1:946414240699408466>  Aucun d'entre eux"],
                           30 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  Breath of the Wild", "<:BB:946480160763437056> <:STX1:946414240699408466>  Ocarina of Time", "<:CC:946480160922828850> <:STX1:946414240699408466>  Twilight Princess", "<:DD:946480161304506428> <:STX1:946414240699408466>  Aucun jeu"],
                           31 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  2", "<:BB:946480160763437056> <:STX1:946414240699408466>  4", "<:CC:946480160922828850> <:STX1:946414240699408466>  3", "<:DD:946480161304506428> <:STX1:946414240699408466>  5"],
                           32 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  12", "<:BB:946480160763437056> <:STX1:946414240699408466>  13", "<:CC:946480160922828850> <:STX1:946414240699408466>  14", "<:DD:946480161304506428> <:STX1:946414240699408466>  15"],
                           33 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  The Adventure of Link", "<:BB:946480160763437056> <:STX1:946414240699408466>  Oracle of Ages", "<:CC:946480160922828850> <:STX1:946414240699408466>  Link's Awakening", "<:DD:946480161304506428> <:STX1:946414240699408466>  A Link Between Worlds"],
                           34 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  1 an et 5 mois", "<:BB:946480160763437056> <:STX1:946414240699408466>  2 ans et 6 mois", "<:CC:946480160922828850> <:STX1:946414240699408466>  1 an et 2 mois", "<:DD:946480161304506428> <:STX1:946414240699408466>  2 ans et 1 mois"],
                           35 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  Par ondes spirituelles", "<:BB:946480160763437056> <:STX1:946414240699408466>  Par télépathie", "<:CC:946480160922828850> <:STX1:946414240699408466>  Par ondes psychiques", "<:DD:946480161304506428> <:STX1:946414240699408466>  Par message"],
                           36 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  Un schéma de la salle aux tapis roulants", "<:BB:946480160763437056> <:STX1:946414240699408466>  3 petits robots", "<:CC:946480160922828850> <:STX1:946414240699408466>  2 statues Armos", "<:DD:946480161304506428> <:STX1:946414240699408466>  Une photo de robot"],
                           37 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  2","<:BB:946480160763437056> <:STX1:946414240699408466>  3","<:CC:946480160922828850> <:STX1:946414240699408466>  4","<:DD:946480161304506428> <:STX1:946414240699408466>  5"],
                           38 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  46", "<:BB:946480160763437056> <:STX1:946414240699408466>  38", "<:CC:946480160922828850> <:STX1:946414240699408466>  50", "<:DD:946480161304506428> <:STX1:946414240699408466>  0"],
                           39 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  Magolor", "<:BB:946480160763437056> <:STX1:946414240699408466>  Magmaudit", "<:CC:946480160922828850> <:STX1:946414240699408466>  Magrock", "<:DD:946480161304506428> <:STX1:946414240699408466>  Magmalor"],
                           40 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  Le combat contre Zelda", "<:BB:946480160763437056> <:STX1:946414240699408466>  Le combat contre Ganon", "<:CC:946480160922828850> <:STX1:946414240699408466>  Le combat à cheval", "<:DD:946480161304506428> <:STX1:946414240699408466>  Le combat contre Ganondorf"],
                           41 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  Dans le château d'Hyrule", "<:BB:946480160763437056> <:STX1:946414240699408466>  Dans la plaine d'Hyrule", "<:CC:946480160922828850> <:STX1:946414240699408466>  Dans Toal", "<:DD:946480161304506428> <:STX1:946414240699408466>  Au crépuscule"],
                           42 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  2014", "<:BB:946480160763437056> <:STX1:946414240699408466>  2015", "<:CC:946480160922828850> <:STX1:946414240699408466>  2016", "<:DD:946480161304506428> <:STX1:946414240699408466>  2017"],
                           43 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  Dans le palais du Crépuscule", "<:BB:946480160763437056> <:STX1:946414240699408466>  Dans la tour du jugement", "<:CC:946480160922828850> <:STX1:946414240699408466>  Dans le Désert Gerudo", "<:DD:946480161304506428> <:STX1:946414240699408466>  La rivière Zora"],
                           44 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  En lapin", "<:BB:946480160763437056> <:STX1:946414240699408466>  En lion", "<:CC:946480160922828850> <:STX1:946414240699408466>  En loup", "<:DD:946480161304506428> <:STX1:946414240699408466>  En chien"],
                           45 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  Navi", "<:BB:946480160763437056> <:STX1:946414240699408466>  Taya", "<:CC:946480160922828850> <:STX1:946414240699408466>  Proxie", "<:DD:946480161304506428> <:STX1:946414240699408466>  Ciela"],
                           46 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  Bellum", "<:BB:946480160763437056> <:STX1:946414240699408466>  Linebeck", "<:CC:946480160922828850> <:STX1:946414240699408466>  Martin", "<:DD:946480161304506428> <:STX1:946414240699408466>  Hergo"],
                           47 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  14", "<:BB:946480160763437056> <:STX1:946414240699408466>  15", "<:CC:946480160922828850> <:STX1:946414240699408466>  16", "<:DD:946480161304506428> <:STX1:946414240699408466>  17"],
                           48 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  900", "<:BB:946480160763437056> <:STX1:946414240699408466>  800", "<:CC:946480160922828850> <:STX1:946414240699408466>  950", "<:DD:946480161304506428> <:STX1:946414240699408466>  1000"],
                           49 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  50", "<:BB:946480160763437056> <:STX1:946414240699408466>  80", "<:CC:946480160922828850> <:STX1:946414240699408466>  90", "<:DD:946480161304506428> <:STX1:946414240699408466>  100"],
                           50 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  Je t'en supplie, sauve Lorule", "<:BB:946480160763437056> <:STX1:946414240699408466>  Sais-tu où se trouve le lapin ?", "<:CC:946480160922828850> <:STX1:946414240699408466>  N'oublie pas, je suis Hilda de Lorule", "<:DD:946480161304506428> <:STX1:946414240699408466>  Je suis Hilda"],
                           51 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  Aëline", "<:BB:946480160763437056> <:STX1:946414240699408466>  Maple", "<:CC:946480160922828850> <:STX1:946414240699408466>  Syrup", "<:DD:946480161304506428> <:STX1:946414240699408466>  Sabrina"],
                           52 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  Jabu Jabu", "<:BB:946480160763437056> <:STX1:946414240699408466>  Goldias", "<:CC:946480160922828850> <:STX1:946414240699408466>  La bâteau fantome", "<:DD:946480161304506428> <:STX1:946414240699408466>  Aucun"],
                           53 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  Ariel", "<:BB:946480160763437056> <:STX1:946414240699408466>  Anna", "<:CC:946480160922828850> <:STX1:946414240699408466>  Tetra", "<:DD:946480161304506428> <:STX1:946414240699408466>  Iria"],
                           54 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  Oui, dans un relais spécifique", "<:BB:946480160763437056> <:STX1:946414240699408466>  Oui, mais si on a déjà attrapé 10 chevaux", "<:CC:946480160922828850> <:STX1:946414240699408466>  Oui, avec un amiibo", "<:DD:946480161304506428> <:STX1:946414240699408466>  Non"],
                           55 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  Oui, en le prenant en photo au moment opportun", "<:BB:946480160763437056> <:STX1:946414240699408466>  Oui, en l'achetant", "<:CC:946480160922828850> <:STX1:946414240699408466>  Oui, en l'obtenant sur une île", "<:DD:946480161304506428> <:STX1:946414240699408466>  Non"],
                           56 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  Bill les Mains d'Or", "<:BB:946480160763437056> <:STX1:946414240699408466>  Henriko", "<:CC:946480160922828850> <:STX1:946414240699408466>  Martha", "<:DD:946480161304506428> <:STX1:946414240699408466>  Monique la Lunatique"],
                           57 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  Armoghoma", "<:BB:946480160763437056> <:STX1:946414240699408466>  Eyesoar", "<:CC:946480160922828850> <:STX1:946414240699408466>  Malkanadus", "<:DD:946480161304506428> <:STX1:946414240699408466>  Manhandla"],
                           58 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  Un espadon royal", "<:BB:946480160763437056> <:STX1:946414240699408466>  Un coffre", "<:CC:946480160922828850> <:STX1:946414240699408466>  Une épée de chevalier", "<:DD:946480161304506428> <:STX1:946414240699408466>  Rien"],
                           59 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  À la Triforce", "<:BB:946480160763437056> <:STX1:946414240699408466>  À son père", "<:CC:946480160922828850> <:STX1:946414240699408466>  À un Goron", "<:DD:946480161304506428> <:STX1:946414240699408466>  À Bowser"],
                           60 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  3", "<:BB:946480160763437056> <:STX1:946414240699408466>  4", "<:CC:946480160922828850> <:STX1:946414240699408466>  5", "<:DD:946480161304506428> <:STX1:946414240699408466>  6"],
                           61 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  Les habitants", "<:BB:946480160763437056> <:STX1:946414240699408466>  Du lait", "<:CC:946480160922828850> <:STX1:946414240699408466>  Romani", "<:DD:946480161304506428> <:STX1:946414240699408466>  Les vaches"],
                           62 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  Des bandits s'introduisent dans une maison", "<:BB:946480160763437056> <:STX1:946414240699408466>  Zelda est capturée par Vaati", "<:CC:946480160922828850> <:STX1:946414240699408466>  Link est mangé par Vaati", "<:DD:946480161304506428> <:STX1:946414240699408466>  Link dort"],
                           63 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  8", "<:BB:946480160763437056> <:STX1:946414240699408466>  10", "<:CC:946480160922828850> <:STX1:946414240699408466>  12", "<:DD:946480161304506428> <:STX1:946414240699408466>  15"],
                           64 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  L'Ocarina", "<:BB:946480160763437056> <:STX1:946414240699408466>  L'Ocarina des Fées", "<:CC:946480160922828850> <:STX1:946414240699408466>  L'Ocarina de Saria","<:DD:946480161304506428> <:STX1:946414240699408466>  L'Ocarina du Temps"],
                           65 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  Potion rouge", "<:BB:946480160763437056> <:STX1:946414240699408466>  Potion verte", "<:CC:946480160922828850> <:STX1:946414240699408466>  Potion bleue", "<:DD:946480161304506428> <:STX1:946414240699408466>  Potion jaune"],
                           66 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  Polaris", "<:BB:946480160763437056> <:STX1:946414240699408466>  Cryonis", "<:CC:946480160922828850> <:STX1:946414240699408466>  Cinétis", "<:DD:946480161304506428> <:STX1:946414240699408466>  Bombes à distance"],
                           67 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  2", "<:BB:946480160763437056> <:STX1:946414240699408466>  3", "<:CC:946480160922828850> <:STX1:946414240699408466>  4","<:DD:946480161304506428> <:STX1:946414240699408466>  5"],
                           68 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  Parasyte du Crépuscule", "<:BB:946480160763437056> <:STX1:946414240699408466>  Mauvaise herbe du Crépuscule", "<:CC:946480160922828850> <:STX1:946414240699408466>  Créature maléfique du Crépuscule", "<:DD:946480161304506428> <:STX1:946414240699408466>  Plante Crépusculaire"],
                           69 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  Célestrier rouge", "<:BB:946480160763437056> <:STX1:946414240699408466>  Célestrier Vermeil", "<:CC:946480160922828850> <:STX1:946414240699408466>  Célestrier Vermeille", "<:DD:946480161304506428> <:STX1:946414240699408466>  Célestrier Merveille"],
                           70 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  Dans A Link to The Past", "<:BB:946480160763437056> <:STX1:946414240699408466>  Dans Ocarina of Time", "<:CC:946480160922828850> <:STX1:946414240699408466>  Dans Majora's Mask", "<:DD:946480161304506428> <:STX1:946414240699408466>  Dans Wind Waker"],
                           71 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  Wind Waker", "<:BB:946480160763437056> <:STX1:946414240699408466>  Minish Cap","<:CC:946480160922828850> <:STX1:946414240699408466>  Breath of the Wild", "<:DD:946480161304506428> <:STX1:946414240699408466>  Spirit Traks"],
                           72 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  Un coffre", "<:BB:946480160763437056> <:STX1:946414240699408466>  Un quart de coeur", "<:CC:946480160922828850> <:STX1:946414240699408466>  Un donjon", "<:DD:946480161304506428> <:STX1:946414240699408466>  Un mort"],
                           73 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  100", "<:BB:946480160763437056> <:STX1:946414240699408466>  95", "<:CC:946480160922828850> <:STX1:946414240699408466>  125", "<:DD:946480161304506428> <:STX1:946414240699408466>  120"],
                           74 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  128", "<:BB:946480160763437056> <:STX1:946414240699408466>  135", "<:CC:946480160922828850> <:STX1:946414240699408466>  136", "<:DD:946480161304506428> <:STX1:946414240699408466>  130"],
                           75 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  De la poudre dorée", "<:BB:946480160763437056> <:STX1:946414240699408466>  Une épée améliorée", "<:CC:946480160922828850> <:STX1:946414240699408466>  Le Monocle de Vérité", "<:DD:946480161304506428> <:STX1:946414240699408466>  Un quart de coeur"],
                           76 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  Au pied d'un dragon", "<:BB:946480160763437056> <:STX1:946414240699408466>  Dans les chambres du château d'Hyrule", "<:CC:946480160922828850> <:STX1:946414240699408466>  Dans les geôles du château d'Hyrule", "<:DD:946480161304506428> <:STX1:946414240699408466>  Au sommet du château d'Hyrule"],
                           77 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  8", "<:BB:946480160763437056> <:STX1:946414240699408466>  9", "<:CC:946480160922828850> <:STX1:946414240699408466>  10", "<:DD:946480161304506428> <:STX1:946414240699408466>  11"],
                           78 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  Un conseil", "<:BB:946480160763437056> <:STX1:946414240699408466>  Un bouclier", "<:CC:946480160922828850> <:STX1:946414240699408466>  Une clé", "<:DD:946480161304506428> <:STX1:946414240699408466>  Une épée"],
                           79 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  Zelda I", "<:BB:946480160763437056> <:STX1:946414240699408466>  A Link to The Past", "<:CC:946480160922828850> <:STX1:946414240699408466>  Ocarina of Time", "<:DD:946480161304506428> <:STX1:946414240699408466>  Zelda II"],
                           80 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  Au plateau du Prélude", "<:BB:946480160763437056> <:STX1:946414240699408466>  Dans la région Gerudo", "<:CC:946480160922828850> <:STX1:946414240699408466>  Dans la région d'Akkala", "<:DD:946480161304506428> <:STX1:946414240699408466>  Dans la région d'Elimith"],
                           81 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  La Jar Magique", "<:BB:946480160763437056> <:STX1:946414240699408466>  Une bourse annexe (x3)", "<:CC:946480160922828850> <:STX1:946414240699408466>  Une médaille rubis", "<:DD:946480161304506428> <:STX1:946414240699408466>  Une bourse annexe (x2)"],
                           82 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  Le tambour", "<:BB:946480160763437056> <:STX1:946414240699408466>  La guitare", "<:CC:946480160922828850> <:STX1:946414240699408466>  La harpe", "<:DD:946480161304506428> <:STX1:946414240699408466>  La flûte à pan"],
                           83 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  Twilight Princess", "<:BB:946480160763437056> <:STX1:946414240699408466>  The Minish Cap", "<:CC:946480160922828850> <:STX1:946414240699408466>  Skyward Sword", "<:DD:946480161304506428> <:STX1:946414240699408466>  The Adventure of Link"],
                           84 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  The Minish Cap", "<:BB:946480160763437056> <:STX1:946414240699408466>  Ocarina of Time", "<:CC:946480160922828850> <:STX1:946414240699408466>  Twilight Princess", "<:DD:946480161304506428> <:STX1:946414240699408466>  Skyward Sword"],
                           85 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  Four Swords Adventures", "<:BB:946480160763437056> <:STX1:946414240699408466>  Majora's Mask", "<:CC:946480160922828850> <:STX1:946414240699408466>  Spirit Tracks", "<:DD:946480161304506428> <:STX1:946414240699408466>  Link's Awakening"],
                           86 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  Dreamworld", "<:BB:946480160763437056> <:STX1:946414240699408466>  Hyrule", "<:CC:946480160922828850> <:STX1:946414240699408466>  Termina", "<:DD:946480161304506428> <:STX1:946414240699408466>  Koholint Island"],
                           87 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  Un chien", "<:BB:946480160763437056> <:STX1:946414240699408466>  Un hibou", "<:CC:946480160922828850> <:STX1:946414240699408466>  Un poisson", "<:DD:946480161304506428> <:STX1:946414240699408466>  Un corbeau"],
                           88 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  Super Mario Maker 2", "<:BB:946480160763437056> <:STX1:946414240699408466>  Tingle's Rosy Rupeeland", "<:CC:946480160922828850> <:STX1:946414240699408466>  Soulcalibur II", "<:DD:946480161304506428> <:STX1:946414240699408466>  Mario Kart 8"],
                           89 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  6", "<:BB:946480160763437056> <:STX1:946414240699408466>  7", "<:CC:946480160922828850> <:STX1:946414240699408466>  5", "<:DD:946480161304506428> <:STX1:946414240699408466>  8"],
                           90 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  10", "<:BB:946480160763437056> <:STX1:946414240699408466>  8", "<:CC:946480160922828850> <:STX1:946414240699408466>  7", "<:DD:946480161304506428> <:STX1:946414240699408466>  9"],
                           91 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  Dans le Palais des Marais", "<:BB:946480160763437056> <:STX1:946414240699408466>  Dans le Palais du Labyrinthe", "<:CC:946480160922828850> <:STX1:946414240699408466>  Dans le Palais de l'Îlot", "<:DD:946480161304506428> <:STX1:946414240699408466>  Dans la ville cachée de Kasuto"],
                           92 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  Ganon", "<:BB:946480160763437056> <:STX1:946414240699408466>  Ganondorf", "<:CC:946480160922828850> <:STX1:946414240699408466>  Dark Link", "<:DD:946480161304506428> <:STX1:946414240699408466>  Thunderbird"],
                           93 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  Champion Stalfos", "<:BB:946480160763437056> <:STX1:946414240699408466>  Stalfos Bombardier", "<:CC:946480160922828850> <:STX1:946414240699408466>  Grand Stalfos", "<:DD:946480161304506428> <:STX1:946414240699408466>  Stalfos du Désert"],
                           94 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  8", "<:BB:946480160763437056> <:STX1:946414240699408466>  9", "<:CC:946480160922828850> <:STX1:946414240699408466>  7", "<:DD:946480161304506428> <:STX1:946414240699408466>  10"],
                           95 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  La Tenue Haute-coupure", "<:BB:946480160763437056> <:STX1:946414240699408466>  La Tenue de l'archer", "<:CC:946480160922828850> <:STX1:946414240699408466>  La Tenue verte", "<:DD:946480161304506428> <:STX1:946414240699408466>  La Tenue Kokiri"],
                           96 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  Le fils du Majordome", "<:BB:946480160763437056> <:STX1:946414240699408466>  Le fils du Roi Mojo", "<:CC:946480160922828850> <:STX1:946414240699408466>  Une peste Mojo quelconque", "<:DD:946480161304506428> <:STX1:946414240699408466>  La princesse Mojo"],
                           97 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  Le masque de Kafei", "<:BB:946480160763437056> <:STX1:946414240699408466>  L'arc", "<:CC:946480160922828850> <:STX1:946414240699408466>  Le masque de Gibdo", "<:DD:946480161304506428> <:STX1:946414240699408466>  Un flacon vide"],
                           98 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  Parce qu'elle s'inquiète pour Mikau", "<:BB:946480160763437056> <:STX1:946414240699408466>  Parce que ses oeufs ont été volé", "<:CC:946480160922828850> <:STX1:946414240699408466>  Parce qu'elle a trop mangé", "<:DD:946480161304506428> <:STX1:946414240699408466>  Parce qu'elle ne peut plus nager"],
                           99 : ["<:AA:946480160830554123> <:STX1:946414240699408466>  Jabu Jabu", "<:BB:946480160763437056> <:STX1:946414240699408466>  Le Temple de la forêt", "<:CC:946480160922828850> <:STX1:946414240699408466>  L'arbre Mojo", "<:DD:946480161304506428> <:STX1:946414240699408466>  La caverne Dodongo"]}
                           
        self.__bonneReponse = ["<:BB:946480160763437056> <:STX1:946414240699408466>  ALTTP",
                               "<:AA:946480160830554123> <:STX1:946414240699408466>  Link",
                               "<:DD:946480161304506428> <:STX1:946414240699408466>  Ruines des Pics Blancs",
                               "<:AA:946480160830554123> <:STX1:946414240699408466>  Timeline de la défaite",
                               "<:DD:946480161304506428> <:STX1:946414240699408466>  Medolie",
                               "<:BB:946480160763437056> <:STX1:946414240699408466>  1987",
                               "<:DD:946480161304506428> <:STX1:946414240699408466>  2001",
                               "<:CC:946480160922828850> <:STX1:946414240699408466>  Octobre 2015",
                               "<:AA:946480160830554123> <:STX1:946414240699408466>  SS-MC-FS-OOT",
                               "<:CC:946480160922828850> <:STX1:946414240699408466>  Derrière la tour de l'Horloge",
                               "<:AA:946480160830554123> <:STX1:946414240699408466>  7",
                               "<:BB:946480160763437056> <:STX1:946414240699408466>  49",
                               "<:CC:946480160922828850> <:STX1:946414240699408466>  Par un Goron",
                               "<:CC:946480160922828850> <:STX1:946414240699408466>  Ma'Ohnu",
                               "<:CC:946480160922828850> <:STX1:946414240699408466>  Latouane",
                               "<:BB:946480160763437056> <:STX1:946414240699408466>  Minako Hamano",
                               "<:AA:946480160830554123> <:STX1:946414240699408466>  Au Nord du village des Animaux",
                               "<:BB:946480160763437056> <:STX1:946414240699408466>  Roi Cuirasse",
                               "<:DD:946480161304506428> <:STX1:946414240699408466>  L'île de Link",
                               "<:CC:946480160922828850> <:STX1:946414240699408466>  En éliminant un Kalamar",
                               "<:DD:946480161304506428> <:STX1:946414240699408466>  Il n'y en a pas",
                               "<:BB:946480160763437056> <:STX1:946414240699408466>  En gagnant aux enchères",
                               "<:AA:946480160830554123> <:STX1:946414240699408466>  6",
                               "<:BB:946480160763437056> <:STX1:946414240699408466>  3",
                               "<:CC:946480160922828850> <:STX1:946414240699408466>  6",
                               "<:AA:946480160830554123> <:STX1:946414240699408466>  La tenue barbare",
                               "<:BB:946480160763437056> <:STX1:946414240699408466>  Le pouvoir de Revali",
                               "<:DD:946480161304506428> <:STX1:946414240699408466>  Le pouvoir de Mipha",
                               "<:AA:946480160830554123> <:STX1:946414240699408466>  Majora's Mask",
                               "<:DD:946480161304506428> <:STX1:946414240699408466>  Aucun d'entre eux",
                               "<:DD:946480161304506428> <:STX1:946414240699408466>  Aucun jeu",
                               "<:CC:946480160922828850> <:STX1:946414240699408466>  3",
                               "<:BB:946480160763437056> <:STX1:946414240699408466>  13",
                               "<:CC:946480160922828850> <:STX1:946414240699408466>  Link's Awakening",
                               "<:AA:946480160830554123> <:STX1:946414240699408466>  1 an et 5 mois",
                               "<:CC:946480160922828850> <:STX1:946414240699408466>  Par ondes psychiques",
                               "<:BB:946480160763437056> <:STX1:946414240699408466>  3 petits robots",
                               "<:CC:946480160922828850> <:STX1:946414240699408466>  4",
                               "<:DD:946480161304506428> <:STX1:946414240699408466>  0",
                               "<:BB:946480160763437056> <:STX1:946414240699408466>  Magmaudit",
                               "<:AA:946480160830554123> <:STX1:946414240699408466>  Le combat contre Zelda",
                               "<:BB:946480160763437056> <:STX1:946414240699408466>  Dans la plaine d'Hyrule",
                               "<:CC:946480160922828850> <:STX1:946414240699408466>  2016",
                               "<:BB:946480160763437056> <:STX1:946414240699408466>  Dans la tour du jugement",
                               "<:CC:946480160922828850> <:STX1:946414240699408466>  En loup",
                               "<:DD:946480161304506428> <:STX1:946414240699408466>  Ciela",
                               "<:BB:946480160763437056> <:STX1:946414240699408466>  Linebeck",
                               "<:CC:946480160922828850> <:STX1:946414240699408466>  16",
                               "<:AA:946480160830554123> <:STX1:946414240699408466>  900",
                               "<:DD:946480161304506428> <:STX1:946414240699408466>  100",
                               "<:CC:946480160922828850> <:STX1:946414240699408466>  N'oublie pas, je suis Hilda de Lorule",
                               "<:AA:946480160830554123> <:STX1:946414240699408466>  Aëline",
                               "<:DD:946480161304506428> <:STX1:946414240699408466>  Aucun",
                               "<:AA:946480160830554123> <:STX1:946414240699408466>  Ariel",
                               "<:DD:946480161304506428> <:STX1:946414240699408466>  Non",
                               "<:BB:946480160763437056> <:STX1:946414240699408466>  Oui, en l'achetant",
                               "<:BB:946480160763437056> <:STX1:946414240699408466>  Henriko",
                               "<:CC:946480160922828850> <:STX1:946414240699408466>  Malkanadus",
                               "<:AA:946480160830554123> <:STX1:946414240699408466>  Un espadon royal",
                               "<:DD:946480161304506428> <:STX1:946414240699408466>  À Bowser",
                               "<:CC:946480160922828850> <:STX1:946414240699408466>  5",
                               "<:DD:946480161304506428> <:STX1:946414240699408466>  Les vaches",
                               "<:BB:946480160763437056> <:STX1:946414240699408466>  Zelda est capturée par Vaati",
                               "<:BB:946480160763437056> <:STX1:946414240699408466>  10",
                               "<:BB:946480160763437056> <:STX1:946414240699408466>  L'Ocarina des Fées",
                               "<:AA:946480160830554123> <:STX1:946414240699408466>  Potion rouge",
                               "<:AA:946480160830554123> <:STX1:946414240699408466>  Polaris",
                               "<:DD:946480161304506428> <:STX1:946414240699408466>  5",
                               "<:BB:946480160763437056> <:STX1:946414240699408466>  Mauvaise herbe du Crépuscule",
                               "<:BB:946480160763437056> <:STX1:946414240699408466>  Célestrier Vermeil",
                               "<:CC:946480160922828850> <:STX1:946414240699408466>  Dans Majora's Mask",
                               "<:AA:946480160830554123> <:STX1:946414240699408466>  Wind Waker",
                               "<:CC:946480160922828850> <:STX1:946414240699408466>  Un donjon",
                               "<:DD:946480161304506428> <:STX1:946414240699408466>  120",
                               "<:CC:946480160922828850> <:STX1:946414240699408466>  136",
                               "<:AA:946480160830554123> <:STX1:946414240699408466>  De la poudre dorée",
                               "<:CC:946480160922828850> <:STX1:946414240699408466>  Dans les geôles du château d'Hyrule",
                               "<:CC:946480160922828850> <:STX1:946414240699408466>  10",
                               "<:DD:946480161304506428> <:STX1:946414240699408466>  Une épée",
                               "<:AA:946480160830554123> <:STX1:946414240699408466>  Zelda I",
                               "<:BB:946480160763437056> <:STX1:946414240699408466>  Dans la région Gerudo",
                               "<:BB:946480160763437056> <:STX1:946414240699408466>  Une bourse annexe (x3)",
                               "<:CC:946480160922828850> <:STX1:946414240699408466>  La harpe",
                               "<:DD:946480161304506428> <:STX1:946414240699408466>  The Adventure of Link",
                               "<:BB:946480160763437056> <:STX1:946414240699408466>  Ocarina of Time",
                               "<:AA:946480160830554123> <:STX1:946414240699408466>  Four Swords Adventures",
                               "<:DD:946480161304506428> <:STX1:946414240699408466>  Koholint Island",
                               "<:BB:946480160763437056> <:STX1:946414240699408466>  Un hibou",
                               "<:BB:946480160763437056> <:STX1:946414240699408466>  Tingle's Rosy Rupeeland",
                               "<:AA:946480160830554123> <:STX1:946414240699408466>  6",
                               "<:DD:946480161304506428> <:STX1:946414240699408466>  9",
                               "<:BB:946480160763437056> <:STX1:946414240699408466>  Dans le Palais du Labyrinthe",
                               "<:CC:946480160922828850> <:STX1:946414240699408466>  Dark Link",
                               "<:AA:946480160830554123> <:STX1:946414240699408466>  Champion Stalfos",
                               "<:BB:946480160763437056> <:STX1:946414240699408466>  9",
                               "<:DD:946480161304506428> <:STX1:946414240699408466>  La Tenue Kokiri",
                               "<:AA:946480160830554123> <:STX1:946414240699408466>  Le fils du Majordome",
                               "<:CC:946480160922828850> <:STX1:946414240699408466>  Le masque de Gibdo",
                               "<:BB:946480160763437056> <:STX1:946414240699408466>  Parce que ses oeufs ont été volé",
                               "<:CC:946480160922828850> <:STX1:946414240699408466>  L'arbre Mojo"]

        self.__tab = ['<:AA:946480160830554123>' , '<:BB:946480160763437056>', '<:CC:946480160922828850>', '<:DD:946480161304506428>', '❌']
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
