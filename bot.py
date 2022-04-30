#from msilib.schema import Class
from cgi import test
from sqlite3 import Time
import string
from this import d
from typing import Any
import typing
from unittest import TestCase
import discord
import asyncio
import random
import time
from commandes import *
from discord.ext import commands
from discord_slash import ButtonStyle
from discord_slash.utils.manage_components import *
import ast

client = discord.Client()
disc = Botdisc()
q = Quizz()
cl = Classement()
bot = commands.Bot(command_prefix = '$', description = "")

listeZelda = ["-Zelda I\n"
"-Zelda II, The Adventure of Link\n"
"-The Legend of Zelda : A Link to the Past\n"
"-The Legend of Zelda : Link's Awakening (1993)\n"
"-The Legend of Zelda : Ocarina of Time (1998)\n"
"-The Legend of Zelda : Link's Awakening DX (1998)\n"
"-The Legend of Zelda : Majora's Mask (2000)\n"
"-The Legend of Zelda : Oracle of Seasons (2001)\n"
"-The Legend of Zelda : Oracle of Ages (2001)\n"
"-The Legend of Zelda : Four Swords (2002)\n"
"-The Legend of Zelda : The Wind Waker (2002)\n"
"-The Legend of Zelda : The Minish Cap (2004)\n"
"-The Legend of Zelda : Four Swords Adventures (2004)\n"
"-The Legend of Zelda : Twilight Princess (2006)\n"
"-The Legend of Zelda : Phantom Hourglass (2007)\n"
"-The Legend of Zelda : Spirit Tracks (2009)\n"
"-The Legend of Zelda : Ocarina of Time 3D (2011)\n"
"-The Legend of Zelda : Skyward Sword (2011)\n"
"-The Legend of Zelda : The Wind Waker HD (2013)\n"
"-The Legend of Zelda : A Link Between Worlds (2013)\n"
"-The Legend of Zelda : Triforces Heroes (2015)\n"
"-The Legend of Zelda : Majora's Mask 3D (2015)\n"
"-The Legend of Zelda : Twilight Princess HD (2016)\n"
"-The Legend of Zelda : Breath of the Wild (2017)\n"
"-The Legend of Zelda : Link's Awakening HD (2019)\n",
"-The Legend of Zelda : Sequel of the Wild (20XX)",
"-The Legend of Zelda : Skyward Sword HD (2021)"
]

questions = ["Qui est le perso principal de la saga Zelda ?", "Qui est la princesse ?"]
réponse = ["Link", "Zelda"]

def max(tab):
    maximum = 0
    for i in range(len(tab)):
        if tab[i]>maximum:
            maximum=i
    return maximum


@bot.event
async def on_ready():
    print("J'suis prêt !")

async def getMutedRole(ctx):
    roles = ctx.guild.roles
    for role in roles:
        if role.name == "MUTED":
            return role

async def getDeesseRole(ctx):
    roles = ctx.guild.roles
    for role in roles:
        if role.name == "Déesse":
            return role

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f"Vous ne pouvez pas utiliser cette commande.")

###############################################################################################

@bot.command()
@commands.has_permissions(kick_members = True)
async def clear(ctx, nb:int):
    await ctx.channel.purge(limit = nb)
    await ctx.send(f"**{nb} message(s)** ont été supprimés.")
    await asyncio.sleep(3)
    await ctx.channel.purge(limit = 1)

@bot.command()
@commands.has_permissions(kick_members = True) 
async def clearall(ctx):
    await ctx.send("Êtes vous sûr de vouloir supprimer tous les messages du channel ? (Irréversible !). Si oui, tapez $confirm")
    disc.garde = True            #Permet de ne pas pouvoir faire $confirm si $clearall n'a pas été lancé
    temps = 30
    sec = False             #Si sec est sur True, alors le chrono commence.           #Check si $confirm a été enclenché, si oui ça met fin à la boucle de messages.
    for i in range(temps):
        if sec == False:
            await ctx.send(f"Il vous reste {temps} secondes pour faire votre choix. Si vous ne voulez rien faire, attendez la fin.")
            sec = True
        elif disc.check == True:
            break
        elif temps == 0:
            await ctx.send("Temps écoulé.")
            disc.garde = False
            break
        elif sec == True:
            time.sleep(10)
            temps = temps - 10
            await ctx.send(f"Il vous reste {temps} secondes pour faire votre choix. Si vous ne voulez rien faire, attendez la fin.")

@bot.command()
@commands.has_permissions(kick_members = True)
async def confirm(ctx):
    if disc.garde == True:
        disc.check = True
        disc.garde = False
        await ctx.send("Chargement en cours...")
        time.sleep(1)
        await ctx.send("Supression des messages en cours... Cela peut prendre jusqu'à plusieurs secondes...")
        await ctx.channel.purge()
    else:
        await ctx.send("Vous ne pouvez pas utiliser cette commande.")

@bot.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, user : discord.User, *reason):
    reason = " ".join(reason)
    await ctx.guild.kick(user, reason = reason)
    embed=discord.Embed(title="**Hylian's Court**", description = f"{user} a été expulsé de Hyrule. Raison : {reason}", color=0xfffef2)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/772462786013691935/774741037947420702/HYLIA.png")
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, user : discord.User, *reason):
    reason = " ".join(reason)
    await ctx.guild.ban(user, reason = reason)
    embed=discord.Embed(title="**Hylian's Court**", description = f"{user} a été banni de Hyrule. Raison : {reason}", color=0xfffef2)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/772462786013691935/774741037947420702/HYLIA.png")
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(ban_members = True)
async def unban(ctx, user):
    userName, userId = user.split("#")
    bannedUsers = await ctx.guild.bans()
    for i in bannedUsers:
        if i.user.name == userName and i.user.discriminator == userId:
            await ctx.guild.unban(i.user)
            await ctx.send(f"{user} peut revenir à Hyrule.")
            return
    await ctx.send(f"{user} n'a jamais été banni de Hyrule ! Ou du moins, on ne le trouve pas sur nos papiers...")

@bot.command()
@commands.has_permissions(kick_members = True)
async def mute(ctx, member : discord.Member, *, reason = "Aucune raison n'a été renseignée"):
    mutedRole = await getMutedRole(ctx)
    hylia = await getDeesseRole(ctx)
    if hylia in member.roles:
        await ctx.send(f"... Non, je ne vais pas me taire !")
    elif mutedRole in member.roles:
        await ctx.send(f"**{member}** n'a déjà plus le droit à la parole.")
    else:
        await member.add_roles(mutedRole, reason = reason)
        embed=discord.Embed(title="**Hylian's Court**", description = f"Hylia a décidé arbitrairement que **{member}** n'aurait plus le droit à la parole !", color = 0xfffef2)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/772462786013691935/774741037947420702/HYLIA.png")
        await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(kick_members = True)
async def unmute(ctx, member : discord.Member, *, reason = "Aucune raison n'a été renseignée"):
    mutedRole = await getMutedRole(ctx)
    if mutedRole in member.roles:
        await member.remove_roles(mutedRole, reason = reason)
        embed=discord.Embed(title="**Hylian's Court**", description = f"Hylia redonne le droit de parole à **{member}**", color = 0xfffef2)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/772462786013691935/774741037947420702/HYLIA.png")
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"**{member}** a déjà le droit de parler.")

@bot.command()
@commands.has_permissions(kick_members = True)
async def tempmute(ctx, member : discord.Member, temps : int, *, reason = "Aucune raison n'a été renseignée"):
    if temps > 0:
        mutedRole = await getMutedRole(ctx)
        if mutedRole in member.roles:
            await ctx.send(f"**{member}** n'a déjà plus le droit à la parole.")
        else:
            durée = temps * 60
            ###########################
            await member.add_roles(mutedRole, reason = reason)
            embed=discord.Embed(title="**Hylian's Court**", description = f"Hylia a décidé arbitrairement que **{member}** n'aurait plus le droit à la parole pendant {temps} minutes ! Raison = {reason}", color=0xfffef2)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/772462786013691935/774741037947420702/HYLIA.png")
            await ctx.send(embed=embed)
            await asyncio.sleep(durée)
            ###########################
            await member.remove_roles(mutedRole, reason = reason)
            embed=discord.Embed(title="**Hylian's Court**", description = f"Hylia redonne la parole à **{member}**.", color=0xfffef2)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/772462786013691935/774741037947420702/HYLIA.png")
            await ctx.send(embed=embed)
    else:
        await ctx.send(f"Vous ne pouvez pas rentrer de nombres négatifs.")

@bot.command()
async def zelda(ctx):
    embed=discord.Embed(title="Jeux Zelda", color=0xfffef2)
    embed.set_author(name="Hyrule's Folders",icon_url="https://cdn.discordapp.com/attachments/772462786013691935/774741037947420702/HYLIA.png")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/772462786013691935/774741037947420702/HYLIA.png")
    valeurs="""-Zelda I
    -Zelda II, The Adventure of Link
    -The Legend of Zelda : A Link to the Past
    -The Legend of Zelda : Link's Awakening (1993)
    -The Legend of Zelda : Ocarina of Time (1998)
    -The Legend of Zelda : Majora's Mask (2000)
    -The Legend of Zelda : Oracle of Seasons (2001)
    -The Legend of Zelda : Oracle of Ages (2001)
    -The Legend of Zelda : Four Swords (2002)
    -The Legend of Zelda : The Wind Waker (2002)
    -The Legend of Zelda : The Minish Cap (2004)
    -The Legend of Zelda : Four Swords Adventures (2004)
    -The Legend of Zelda : Twilight Princess (2006)
    -The Legend of Zelda : Phantom Hourglass (2007)
    -The Legend of Zelda : Spirit Tracks (2009)
    -The Legend of Zelda : Skyward Sword (2011)
    -The Legend of Zelda : A Link Between Worlds (2013)
    -The Legend of Zelda : Triforces Heroes (2015)
    -The Legend of Zelda : Breath of the Wild (2017)
    -The Legend of Zelda : Sequel of the Wild (20XX)
    -The Legend of Zelda : Skyward Sword HD (2021)"""
    embed.add_field(name="Liste des jeux Zelda canon : ", value=valeurs, inline=True)
    await ctx.send(embed=embed)
    embed=discord.Embed(title="Timelines", color=0xfffef2)
    embed.set_author(name="Hyrule's Folders",icon_url="https://cdn.discordapp.com/attachments/772462786013691935/774741037947420702/HYLIA.png")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/772462786013691935/774741037947420702/HYLIA.png")
    embed.add_field(name="Tradition divine & Héros du temps", value="Zelda Skyward Sword\nZelda Minish Cap\nZelda Four Sword\nZelda Ocarina of Time", inline=True)
    embed.add_field(name="Branche de l'Héros Adulte", value="Zelda Wind Waker\nZelda Phantom Hourglass\nZelda Spirits Tracks", inline=True)
    embed.add_field(name="Branche de la défaite du Héros", value="Zelda A Link to the Past\nZelda Oracles of Seaons\nZelda Oracles of Ages\nZelda Link's Awaneking\nZelda I\nZelda II", inline=True)
    embed.add_field(name="Branche de l'Héros Enfant", value="Zelda Majora's Mask\nZelda Twiligt Princess\nZelda Four Swords Adventures\n", inline=True)
    await ctx.send(embed=embed)


@bot.command()
@commands.has_permissions(kick_members = True)
async def modération(ctx):
    await ctx.send("$ban pseudo raison -> sert à ban quelqu'un\n"
    "$kick pseudo raison -> sert à kick quelqu'un\n"
    "$unban pseudo -> sert à déban quelqu'un\n"
    "$mute pseudo raison -> sert à mute quelqu'un\n"
    "$unmute pseudo raison -> sert à démute quelqu'un, j'pense que t'as compris à force\n"
    "$clear n -> sert à enlever n messages (par exemple $clear 5 supprimera les 5 derniers messages\n"
    "$clearall -> sert à supprimer TOUS les messages d'un channel. Faites attention !")

@bot.command()
async def staff(ctx):
    embed=discord.Embed(title="**Staff du Discord The Legend of Zelda Français**", color=0xfffef2)
    embed.set_author(name="Hyrule's Folders", icon_url="https://cdn.discordapp.com/attachments/772462786013691935/774741037947420702/HYLIA.png")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/772462786013691935/774741037947420702/HYLIA.png")
    embed.add_field(name="**__LEADER__**", value="**•Wolfka**", inline=True)
    embed.add_field(name="**__MODÉRATEUR__**", value="**•Skyflooze**\n **•Wild**\n**•Nayru**", inline=True)
    await ctx.send(embed=embed)


@bot.command()
async def aide(ctx):
    embed=discord.Embed(title="**Commandes utile pour les Hyruliens**",color=0xfffef2)
    embed.set_author(name="Hyrule's Folders", icon_url="https://cdn.discordapp.com/attachments/772462786013691935/774741037947420702/HYLIA.png")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/772462786013691935/774741037947420702/HYLIA.png")
    valeurs = """$**zelda** -> Vous renvoie la liste des jeux Zelda
    $**staff** -> Vous renvoie la liste des personnes du staff
    $**grades** -> Vous renvoie la liste des grades par niveaux
    $**baston @pseudo @pseudo2** -> ... A vous de tester.
    $**quizz** -> Lancer un quizz
    $**helpquizz** -> Aide pour le quizz"""
    embed.add_field(name="**__Commandes Hylia__**", value= valeurs, inline=True)
    embed.add_field(name="**__Commandes Asarim__**", value="!**help** -> Vous renvoie les commandes nécessaire à la compréhension de Asarim", inline=True)
    await ctx.send(embed=embed)

@bot.command()
async def grades(ctx):
    embed=discord.Embed(title="**Spécifications des grades par niveaux**",color=0xfffef2)
    embed.set_author(name="Hyrule's Folders", icon_url="https://cdn.discordapp.com/attachments/772462786013691935/774741037947420702/HYLIA.png")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/772462786013691935/774741037947420702/HYLIA.png")
    valeurs = """***Niveau 0 à 1*** : `Noix Korogu`
    ***Niveau 2 à 5*** : `Voyageur Intrépide`
    ***Niveau 6 à 10*** : `Jeune Ecuyer`
    ***Niveau 11 à 15*** : `Brave Soldat`
    ***Niveau 16 à 20*** : `Noble Chevalier`
    ***Niveau 21 à 25*** : `Garde Royal`
    ***Niveau 26 à 30*** : `Petit Prodiges`
    ***Niveau 30*** : `Héros ⚔️`
     """
    embed.add_field(name="**Grades:**", value = valeurs, inline=True)
    await ctx.send(embed=embed)

@bot.command()
async def baston(ctx, combattant1 , combattant2):
    tablo = [combattant1, combattant2]
    aléa = random.randint(0,1)
    await ctx.send(f"Le combat opposant {combattant1} et {combattant2} va commencer dans 3...")
    await asyncio.sleep(1)
    await ctx.send("2...")
    await asyncio.sleep(1)
    await ctx.send("1...")
    await asyncio.sleep(1)
    await ctx.send(f"BOUM ! C'est {tablo[aléa]} qui gagne le combat !")


############################################################QUIZZ#######################################################################


@bot.command()
async def quizz(ctx):
    if q.getQuizzEnCours() == False:
        q.setLancer(True)
        q.setQuizzEnCours(True)
        embed=discord.Embed(title="Le Quizz LonLon Coffee <:lonloncoffee:945743720173670480>", color=0xfffef2)
        embed.add_field(name="🟢 Questions faciles\n🟠 Questions moyennes\n🔴 Questions difficiles", value="Pour lancer une partie, tapez $lancer. On vous souhaite bonne chance !", inline=True)
        message = await ctx.send(embed=embed)
    else:
        await ctx.send("Un quizz est déjà en cours.")

@bot.command()
async def lancer(ctx):
    if q.getLancer(): #Si true
        q.setLancer(False)
        tour = 1
        vieuxPoints = []
        questionsUtilisées = []
        questionsUtiliséesIndex = []

        for i in cl.getTabJoueursObjet():
            vieuxPoints.append(i.getPoints())
        for w in range(5): #Nombre de questions
            #################################################POSE LA QUESTION
            alea = random.randint(0,len(q.getQuestions())-1) 
            while(q.getQuestions()[alea] in questionsUtilisées):
                alea = random.randint(0,len(q.getQuestions())-1)   

            questionsUtilisées.append(q.getQuestions()[alea])
            questionsUtiliséesIndex.append(alea) #Sert pour l'historique des questions posées à la fin.

            rep = ""
            for i in q.getReponses()[alea]:
                print(i)
                if i == q.getReponses()[alea][len(q.getReponses()[alea])-1]:
                    rep += "" + i + " ?"
                else:
                    rep += i + ",\n"
            try:
                embed=discord.Embed(title=q.getQuestions()[alea], color=0xfffef2, description = f"**{rep}**\n\n<:STX5:945700963803611216> Répondez en cliquant sur les lettres")
                message = await ctx.send(embed=embed)
            except Exception as e:
                print(e)

            
            for j in range(5): #Nombres de réponses (4 + 1 pour skip)
                emo = q.getTab()[j]
                await message.add_reaction(emo)
            
            
            #################################################FIN DE POSE LA QUESTION

            def check(reaction, user):
                for br in q.getReponses()[alea]:
                    if br == q.getBonneReponse()[alea]:
                        q.setPlace(q.getReponses()[alea].index(br))
                if user != bot.user:
                    x = (q.getTab()[q.getPlace()]).encode('utf-8')
                    return x

            var = False
            tabJoueurs = []  #Tablo des noms de joueurs qui est remit à 0 à chaque tour
            while(var == False):
                if q.getQuizzEnCours() == False:  #stop le quizz après $stopquizz
                    break
                verrou = False

                try:
                    reaction, user = await bot.wait_for('reaction_add', timeout=15.0 ,check=check)
                except asyncio.TimeoutError :
                    await ctx.send(f"Vous avez pris trop de temps ! **Question {w+1}** skipée.")
                    await message.delete();
                    break

                if Joueur(user).getUser() in tabJoueurs: #Si le joueur a déjà joué CE TOUR, on passe
                    pass
                else:                                       #Sinon, on créé un nouveau joueur
                    for i in cl.getTabJoueursObjet():               #Si le joueur a déjà joué auparavant, alors son pseudo est juste mit dans la liste tabJoueurs, mais il n'est pas nouvel inscrit
                        if i.getUser() == Joueur(user).getUser():
                            #print(f"je suis la {Joueur(user).getUser()}")
                            tabJoueurs.append(Joueur(user).getUser())
                            joueur = i
                            verrou = True
                    if verrou != True:                      #Si le joueur a JAMAIS joué, il est inscrit dans tabJoueurs et dans tabJoueursObjet
                        joueur = Joueur(user)
                        print(f"{Joueur(user).getUser()} est inscrit")
                        cl.ajouterJoueurs(joueur)
                        cl.ajouterJoueursId(user.id)
                        print(user.id)
                        tabJoueurs.append(joueur.getUser())
                #print(tabJoueurs)
                #print(cl.getTabJoueursObjet())

                if str(reaction.emoji) == (q.getTab()[4]):
                    var = True
                    print(joueur.getAPerduPoint())
                    if joueur.getAPerduPoint() == False:
                        joueur.rmPointsToUser()
                        await ctx.send(f"**Question {w+1}** skipée, `{user.name}` tu perds un point !")
                    elif joueur.getAPerduPoint() == True:
                        await ctx.send(f"**Question {w+1}** skipée.")
                    for i in cl.getTabJoueursObjet():
                        i.restartJouer()
                        i.setAPerduPoint(False)
                    await message.delete()

                elif(joueur.getJouer() > 0):
                    await ctx.send(f"Tu as déjà répondu `{user.name}` ")

                elif str(reaction.emoji) == (q.getTab()[q.getPlace()]):
                    await ctx.send(f"Bien joué `{user.name}` tu as trouvé la bonne réponse pour la **question {w+1}** !")
                    var = True
                    joueur.setPointsToUser(1)
                    for i in cl.getTabJoueursObjet():
                        i.restartJouer()
                    tour+=1
                    await message.delete()

                else:
                    await ctx.send(f"Mauvaise réponse `{user.name}` !")
                    joueur.rmPointsToUser()
                    joueur.setAPerduPoint(True)
                    joueur.setJouer()

        rep = ""
        for i in range(len(questionsUtilisées)):
            rep = rep + f"**Question {i+1}** : {questionsUtilisées[i]}\n**Réponse** : {q.getBonneReponse()[questionsUtiliséesIndex[i]]}\n" + "\n"
        embed=discord.Embed(color=0xfffef2)
        embed.add_field(name=f"Historique des questions", value=f"{rep}", inline=True)
        try:
            assert vieuxPoints[0] #Si crash (ce qui veut dire qu'on est au premier lancement) -> except
            await ctx.send("Fin du Quizz !")
            historique = await ctx.send(embed=embed)
            for i in range(len(cl.getTabJoueursObjet())):
                if vieuxPoints[i] > cl.getTabJoueursObjet()[i].getPoints():
                    await ctx.send(f"`{cl.getTabJoueursObjet()[i].getUser()}` a perdu {(vieuxPoints[i] - cl.getTabJoueursObjet()[i].getPoints())} points !")
                elif vieuxPoints[i] < cl.getTabJoueursObjet()[i].getPoints():
                    await ctx.send(f"`{cl.getTabJoueursObjet()[i].getUser()}` a gagné {(cl.getTabJoueursObjet()[i].getPoints() - vieuxPoints[i])} points !")
            await ctx.send("Utilisez $classement pour connaître le classement du serveur sur les quizz !")
        except Exception as e:
            print(e)
            await ctx.send("Fin du Quizz !")
            historique = await ctx.send(embed=embed)
            await ctx.send("Utilisez $classement pour connaître le classement du serveur sur les quizz !")

    else:
        await ctx.send("Vous devez lancer un quizz avec la commande $quizz pour accéder à cette commande. Utilisez $quizzhelp pour plus d'infos.")
    
    initialiserClassement()
    q.setLancer(False)
    q.setQuizzEnCours(False)

def initialiserClassement():
    tab = []
    cl.resetClassement()
    save = ""
    try:
        for i in range(len(cl.getTabJoueursObjet())):
            tab.append(cl.getTabJoueursObjet()[i])
        for i in range(len(cl.getTabJoueursObjet())):
            print(f"x avant : {tab}")
            x = cl.ajoutMaxAListe(tab)
            print(f"x : {x}")
            tab = x
        
        print(f"OUAIS : {cl.getTabJoueursObjet()}")
        print(f"TABLO : {tab}")
        for i in tab:
            print(i.getUser())
        print(cl.getTabClassement())
    except Exception as e:
        print(e)
    try:
        for i in range(len(cl.getTabClassement())):
            save = save + (f"{cl.getTabClassement()[i].getUserId()}:{cl.getTabClassement()[i].getUser()}:{cl.getTabClassement()[i].getPoints()}\n")
        file1 = open("classement.txt", "w", encoding="utf-8")
        file1.write(save)
        file1.close()

    except Exception as e:
        print(e)

@bot.command()
async def classement(ctx):
    valeur = ""
    serverLogo = ctx.guild.icon_url
    try:
        if len(cl.getTabClassement()) > 10: #Si il y a plus de 10 joueurs -> TOP 10 uniquement
            for i in range(10):
                valeur = valeur + (f"**{i+1}** : `{cl.getTabClassement()[i].getUser()}` avec {cl.getTabClassement()[i].getPoints()} points.\n")
            valeur = valeur + (f"\nSi vous n'êtes pas dans le TOP 10, utilisez $place pour connaître votre classement !")
            embed=discord.Embed(title="**Classement du Quizz `(TOP 10)`**",color=0xfffef2)
            embed.add_field(name=f"{len(cl.getTabClassement())} joueurs inscrits", value=valeur, inline=True)
            embed.set_thumbnail(url=(serverLogo))
            await ctx.send(embed=embed)
        else: #Sinon si c'est en dessous de 10, alors ça sera top len(classement)
            for i in range(len(cl.getTabClassement())):
                valeur = valeur + (f"**{i+1}** : `{cl.getTabClassement()[i].getUser()}` avec {cl.getTabClassement()[i].getPoints()} points.\n")
            embed=discord.Embed(title="**Classement du Quizz**",color=0xfffef2)
            embed.add_field(name=f"{len(cl.getTabClassement())} joueurs inscrits", value=valeur, inline=True)
            embed.set_thumbnail(url=(serverLogo))
            await ctx.send(embed=embed)
    except:
        embed=discord.Embed(title="**Classement du Quizz**",color=0xfffef2)
        embed.add_field(name=f"0 joueur inscrit", value="Aucune personne n'est dans le classement", inline=True)
        embed.set_thumbnail(url=(serverLogo))
        await ctx.send(embed=embed)



@bot.command()
async def place(ctx):
    print(ctx.message.author.name)
    placement, point = cl.getPlaceJoueurClassementEtPoints(ctx.message.author.name) #Pour récupérer classement + points
    pfp = ctx.message.author.avatar_url #Pour récupérer la pdp
    if placement==1:
        embed=discord.Embed(color=0xfffef2)
        embed.add_field(name="Ton classement", value=f"`{ctx.message.author.name}` tu es {placement}er(e) du classement avec {point} points !", inline=True)
        embed.set_image(url=(pfp))
        await ctx.send(embed=embed)
    elif placement < 1:
        embed=discord.Embed(color=0xfffef2)
        embed.add_field(name="Ton classement", value=f"`{ctx.message.author.name}` tu n'es pas classé avec...{point} point. Il faut avoir un score positif pour être classé <:ptdr:864804743498039307>", inline=True)
        embed.set_image(url=(pfp))
        await ctx.send(embed=embed)
    else:
        embed=discord.Embed(color=0xfffef2)
        embed.add_field(name="Ton classement", value=f"`{ctx.message.author.name}` tu es {placement}ème du classement avec {point} points !", inline=True)
        embed.set_image(url=(pfp))
        await ctx.send(embed=embed)


@bot.command()
async def stopquizz(ctx):
    if q.getQuizzEnCours() == True:
        q.setLancer(False)
        q.setQuizzEnCours(False)
        await ctx.send("Quizz arrêté")


@bot.command()
async def helpquizz(ctx):
    embed=discord.Embed(color=0xfffef2)
    embed.add_field(name="Commandes pour le fonctionnement du Quizz LonLon Coffee", value="`Pour lancer le quizz` : $quizz\n`Pour commencer le quizz` : $lancer\n`Pour connaître le classement du quizz`: $quizz\n`Pour connaître votre place dans le classement` : $place\n`Pour arrêter le système du quizz` (A UTILISER EN CAS DE GROS PROBLEMES, NE PAS UTILISER SINON) : $stopquizz", inline=True)
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(kick_members = True)
async def addpoint(ctx, user:discord.User, point : int):
    tabJoueur = []

    for i in cl.getTabJoueursObjet():
        tabJoueur.append(i.getUser())
    if user.name not in tabJoueur:
        joueur = Joueur(user)
        joueur.setPointsToUser(point)
        cl.ajouterJoueurs(joueur)
        cl.ajouterJoueursId(user.id)
    else:
        for i in cl.getTabJoueursObjet():
            if i.getUser()==user.name:
                i.setPointsToUser(point)
    initialiserClassement()


@bot.command()
@commands.has_permissions(kick_members = True)
async def setclassement(ctx):
    tab = []
    with open("classement.txt", "r", encoding="utf-8") as f:
        for ligne in f:

            x = ligne.split(":")

            cl.ajouterJoueursId(x[0])

            user = await bot.fetch_user(x[0])

            cl.ajouterJoueurs(Joueur(user))
            
            tab.append(int(x[2])) #tablo des points de chaque joueur
            
            try:
                j=0
                for i in cl.getTabJoueursObjet():   
                    i.donnerNombrePoint(tab[j])
                    j+=1
            except Exception as e:
                print(e)
            print(cl.getTabJoueursObjet())
            initialiserClassement()



#####################################################################Blindtest

'''

@bot.command()
@commands.has_permissions(kick_members = True)
async def blindtest(ctx):
    disc.def_open = True

@bot.command()
async def join(ctx,pseudo:str):
    if disc.def_open == True:
        for i in disc.participants:
            if i==pseudo:
                await ctx.send(f"{pseudo} est déjà dans la liste.")
            else:
                disc.participants.append(pseudo)
                disc.points.append(0)

@bot.command()
async def participants(ctx):
    await ctx.send(f"Voici la liste des participants du blindtest : ")
    for i in disc.participants:
        await ctx.send(f"{i}\n")

@bot.command()
@commands.has_permissions(kick_members=True)
async def points(ctx,pseudo:str,point:int):
    for i in disc.participants:
        if i==pseudo:
            disc.points[disc.participants.index(i)] += point


@bot.command()
@commands.has_permissions(kick_members = True)
async def close(ctx):
    disc.def_open = False

@bot.command()
@commands.has_permissions(kick_members=True)
async def blindtestfin(ctx):
    await ctx.send("C'est la fin du blindtest !")
    await asyncio.sleep(2)
    indice = max(disc.points)
    await ctx.send(f"Le gagnant est {disc.participants(indice)} avec un total de {disc.points(indice)} !")
    await asyncio.sleep(2)
    await ctx.send("Merci d'avoir participé ! Voici la liste des résultats : ")
    for i in range(len(disc.participants)):
        await ctx.send(f"{disc.participants[i]} -> {disc.points[i]} points")
    disc.points = []
    disc.participants = []

'''



################################################################################Tchats

'''
@bot.command()
async def artiste(ctx):
    await ctx.channel.send("<#773254819707224074>")

@bot.command()
async def gen(ctx):
    await ctx.channel.send("<#772462715004387350>")

@bot.command()
async def stream(ctx):
    await ctx.channel.send("<#773658789161074708>")
'''


bot.run("NzczMjQ0MDIwMDg3NzE3OTQ5.X6GZnA.HGvwG3-UW_nfe_y2wXVevcbAc58")