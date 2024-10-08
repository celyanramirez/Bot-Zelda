#from msilib.schema import Class
from cgi import test
from contextvars import Context
from email import message
from imghdr import what
from multiprocessing import context
from sqlite3 import Time
from this import d
from typing import Any
from unittest import TestCase
import discord
import asyncio
import random
import time
from commandes import *
from discord.ext import commands
from discord.ext import tasks
from discord.ui import Button, View
from datetime import date, datetime
from connection import *
from discord.utils import get
import os
import schedule
import sqlite3


intents = discord.Intents.default()
intents.members = True  # Pour obtenir la liste des membres du serveur
intents.guilds = True
intents.message_content = True

client = discord.Client(intents=intents)
disc = Botdisc()
q = Quizz()
cl = Classement()
prefix = "$"
bot = commands.Bot(command_prefix=prefix, intents=intents)
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

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

def createTables():

    # Création de la table leaderboard
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS leaderboard (
        user_id TEXT PRIMARY KEY,
        username TEXT,
        points INTEGER DEFAULT 0
    )
    ''')

    # Sauvegarder (commit) les modifications
    conn.commit()

def getUsers():
    cursor.execute('SELECT * FROM leaderboard')
    users = cursor.fetchall()
    return users

def getUsernameById(id):
    cursor.execute(f'SELECT leaderboard.username FROM leaderboard WHERE user_id = {id}')
    username = cursor.fetchall()
    return username[0][0]

def max(tab):
    maximum = 0
    for i in range(len(tab)):
        if tab[i]>maximum:
            maximum=i
    return maximum

ROLE_NAME = "PRODIGE DU SAVOIR"

@tasks.loop(minutes=2)
async def check_leaderboard():
    guild = bot.get_guild(772462714491633685)
    if not guild:
        print("Le bot n'est connecté à aucun serveur.")
        return

    # Obtenir le rôle Top 1 Guess
    role = discord.utils.get(guild.roles, name=ROLE_NAME)
    if not role:
        # Crée le rôle si il n'existe pas
        role = await guild.create_role(name=ROLE_NAME, reason="Création du rôle pour le top 1 du classement Guess")

    # Obtenir le top 1 du classement
    cursor.execute('SELECT user_id FROM leaderboard ORDER BY points DESC LIMIT 1')
    result = cursor.fetchone()
    if not result:
        print("Aucun joueur trouvé dans le classement.")
        return

    top1_user_id = result[0]
    top1_member = guild.get_member(int(top1_user_id))

    if not top1_member:
        print(f"Le joueur avec l'ID {top1_user_id} n'est pas trouvé dans le serveur.")
        return

    # Retirer le rôle Top 1 de tous les membres
    for member in guild.members:
        if role in member.roles and member != top1_member:
            await member.remove_roles(role)

    # Donner le rôle Top 1 au top 1 actuel
    if role not in top1_member.roles:
        await top1_member.add_roles(role)
        print(f"{top1_member.name} a été assigné le rôle {ROLE_NAME}.")

@bot.event
async def on_ready():
    check.start()
    createTables()
    check_leaderboard.start()
    print("J'suis prêt !")
    

class PointsView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.users = getUsers()
        self.points_to_add_or_remove = 0  # Nouveau: Stocke le nombre de points

        self.add_button = discord.ui.Button(label="Ajout Points", style=discord.ButtonStyle.green)
        self.remove_button = discord.ui.Button(label="Retrait Points", style=discord.ButtonStyle.red)

        # Assigner les callbacks aux boutons
        self.add_button.callback = self.check_permissions(self.add_points)
        self.remove_button.callback = self.check_permissions(self.remove_points)
        
        # Ajouter les boutons à la vue
        self.add_item(self.add_button)
        self.add_item(self.remove_button)
    
    def check_permissions(self, func):
        async def wrapper(interaction):
            if interaction.user.guild_permissions.ban_members:
                await func(interaction)
            else:
                await interaction.response.send_message("Vous n'avez pas la permission d'utiliser cette commande.", ephemeral=True)
        return wrapper

    async def add_points(self, interaction):
        self.users = getUsers()
        select = discord.ui.Select(
            placeholder="Choisir un nombre de points",
            options=[
                discord.SelectOption(label="100 points", value="100"),
                discord.SelectOption(label="50 points", value="50"),
                discord.SelectOption(label="25 points", value="25"),
            ]
        )
        select.callback = self.set_points_and_select_user
        self.points_to_add_or_remove = "add"  # Indique que les points doivent être ajoutés
        view = discord.ui.View()
        view.add_item(select)
        await interaction.response.send_message("Choisissez combien de points ajouter:", view=view, ephemeral=True)
    
    async def remove_points(self, interaction):
        self.users = getUsers()
        select = discord.ui.Select(
            placeholder="Choisir un nombre de points",
            options=[
                discord.SelectOption(label="100 points", value="100"),
                discord.SelectOption(label="50 points", value="50"),
                discord.SelectOption(label="25 points", value="25"),
            ]
        )
        select.callback = self.set_points_and_select_user
        self.points_to_add_or_remove = "remove"  # Indique que les points doivent être retirés
        view = discord.ui.View()
        view.add_item(select)
        await interaction.response.send_message("Choisissez combien de points retirer:", view=view, ephemeral=True)
    
    async def set_points_and_select_user(self, interaction):
        self.selected_points = int(interaction.data['values'][0])
        modal = SelectUserModal()
        await interaction.response.send_modal(modal)
        await modal.wait()  # Attendre que le modal soit soumis
        user_id = modal.get_user_id()  # Récupérer l'ID du joueur

        if user_id is None:
            await interaction.followup.send("Aucun utilisateur sélectionné. Veuillez réessayer.", ephemeral=True)
            return

        if self.points_to_add_or_remove == "add":
            await self.add_selected_points(interaction, user_id)
        elif self.points_to_add_or_remove == "remove":
            await self.remove_selected_points(interaction, user_id)

    async def add_selected_points(self, interaction, user_id):
        user = await interaction.guild.fetch_member(int(user_id))
        cursor.execute('INSERT OR IGNORE INTO leaderboard (user_id, username, points) VALUES (?, ?, 0)', (str(user.id), user.name))
        cursor.execute('UPDATE leaderboard SET points = points + ? WHERE user_id = ?', (self.selected_points, user_id))
        conn.commit()
        await interaction.followup.send(f'{self.selected_points} points ajouté à {user.name} !', ephemeral=True)
    
    async def remove_selected_points(self, interaction, user_id):
        user = await interaction.guild.fetch_member(int(user_id))
        cursor.execute('INSERT OR IGNORE INTO leaderboard (user_id, username, points) VALUES (?, ?, 0)', (str(user.id), user.name))
        cursor.execute('UPDATE leaderboard SET points = points - ? WHERE user_id = ?', (self.selected_points, user_id))
        conn.commit()
        await interaction.followup.send(f'{self.selected_points} points enlevé à {user.name} !', ephemeral=True)

    
class SelectUserModal(discord.ui.Modal):
    def __init__(self):
        super().__init__(title="Sélectionner un utilisateur")
        self.user_input = discord.ui.TextInput(label="Pseudo, mention ou ID de l'utilisateur", max_length=45)
        self.add_item(self.user_input)
        self.user_id = None  # Attribut pour stocker l'ID de l'utilisateur

    async def on_submit(self, interaction):
        user_input = self.user_input.value
        print(f'Débogage: Entrée utilisateur: {user_input}')  # Débogage
        user = await self.resolve_user(interaction, user_input)
        
        if user:
            print(f'Débogage: Utilisateur trouvé: {user.name} ({user.id})')  # Débogage
            self.user_id = str(user.id)  # Stocker l'ID de l'utilisateur
        else:
            print('Débogage: Utilisateur non trouvé')  # Débogage

        await interaction.response.send_message(f"Utilisateur {user.name} sélectionné.", ephemeral=True)  # Réponse éphemère pour fermer la fenêtre modale

        self.stop()

    async def resolve_user(self, interaction, user_input):
        try:
            if user_input.isdigit():
                return await interaction.guild.fetch_member(int(user_input))
            elif user_input.startswith('<@') and user_input.endswith('>'):
                user_id = user_input[2:-1].replace('!', '')
                return await interaction.guild.fetch_member(int(user_id))
            else:
                for member in interaction.guild.members:
                    if member.name == user_input:
                        return member
        except Exception as e:
            print(f'Erreur lors de la résolution de l\'utilisateur: {e}')  # Débogage
        return None
    
    def get_user_id(self):
        return self.user_id

@bot.command()
@commands.has_permissions(ban_members=True)
async def guessadd(ctx, user: discord.Member, points: int):
    # Vérifier si l'utilisateur existe déjà dans le classement
    cursor.execute('SELECT points FROM leaderboard WHERE user_id = ?', (str(user.id),))
    result = cursor.fetchone()

    # Ajouter l'utilisateur s'il n'est pas déjà dans le classement
    if result is None:
        cursor.execute('INSERT INTO leaderboard (user_id, username, points) VALUES (?, ?, ?)', (str(user.id), user.name, points))
    else:
        cursor.execute('UPDATE leaderboard SET points = points + ? WHERE user_id = ?', (points, str(user.id)))

    conn.commit()

    # Confirmation du succès de l'ajout
    await ctx.send(f"{points} points ajoutés à {user.name} pour le classement GUESS!")

@bot.command()
@commands.has_permissions(ban_members=True)
async def guessremove(ctx, user: discord.Member, points: int):
    # Vérifier si l'utilisateur existe déjà dans le classement
    cursor.execute('SELECT points FROM leaderboard WHERE user_id = ?', (str(user.id),))
    result = cursor.fetchone()
    if result is None:
        await ctx.send(f"L'utilisateur {user.name} n'a pas de points dans le classement GUESS.")
        return

    current_points = result[0]

    # Vérification des points pour éviter un score négatif
    if current_points - points < 0:
        await ctx.send(f"{user.name} n'a pas assez de points pour cette déduction.")
        return

    # Retirer les points
    cursor.execute('UPDATE leaderboard SET points = points - ? WHERE user_id = ?', (points, str(user.id)))
    conn.commit()

    # Confirmation du succès de la suppression
    await ctx.send(f"{points} points retirés à {user.name} pour le classement GUESS!")

   
@bot.command()
@commands.has_permissions(ban_members = True)
async def guess(ctx):
    try:
        view = PointsView()
        await ctx.send("Cliquez sur un bouton pour ajouter ou retirer des points:", view=view)
    except Exception as e:
        print(e)

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
    embed=discord.Embed(title="**Hylian's Court**", description = f"{user} a été expulsé de Hyrule. Raison : {reason}", color=0xC09866)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/772462786013691935/774741037947420702/HYLIA.png")
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, user : discord.User, *reason):
    reason = " ".join(reason)
    await ctx.guild.ban(user, reason = reason)
    embed=discord.Embed(title="**Hylian's Court**", description = f"{user} a été banni de Hyrule. Raison : {reason}", color=0xC09866)
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
        embed=discord.Embed(title="**Hylian's Court**", description = f"Hylia a décidé arbitrairement que **{member}** n'aurait plus le droit à la parole !", color = 0xC09866)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/772462786013691935/774741037947420702/HYLIA.png")
        await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(kick_members = True)
async def unmute(ctx, member : discord.Member, *, reason = "Aucune raison n'a été renseignée"):
    mutedRole = await getMutedRole(ctx)
    if mutedRole in member.roles:
        await member.remove_roles(mutedRole, reason = reason)
        embed=discord.Embed(title="**Hylian's Court**", description = f"Hylia redonne le droit de parole à **{member}**", color = 0xC09866)
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
            embed=discord.Embed(title="**Hylian's Court**", description = f"Hylia a décidé arbitrairement que **{member}** n'aurait plus le droit à la parole pendant {temps} minutes ! Raison = {reason}", color=0xC09866)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/772462786013691935/774741037947420702/HYLIA.png")
            await ctx.send(embed=embed)
            await asyncio.sleep(durée)
            ###########################
            await member.remove_roles(mutedRole, reason = reason)
            embed=discord.Embed(title="**Hylian's Court**", description = f"Hylia redonne la parole à **{member}**.", color=0xC09866)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/772462786013691935/774741037947420702/HYLIA.png")
            await ctx.send(embed=embed)
    else:
        await ctx.send(f"Vous ne pouvez pas rentrer de nombres négatifs.")

@bot.command()
async def zelda(ctx):
    await ctx.send(file=discord.File("main/HYLIA_Zelda_I.png"))
    await ctx.send(file=discord.File("main/HYLIA_Zelda_II.png"))


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
    await ctx.send(file=discord.File("main/HYLIA_Organigramme.png"))

@bot.command()
async def aide(ctx):
    embed=discord.Embed(title="**Commandes utile pour les Hyruliens**",color=0xC09866)
    embed.set_author(name="Hyrule's Folders", icon_url="https://cdn.discordapp.com/attachments/609434127258746896/1125337609649008640/HYLIA_V2.jpg")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/609434127258746896/1125337609649008640/HYLIA_V2.jpg")
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
    await ctx.send(file=discord.File("main/images/levels/05.png"))
    await ctx.send(file=discord.File("main/images/levels/06.png"))
    await ctx.send(file=discord.File("main/images/levels/07.png"))

@bot.command()
async def baston(ctx, *args):
    aléa = random.randint(0,len(args)-1)
    msg = "Le combat opposant "
    for i in range(len(args)-1):
        msg = msg + args[i] + ", "
    msg = msg[:-1]
    msg = msg[:-1]
    msg = msg + " et " + args[len(args)-1] + " va commencer dans 3..."
    await ctx.send(msg)
    await asyncio.sleep(1)
    await ctx.send("2...")
    await asyncio.sleep(1)
    await ctx.send("1...")
    await asyncio.sleep(1)
    await ctx.send(f"BOUM ! C'est {args[aléa]} qui gagne le combat !")

'''
@tasks.loop(seconds=10)
async def checkReu():
    date = datetime.now()
    channel = bot.get_channel(1029657819470889021)
    if date.hour == 20:
        await channel.send("||@everyone ||\n**Réunion quotidienne**\n\nQu'est-ce que vous avez fait ?\nQu'est-ce que vous allez faire demain ?\nAvez-vous rencontré des problèmes ?")
'''

@tasks.loop(seconds=10)
async def check():
    a = datetime.now()
    if a.hour == 0:
        await anniv()
        await asyncio.sleep(3600)

async def anniv():
    today = date.today()
    mois = today.month
    jour = today.day
    channel = bot.get_channel(772462715004387350)
    if jour == 21 and mois == 2:
        await channel.send("Aujourd'hui, c'est l'anniversaire du tout premier **The Legend of Zelda** <:loz:1121786414636482580> ! C'est pas rien ! On peut même dire que c'est l'anniversaire la saga ! Alors on dit tous :\n 🎂 🎉 **BON ANNIVERSAIRE THE LEGEND OF ZELDA** 🎉 🎂")
    if jour == 15 and mois == 11:
        await channel.send("Aujourd'hui, c'est l'anniversaire du tout premier **The Legend of Zelda** <:loz:1121786414636482580>, en Europe ! En réalité, il est arrivé chez nous (en France) bien plus tard, mais chut. \nOn lui souhaite un 🎂 🎉 **BON ANNIVERSAIRE** 🎉 🎂")
   
    if jour == 14 and mois == 2:
        await channel.send("Aujourd'hui, c'est l'anniversaire de **The Legend of Zelda : The Adventure of Link** <:aol:1121788774188335107> !\nQu'on l'aime ou non, il mérite qu'on lui souhaite un 🎂 🎉 **JOYEUX ANNIVERSAIRE !** 🎉 🎂")
    if jour == 26 and mois == 9:
        await channel.send("Aujourd'hui, c'est l'anniversaire de **The Legend of Zelda : The Adventure of Link** <:aol:1121788774188335107> chez nous, en Europe !\nQu'on l'aime ou non, il mérite qu'on lui souhaite un 🎂 🎉 **JOYEUX ANNIVERSAIRE !** 🎉 🎂 ")
    
    if jour == 21 and mois == 11:
        await channel.send("Aujourd'hui, c'est l'anniversaire de **The Legend of Zelda : A Link to the Past** <:alttp:1121788800838930512> !\nUn des Zelda les plus appréciés, et qui aura sûrement été le premier pour les plus anciens d'entre-nous !\nIl mérite qu'on lui souhaite un 🎂 🎉 **JOYEUX ANNIVERSAIRE !** 🎉 🎂")
    if jour == 24 and mois == 9:
        await channel.send("Aujourd'hui, c'est l'anniversaire de **The Legend of Zelda : A Link to the Past** <:alttp:1121788800838930512> chez nous, en Europe !\nQu'avez-vous pensé de ce Zelda, qui est probablement un des plus appréciés de la saga ?\nEt n'oubliez pas de lui souhaiter un 🎂 🎉 **JOYEUX ANNIVERSAIRE !** 🎉 🎂 ")
   
    if jour == 6 and mois == 6:
        await channel.send("Aujourd'hui, c'est l'anniversaire de **The Legend of Zelda : Link's Awakening** <:lsa:1121788870741217301> !\nUn Zelda à très spécial, avec son monde si particulier et ses références à d'autres univers de jeux-vidéo comme... Mario !\nBref, souhaitez-lui un 🎂 🎉 **JOYEUX ANNIVERSAIRE !** 🎉 🎂")
    if jour == 1 and mois == 12:
        await channel.send("Aujourd'hui, c'est l'anniversaire de **The Legend of Zelda : Link's Awakening** <:lsa:1121788870741217301> chez nous, en Europe !\nUn Zelda à très spécial, avec son monde si particulier et ses références à d'autres univers de jeux-vidéo comme... Mario !\nBref, souhaitez-lui un 🎂 🎉 **JOYEUX ANNIVERSAIRE !** 🎉 🎂")
    
    if jour == 20 and mois == 9:
        await channel.send("Aujourd'hui, c'est l'anniversaire de **The Legend of Zelda : Link's Awakening HD** <:lsa:1121788870741217301> !\nUn superbe remake de l'opus GameBoy ! Qu'on aime ou non son style artistique, il reste très fidèle au jeu original !\nIl mérite qu'on lui souhaite un 🎂 🎉 **JOYEUX ANNIVERSAIRE !** 🎉 🎂 ")

    if jour== 21 and mois == 11:
        await channel.send("Aujourd'hui, c'est l'anniversaire de **The Legend of Zelda : Ocarina of Time** <:oot:1121788885861675008> !\nLe tout premier The Legend of Zelda en 3D ! Il est même considéré par beaucoup comme le meilleur jeu de tous les temps !\nIl mérite qu'on lui souhaite un 🎂 🎉 **JOYEUX ANNIVERSAIRE !** 🎉 🎂")
    if jour == 11 and mois == 12:
        await channel.send("Aujourd'hui, c'est l'anniversaire de **The Legend of Zelda : Ocarina of Time** <:oot:1121788885861675008> chez nous, en Europe ! Vous avez pu y jouer à sa sortie ?\nIl mérite qu'on lui souhaite un 🎂 🎉 **JOYEUX ANNIVERSAIRE !** 🎉 🎂")
    
    if jour == 27 and mois == 4:
        await channel.send("Aujourd'hui, c'est l'anniversaire de **The Legend of Zelda : Majora's Mask** <:msm:1121788914525548615> !\nProbablement le Zelda le plus singulier de la franchise !\nOn lui souhaite un 🎂 🎉 **JOYEUX ANNIVERSAIRE !** 🎉 🎂")
    if jour == 17 and mois == 11:
        await channel.send("Aujourd'hui, c'est l'anniversaire de **The Legend of Zelda : Majora's Mask** <:msm:1121788914525548615> chez nous, en Europe !\nUn Zelda qui en aura surpris plus d'un par son ambiance si singulière !\nOn lui souhaite un 🎂 🎉 **JOYEUX ANNIVERSAIRE !** 🎉 🎂")
    
    if jour == 13 and mois == 2:
        await channel.send("Aujourd'hui, c'est l'anniversaire de **The Legend of Zelda : Majora's Mask 3D** <:msm:1121788914525548615> !\nUn superbe remake de l'opus N64 qui lui rend parfaitement honneur !\nOn lui souhaite un 🎂 🎉 **JOYEUX ANNIVERSAIRE !** 🎉 🎂")
    
    if jour == 27 and mois == 2:
        await channel.send("Aujourd'hui, ce n'est pas l'anniversaire d'un jeu Zelda... Non, c'est l'anniversaire de 2 jeux Zelda ! **Oracles of Ages <:ooa:1121788934121341042> et Oracles of Seasons <:oos:1121788947345965187>** !\nOn leur souhaite un 🎂 🎉 **JOYEUX ANNIVERSAIRE !** 🎉 🎂")
    if jour == 5 and mois == 10:
         await channel.send("Aujourd'hui, ce n'est pas l'anniversaire d'un jeu Zelda... Non, c'est l'anniversaire de 2 jeux Zelda ! **Oracles of Ages <:ooa:1121788934121341042> et Oracles of Seasons <:oos:1121788947345965187>**, qui sont arrivés ce jour-ci dans nos belles contrées !\nOn leur souhaite un 🎂 🎉 **JOYEUX ANNIVERSAIRE !** 🎉 🎂")
    
    if jour == 2 and mois == 12:
        await channel.send("Aujourd'hui, c'est l'anniversaire de **The Legend of Zelda : Four Swords** <:fs:1121789007467135047> !\nLe tout premier jeu Zelda en multijoueur !\nIl mérite bien qu'on lui souhaite un 🎂 🎉 **JOYEUX ANNIVERSAIRE !** 🎉 🎂")
    if jour == 28 and mois == 4:
         await channel.send("Aujourd'hui, c'est l'anniversaire de **The Legend of Zelda : Four Swords** <:fs:1121789007467135047> chez nous, en Europe !\nLe tout premier jeu Zelda en multijoueur !\nIl mérite bien qu'on lui souhaite un 🎂 🎉 **JOYEUX ANNIVERSAIRE !** 🎉 🎂")
    
    if jour == 13 and mois == 12:
        await channel.send("Aujourd'hui, c'est l'annivesaire de **The Legend of Zelda : The Wind Waker** <:tww:1121788965922549760> !\nUn jeu qui en aura conquis plus d'un avec son open-world marin !\nOn lui souhaite un 🎂 🎉 **JOYEUX ANNIVERSAIRE !** 🎉 🎂")
    if jour == 3 and mois == 5:
        await channel.send("Aujourd'hui, c'est l'annivesaire de **The Legend of Zelda : The Wind Waker** <:tww:1121788965922549760> chez nous, en Europe !\nQui ici a été conquis par ce jeu et sa magnifique mer ?\nOn lui souhaite un 🎂 🎉 **JOYEUX ANNIVERSAIRE !** 🎉 🎂")
    
    if jour == 20 and mois == 9:
        await channel.send("Aujourd'hui, c'est l'anniversaire de **The Legend of Zelda : The Wind Waker HD** <:tww:1121788965922549760> !\nUn superbe remaster qui aura rendu le jeu encore plus beau visuellement, mais aussi plus agréable avec la voile rapide !\nOn lui souhaite un 🎂 🎉 **JOYEUX ANNIVERSAIRE !** 🎉 🎂")
    if jour == 4 and mois == 10:
        await channel.send("Aujourd'hui, c'est l'anniversaire de **The Legend of Zelda : The Wind Waker HD** <:tww:1121788965922549760> chez nous, en Europe !\nUn superbe remaster qui aura rendu le jeu encore plus beau visuellement, mais aussi plus agréable avec la voile rapide !\nOn lui souhaite un 🎂 🎉 **JOYEUX ANNIVERSAIRE !** 🎉 🎂")
    
    if jour == 18 and mois == 3:
        await channel.send("Aujourd'hui, c'est l'anniversaire de **The Legend of Zelda : Four Swords Adventure** <:fsa:1121789028719673454> !\nLe deuxième volet multijoueur de la saga, sorti sur Nintendo GameCube !\nOn lui souhaite un 🎂 🎉 **JOYEUX ANNIVERSAIRE !** 🎉 🎂")
    if jour == 7 and mois == 1:
        await channel.send("Aujourd'hui, c'est l'anniversaire de **The Legend of Zelda : Four Swords Adventure** <:fsa:1121789028719673454> chez nous, en Europe !\nLe deuxième volet multijoueur de la saga, sorti sur Nintendo GameCube !\nOn lui souhaite un 🎂 🎉 **JOYEUX ANNIVERSAIRE !** 🎉 🎂")
    
    if jour == 4 and mois == 11:
        await channel.send("Aujourd'hui, c'est l'anniversaire de **The Legend of Zelda : The Minish Cap** <:tmc:1121788983907725444> !\nLe fameux épisode sur Game Boy Advance, où Link est accompagné d'un bonnet... vivant ! D'ailleurs, on attend toujours le remake Nintendo !\nBref, souhaitez-lui un 🎂 🎉 **JOYEUX ANNIVERSAIRE !** 🎉 🎂")
    if jour == 12 and mois == 11:
        await channel.send("Aujourd'hui, c'est l'anniversaire de **The Legend of Zelda : The Minish Cap** <:tmc:1121788983907725444> mais cette fois-ci, chez nous, en Europe !\nSouhaitez-lui un 🎂 🎉 **JOYEUX ANNIVERSAIRE !** 🎉 🎂")
    
    if jour == 19 and mois == 11:
        await channel.send("Aujourd'hui, c'est l'anniversaire de **The Legend of Zelda : Twiligth Princess** <:tp:1121789061779169370> !\nPeut-être l'épisode avec lequel vous avez découvert la licence Zelda ! C'est en tout cas un épisode très apprécié !\nIl mérite qu'on lui souhaite un 🎂 🎉 **JOYEUX ANNIVERSAIRE !** 🎉 🎂")
    if jour == 8 and mois == 12:
        await channel.send("Aujourd'hui, c'est l'anniversaire de **The Legend of Zelda : Twiligth Princess** <:tp:1121789061779169370> chez nous, en Europe !\nQu'avez-vous pensé de cet opus et de son monde unique : le Crépuscule ? \nQuelle que soit votre réponse, il mérite qu'on lui souhaite un 🎂 🎉 **JOYEUX ANNIVERSAIRE !** 🎉 🎂")
    
    if jour == 4 and mois == 3:
        await channel.send("Aujourd'hui, c'est l'anniversaire de **The Legend of Zelda : Twiligth Princess HD** <:tp:1121789061779169370> !\nUn remaster très sympa qui embelli le jeu pour le rendre au goût du jour !\nSouhaitons-lui un 🎂 🎉 **JOYEUX ANNIVERSAIRE !** 🎉 🎂")
    if jour == 10 and mois == 3:
        await channel.send("Aujourd'hui, c'est encore l'anniversaire de **The Legend of Zelda : Twiligth Princess HD** <:tp:1121789061779169370>, mais cette fois-ci chez nous, en Europe !\nSouhaitons-lui un 🎂 🎉 **JOYEUX ANNIVERSAIRE !** 🎉 🎂")
    
    if jour == 23 and mois == 6:
        await channel.send("Aujourd'hui, c'est l'anniversaire de **The Legend of Zelda : Phantom Hourglass** <:ph:1121789085116272762> !\nLe premier épisode DS, qui fait suite directe à The Wind Waker !\nOn lui souhaite un 🎂 🎉 **JOYEUX ANNIVERSAIRE !** 🎉 🎂")
    if jour == 19 and mois == 10:
        await channel.send("Aujourd'hui, c'est l'anniversaire de **The Legend of Zelda : Phantom Hourglass** <:ph:1121789085116272762> chez nous, en Europe !\nLe premier épisode DS, qui fait suite directe à The Wind Waker !\nOn lui souhaite un 🎂 🎉 **JOYEUX ANNIVERSAIRE !** 🎉 🎂")
    
    if jour == 7 and mois == 12:
        await channel.send("Aujourd'hui, c'est l'anniversaire de **The Legend of Zelda : Spirit Tracks** <:st:1121789102208057395> !\nLe deuxième épisode sur DS, et la suite à Phantom Hourglass !\nOn lui souhaite un 🎂 🎉 **JOYEUX ANNIVERSAIRE !** 🎉 🎂")
    if jour == 11 and mois == 12:
        await channel.send("Aujourd'hui, c'est l'anniversaire de **The Legend of Zelda : Spirit Tracks** <:st:1121789102208057395> chez nous, en Europe !\nJe pense que vous êtes un certains nombre à l'avoir reçu pour Noël au vu de la date, non ? 🤭\nEn cette période de fête, on n'oublie pas de lui souhaiter un 🎂 🎉 **JOYEUX ANNIVERSAIRE !** 🎉 🎂")
    
    if jour == 18 and mois == 11:
        await channel.send("Aujourd'hui, c'est l'anniversaire de **The Legend of Zelda : Skyward Sword** <:ss:1121789139390582876> ! \nUn épisode au gameplay très spécial, et qui est surtout le tout début de la chronologie The Legend of Zelda, dont il est d'ailleurs à l'origine !\nIl mérite qu'on lui souhaite un 🎂 🎉 **JOYEUX ANNIVERSAIRE !** 🎉 🎂")
    
    if jour == 16 and mois == 8:
        await channel.send("Aujourd'hui, c'est l'anniversaire de **The Legend of Zelda : Skyward Sword HD** <:ss:1121789139390582876> !\nUn portage qui corrigera les principaux problèmes de gameplay à cause de la wiimote, grâce aux joycons !\nOn lui souhaite un 🎂 🎉 **JOYEUX ANNIVERSAIRE !** 🎉 🎂")
    
    if jour == 22 and mois == 11:
        await channel.send("Aujourd'hui, c'est l'anniversaire de **The Legend of Zelda : A Link Between Worlds** <:albw:1121789190179405975> !\nLE Zelda solo de la 3DS, qui reprend la même géographie de la map de A Link to the Past !\nOn lui souhaite un 🎂 🎉 **JOYEUX ANNIVERSAIRE !** 🎉 🎂")
    
    
    if jour == 22 and mois == 10:
        await channel.send("Aujourd'hui, c'est l'anniversaire de **The Legend of Zelda : TriForce Heroes** <:tfh:1121789215919845386> !\nLe Zelda multijoueur le plus récent de la franchise, où on pouvait jouer jusqu'à 3 Link dans la même carte ! Un jeu au potentiel de fun très sous-estimé.\nIl mérite qu'on lui souhaite un 🎂 🎉 **JOYEUX ANNIVERSAIRE !** 🎉 🎂")
    if jour == 23 and mois == 10:
        await channel.send("Aujourd'hui, c'est encore l'anniversaire de **The Legend of Zelda : TriForce Heroes** <:tfh:1121789215919845386>, mais cette fois-ci, chez nous, en Europe !\nIl mérite qu'on lui (re)souhaite un 🎂 🎉 **JOYEUX ANNIVERSAIRE !** 🎉 🎂")
    
    if jour == 3 and mois == 3:
        await channel.send("Aujourd'hui, c'est l'anniversaire de **The Legend of Zelda : Breath of The Wild** <:botw:1121789234731307020> !\nLe Zelda qui aura totalement cassé les codes que la saga avait adopté depuis A Link to the Past, et également le jeu qui aura mit l'exploration au premier plan !\nIl mérite qu'on lui souhaite un 🎂 🎉 **JOYEUX ANNIVERSAIRE !** 🎉 🎂")
    
    if jour == 14 and mois == 8:
        await channel.send("Aujourd'hui, c'est l'anniversaire de **Hyrule Warriors** <:hw:1121789291413123214> !\nLe premier spin-off hack'n'slash de la série ! Un jeu également rempli de fanservice !\nOn lui souhaite un 🎂 🎉 **JOYEUX ANNIVERSAIRE !** 🎉 🎂")
    if jour == 19 and mois == 9:
        await channel.send("Aujourd'hui, c'est l'anniversaire de **Hyrule Warriors** <:hw:1121789291413123214> chez nous, en Europe !\nQu'avez-vous pensé de ce spin-off de la saga ?\nOn lui souhaite un 🎂 🎉 **JOYEUX ANNIVERSAIRE !** 🎉 🎂")
    
    if jour == 13 and mois == 6:
        await channel.send("Aujourd'hui, c'est l'anniversaire de **Cadence of Hyrule** <:coh:1121789338615824454> !\nUn spin-off Zelda très sympa et basé sur le rythme !\nOn lui souhaite un 🎂 🎉 **JOYEUX ANNIVERSAIRE !** 🎉 🎂")
    
    if jour == 20 and mois == 11:
        await channel.send("Aujourd'hui, c'est l'anniversaire de **Hyrule Warriors : Age of Calamity** <:aoc:1121789303719198781> !\nUn Hyrule Warriors canon à la série Zelda qui se passe 100 ans avant les événements de Breath of the Wild !\nOn lui souhaite un 🎂 🎉 **JOYEUX ANNIVERSAIRE !** 🎉 🎂")
    
    if jour == 12 and mois == 5:
        await channel.send("@everyone\nAujourd'hui, c'est l'anniversaire de **The Legend of Zelda : Tears of the Kingdom <:totk:1121789258273935403> !**\nLa suite directe de la dernière révolution de la saga, et le dernier Zelda 3D en date !\nOn lui souhaite un 🎂 🎉 **JOYEUX ANNIVERSAIRE !** 🎉 🎂 ")


############################################################QUIZZ#######################################################################


class LancerQuizz(discord.ui.View):

    def __init__(self):
        super().__init__()
        self.value = None
        
    @discord.ui.button(label="Lancer le Quizz", style=discord.ButtonStyle.success, disabled=False)
    async def lancerQuizz1(self, button: discord.ui.Button, interaction: discord.Interaction):
        await lancer(interaction.channel)

    async def interaction_check(self, interaction: discord.Interaction, /) -> bool:
        await lancer(interaction.channel)

@bot.command()
async def quizz(ctx):
    print("ahaha")
    global msgLancer
    if(q.getQuizzTravaux()):
        await ctx.send("Le Quizz est en travaux ! Il sera bientôt disponible dans une nouvelle version !")
    else:
        await setclassement(ctx)
        if q.getQuizzEnCours() == False:
            view = LancerQuizz()
            q.setLancer(True)
            q.setQuizzEnCours(True)
            embed=discord.Embed(title="Le Quizz LonLon Coffee <:lonloncoffee:1139562304841711666>", color=0xC09866)
            embed.add_field(name="🟢 Questions faciles\n🟠 Questions moyennes\n🔴 Questions difficiles", value="Pour lancer une partie, cliquez sur le bouton en-dessous. On vous souhaite bonne chance !\nPS : Si vous êtes coincé, cliquez sur ❌", inline=True)
            message = await ctx.send(embed=embed)
            msgLancer = await ctx.send(view=view)
        else:
            await ctx.send("Un quiz est déjà en cours.")


def enleverImg(question):
    if "/img" in question:
        question = question.replace("/img", "")                  #efface le /img de la question             
        #efface cet index de la question
        question = question.replace(question[0], "")
        if question[0] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            question = question.replace(question[0], "")
            q.setDeuxNombres(True)
        q.setContientImage(True)
        print(q.getDeuxNombres())
    else:
        return question
    return question

@bot.command()
async def lancer(ctx):
    await msgLancer.delete()
    q.setDeuxNombres(False)
    if q.getLancer(): #Si true
        q.setLancer(False)
        tour = 1
        vieuxPoints = []
        questionsUtilisées = []
        questionsUtiliséesIndex = []    

        for i in cl.getTabJoueursObjet():
            vieuxPoints.append(i.getPoints())
        print(f"Vieux : {vieuxPoints}")
        for w in range(5): #Nombre de questions
            q.setDeuxNombres(False)
            q.setContientImage(False)
            #################################################POSE LA QUESTION
            alea = random.randint(0,len(q.getQuestions())-1)
            #print("QUESTION : ", q.getQuestions()[alea])
            question = enleverImg(q.getQuestions()[alea])
            print(questionsUtilisées)
            while(question in questionsUtilisées):
                q.setDeuxNombres(False)
                alea = random.randint(0,len(q.getQuestions())-1)
                question = enleverImg(q.getQuestions()[alea])      
                if question == enleverImg(q.getQuestions()[alea]): #Debug au cas où la 1ère question contienne /img, qu'elle est déjà dans questionsUtilisées, et que la prochaine ne contienne pas de /img mais que le programme considère qu'elle l'a
                    q.setContientImage(False)
                    q.setDeuxNombres(False)
            #print("sortie : ", question)
            
            questionImageTemporaire = q.getQuestions()[alea]
            question = enleverImg(questionImageTemporaire)
            if q.getContientImage() == True:
                if q.getDeuxNombres():
                    q.setDeuxNombres(False)
                    print(q.getDeuxNombres())
                    premierNombre = questionImageTemporaire[4]
                    deuxiemeNombre = questionImageTemporaire[5]
                    nombre = premierNombre + deuxiemeNombre
                    print(nombre)
                    q.setLienImage(q.getImages()[int(nombre)])
                else:
                    q.setLienImage(q.getImages()[int(questionImageTemporaire[4])])   #récupère le lien de l'image grâce à l'index présent au début de la question

            if q.getContientImage() == True:
                questionsUtilisées.append(question)
                questionsUtiliséesIndex.append(alea)
            else:
                questionsUtilisées.append(q.getQuestions()[alea])
                questionsUtiliséesIndex.append(alea) #Sert pour l'historique des questions posées à la fin.

            if q.getContientImage() == True:
                with open(q.getLienImage(), "rb") as fh:
                    f = discord.File(fh, filename=q.getLienImage())
                image = await ctx.send(file=f)

            rep = ""
            nb = 0
            random.shuffle(q.getReponses()[alea])
            for i in q.getReponses()[alea]:
                print(i)
                if i == q.getReponses()[alea][len(q.getReponses()[alea])-1]:
                    rep += "\n<:DD:946480161304506428> <:STX1:946414240699408466> "+ i + " ?"
                elif nb == 0:
                    rep += "<:AA:946480160830554123> <:STX1:946414240699408466> "+ i +  ","
                elif nb == 1:
                    rep += "\n<:BB:946480160763437056> <:STX1:946414240699408466> "+ i +  ","
                elif nb == 2:
                    rep += "\n<:CC:946480160922828850> <:STX1:946414240699408466> " + i +  ","
                nb+=1 
            try:
                if q.getContientImage() == True: 
                    questionImageTemp = questionImageTemporaire
                    questionImageTemp = enleverImg(questionImageTemp)
                    
                    embed=discord.Embed(title=questionImageTemp, color=0xC09866, description = f"**{rep}**\n\n<:STX5:945700963803611216> Répondez en cliquant sur les lettres")
                    message = await ctx.send(embed=embed)
                else:
                    embed=discord.Embed(title=q.getQuestions()[alea], color=0xC09866, description = f"**{rep}**\n\n<:STX5:945700963803611216> Répondez en cliquant sur les lettres")
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
                    reaction, user = await bot.wait_for('reaction_add', timeout=20.0 ,check=check)
                except asyncio.TimeoutError :
                    await ctx.send(f"Vous avez pris trop de temps ! **Question {w+1}** skipée.")
                    for i in cl.getTabJoueursObjet():
                        i.restartJouer()
                    await message.delete()
                    if q.getContientImage() == True:
                        await image.delete()
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
                    if q.getContientImage() == True:
                        await image.delete()

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
                    if q.getContientImage() == True:
                        await image.delete()

                else:
                    await ctx.send(f"Mauvaise réponse `{user.name}` !")
                    joueur.rmPointsToUser()
                    joueur.setAPerduPoint(True)
                    joueur.setJouer()

        rep = ""
        for i in range(len(questionsUtilisées)):
            rep = rep + f"**Question {i+1}** : {questionsUtilisées[i]}\n**Réponse** : {q.getBonneReponse()[questionsUtiliséesIndex[i]]}\n" + "\n"
        embed=discord.Embed(color=0xC09866)
        '''
        if q.getContientImage() == True:
            repImage = []
            for i in range(len(questionsUtilisées)):
                repImage[i] = questionsUtilisées[i]
            for i in range(len(repImage)):
                enleverImg(repImage[i])
            embed.add_field(name=f"Historique des questions", value=f"{repImage}", inline=True)
        '''
        embed.add_field(name=f"Historique des questions", value=f"{rep}", inline=True)
        try:
            assert vieuxPoints[0] #Si crash (ce qui veut dire qu'on est au premier lancement) -> except
            await ctx.send("Fin du Quizz !")
            historique = await ctx.send(embed=embed)
            if len(cl.getTabJoueursObjet()) == 1 and cl.getTabJoueursObjet()[0].getPoints() <= 0: #Si joueur gagne juste 0 point solo
                await ctx.send("Utilisez $classement pour connaître le classement du café sur les quizz !")
            else:
                for i in range(len(cl.getTabJoueursObjet())):
                    if vieuxPoints[i] > cl.getTabJoueursObjet()[i].getPoints():
                        await ctx.send(f"`{cl.getTabJoueursObjet()[i].getUser()}` a perdu {(vieuxPoints[i] - cl.getTabJoueursObjet()[i].getPoints())} points !")
                    elif vieuxPoints[i] < cl.getTabJoueursObjet()[i].getPoints():
                        await ctx.send(f"`{cl.getTabJoueursObjet()[i].getUser()}` a gagné {(cl.getTabJoueursObjet()[i].getPoints() - vieuxPoints[i])} points !")
                await ctx.send("Utilisez $classement pour connaître le classement du café sur les quizz !")
            
        except Exception as e:
            print(e)
            await ctx.send("Fin du Quizz !")
            historique = await ctx.send(embed=embed)
            await ctx.send("Utilisez $classement pour connaître le classement du café sur les quizz !")
        initialiserClassement()
        q.setLancer(False)
        q.setQuizzEnCours(False)

    else:
        await ctx.send("Vous devez lancer un quizz avec la commande $quizz pour accéder à cette commande. Utilisez $quizzhelp pour plus d'infos.")

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
        
        print(f"\n\TABJOUEURSOBJET : {cl.getTabJoueursObjet()}\n\n")
        print(f"TABLO : {tab}\n\n")
        for i in tab:
            print(i.getUser())
        print(f"Tab classement : {cl.getTabClassement()}\n\n")
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


# Fonction pour récupérer le top 10 des utilisateurs du Guess
def get_guess_top_10():
    cursor.execute('SELECT username, points FROM leaderboard ORDER BY points DESC LIMIT 10')
    return cursor.fetchall()

class ClassementView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(ClassementSelect())

class ClassementSelect(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label='Classement Quizz', value='quizz', description='Voir le classement du Quizz'),
            discord.SelectOption(label='Classement Guess', value='guess', description='Voir le classement du Guess')
        ]
        super().__init__(placeholder='Choisissez un classement...', min_values=1, max_values=1, options=options)

    async def callback(self, interaction):
        await interaction.response.defer()
        
        if self.values[0] == 'quizz':
            await self.show_quizz_classement(interaction)
        elif self.values[0] == 'guess':
            await self.show_guess_classement(interaction)
        
        await interaction.message.edit(content="Classement affiché ci-dessous:", view=None)

    async def show_quizz_classement(self, interaction):
        valeur = ""
        serverLogo = interaction.guild.icon.url
        try:
            if len(cl.getTabClassement()) > 10:  # Si il y a plus de 10 joueurs -> TOP 10 uniquement
                for i in range(10):
                    valeur = valeur + (f"**{i+1}** : `{cl.getTabClassement()[i].getUser()}` avec {cl.getTabClassement()[i].getPoints()} points.\n")
                valeur = valeur + (f"\nSi vous n'êtes pas dans le TOP 10, utilisez $place pour connaître votre classement !")
                embed = discord.Embed(title="**Classement du Quizz `(TOP 10)`**", color=0xC09866)
                embed.add_field(name=f"{len(cl.getTabClassement())} joueurs inscrits", value=valeur, inline=True)
                embed.set_thumbnail(url=(serverLogo))
                await interaction.followup.send(embed=embed)
            else:  # Sinon si c'est en dessous de 10, alors ça sera top len(classement)
                for i in range(len(cl.getTabClassement())):
                    valeur = valeur + (f"**{i+1}** : `{cl.getTabClassement()[i].getUser()}` avec {cl.getTabClassement()[i].getPoints()} points.\n")
                embed = discord.Embed(title="**Classement du Quizz**", color=0xC09866)
                embed.add_field(name=f"{len(cl.getTabClassement())} joueurs inscrits", value=valeur, inline=True)
                embed.set_thumbnail(url=(serverLogo))
                await interaction.followup.send(embed=embed)
        except:
            embed = discord.Embed(title="**Classement du Quizz**", color=0xC09866)
            embed.add_field(name=f"0 joueur inscrit", value="Aucune personne n'est dans le classement", inline=True)
            embed.set_thumbnail(url=(serverLogo))
            await interaction.followup.send(embed=embed)

    async def show_guess_classement(self, interaction):
        top_10 = get_guess_top_10()
        serverLogo = interaction.guild.icon.url
        if top_10:
            valeur = ""
            for i, (username, points) in enumerate(top_10, start=1):
                valeur = valeur + f"**{i}** : `{username}` avec {points} points.\n"
            embed = discord.Embed(title="**Classement du Guess `(TOP 10)`**", color=0xC09866)
            embed.add_field(name=f"{len(top_10)} joueurs inscrits", value=valeur, inline=True)
            embed.set_thumbnail(url=(serverLogo))
            await interaction.followup.send(embed=embed)
        else:
            embed = discord.Embed(title="**Classement du Guess**", color=0xC09866)
            embed.add_field(name="0 joueur inscrit", value="Aucune personne n'est dans le classement", inline=True)
            embed.set_thumbnail(url=(serverLogo))
            await interaction.followup.send(embed=embed)

@bot.command()
async def classement(ctx):
    view = ClassementView()
    await ctx.send("Choisissez un classement à afficher:", view=view)

class PlaceView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(PlaceSelect())

class PlaceSelect(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label='Place Quizz', value='quizz', description='Voir ta place dans le classement du Quizz'),
            discord.SelectOption(label='Place Guess', value='guess', description='Voir ta place dans le classement du Guess')
        ]
        super().__init__(placeholder='Choisissez un classement...', min_values=1, max_values=1, options=options)

    async def callback(self, interaction):
        await interaction.response.defer()

        if self.values[0] == 'quizz':
            await self.show_quizz_place(interaction)
        elif self.values[0] == 'guess':
            await self.show_guess_place(interaction)
        
        await interaction.message.edit(content="Classement affiché ci-dessous:", view=None)

    async def show_quizz_place(self, interaction):
        user_name = interaction.user.name
        placement, point = cl.getPlaceJoueurClassementEtPoints(user_name) # Pour récupérer classement + points
        pfp = interaction.user.avatar.url # Pour récupérer la pdp
        embed = discord.Embed(color=0xC09866)

        if placement == 1:
            embed.add_field(name="Ton classement", value=f"`{user_name}` tu es {placement}er(e) du classement avec {point} points !", inline=True)
        elif placement < 1:
            embed.add_field(name="Ton classement", value=f"`{user_name}` tu n'es pas classé avec...{point} point. Il faut avoir un score positif pour être classé.", inline=True)
        else:
            embed.add_field(name="Ton classement", value=f"`{user_name}` tu es {placement}ème du classement avec {point} points !", inline=True)
        
        embed.set_image(url=(pfp))
        await interaction.followup.send(embed=embed)

    async def show_guess_place(self, interaction):
        user_id = interaction.user.id
        cursor.execute('SELECT points FROM leaderboard WHERE user_id = ?', (str(user_id),))
        result = cursor.fetchone()
        
        if result:
            points = result[0]
            cursor.execute('SELECT COUNT(*) + 1 FROM leaderboard WHERE points > ?', (points,))
            placement = cursor.fetchone()[0]
        else:
            points = 0
            placement = -1
        
        pfp = interaction.user.avatar.url
        embed = discord.Embed(color=0xC09866)

        if placement == 1:
            embed.add_field(name="Ton classement", value=f"`{interaction.user.name}` tu es {placement}er(e) du classement avec {points} points !", inline=True)
        elif placement < 1:
            embed.add_field(name="Ton classement", value=f"`{interaction.user.name}` tu n'es pas classé avec...{points} point. Il faut avoir un score positif pour être classé.", inline=True)
        else:
            embed.add_field(name="Ton classement", value=f"`{interaction.user.name}` tu es {placement}ème du classement avec {points} points !", inline=True)
        
        embed.set_image(url=(pfp))
        await interaction.followup.send(embed=embed)

@bot.command()
async def place(ctx):
    view = PlaceView()
    await ctx.send("Choisissez un classement à afficher:", view=view)



'''@bot.command()
async def stopquizz(ctx):
    if q.getQuizzEnCours() == True:
        q.setLancer(False)
        q.setQuizzEnCours(False)
        await ctx.send("Quizz arrêté")'''


@bot.command()
async def helpquizz(ctx):
    embed=discord.Embed(color=0xC09866)
    embed.add_field(name="Commandes pour le fonctionnement du Quizz LonLon Coffee", value="`Pour lancer le quizz` : $quizz\n`Pour commencer le quizz` : $lancer\n`Pour connaître le classement du quizz`: $classement\n`Pour connaître votre place dans le classement` : $place\n`Pour arrêter le système du quizz` (A UTILISER EN CAS DE GROS PROBLEMES, NE PAS UTILISER SINON) : $stopquizz", inline=True)
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
    try:
        cl.resetTabJoueursObjet()
        tab = []
        with open("classement.txt", "r", encoding="utf-8") as f:
            for ligne in f:

                x = ligne.split(":")

                cl.ajouterJoueursId(x[0])

                user = await bot.fetch_user(x[0])

                cl.ajouterJoueurs(Joueur(user))
                
                tab.append(int(x[2])) #tablo des points de chaque joueur
                print(f"tab setclassement : {tab}")
                try:
                    j=0
                    for i in cl.getTabJoueursObjet():   
                        i.donnerNombrePoint(tab[j])
                        j+=1
                except Exception as e:
                    print(f"Erreur dans setclassement : {e}")
                print(cl.getTabJoueursObjet())
                print(f"taille : {len(cl.getTabJoueursObjet())}")
                initialiserClassement()
    except Exception as e:
        print(e)

######################################################################Musique


#####################################################################Ping

@bot.command()
async def ping(ctx):
    channelName = str(ctx.channel)
    channel = get(ctx.guild.channels, name=channelName)
    tab = {1059825385149321226 : 928401913182035999, #tloz (channel : role)
            1059825536395903016 : 928402198138863636, #aol
            1059825936608018552 : 928402618403942411, #alttp
            1059827532758790164 : 928402815943061634, #la
            1059827792537190430 : 928403095510196274, #oot
            1059828105822347304 : 928403211591778315, #mm
            1059831103298478200 : 928403296576757780, #ooa
            1059831316050366474 : 928403472477458482, #oos
            1059834770709819485 : 928403712693637151, #tww
            1059836385441353868 : 928403912195711066, #tmc
            #no FS
            1059841852351709234 : 928404096287924244, #fsa
            1059847618190135378 : 928404790336184380, #tp
            1059848574277533761 : 928404946729189378, #ph
            1059852802962239648 : 928405048931782676, #st
            1059853901731483720 : 928405127029751820, #ss
            1059857316859625592 : 928405234747838485, #albw
            1059858427909787739 : 928405518404423740, #tfh
            1059971869400387654 : 928405583432937483, #botw
            1060238945016893472 : 928405741121982524, #hw
            1060243138263928913 : 928406210925977651, #aoc
            774309114763018272 : 928405518404423740,
            }
    
    for i,j in tab.items():
        if(int(channel.id) == int(i)):
            print("beforeROLE")
            searched_role = get(ctx.guild.roles, id=j)
            await ctx.send(f"{searched_role.mention}")

@bot.event
async def on_message(message):
    if message.channel.id == 1080091500618194975 and message.author.id == 1080118704366419988:
        embed = message.embeds[0]
        msg = embed.title
        for word in msg.split():
            if(word == "[CG-Games-Project:equipe2-aubert-brizay-fraile]"):
                channel = bot.get_channel(1080496366041710594) #tournois
                await channel.send(embed=embed)
            elif(word == "[CG-Games-Project:equipe1-kicien-ramirez-reiner]"):
                channel = bot.get_channel(1080496408248979579) #stats
                await channel.send(embed=embed)
            elif(word == "[CG-Games-Project:equipe3-chapuisat-turner-viviers]"):
                channel = bot.get_channel(1080496332977999892) #param
                await channel.send(embed=embed)     
            elif(word == "[CG-Games-Project:equipe5-blanchet-ghiorghita-rodrigues]"):
                channel = bot.get_channel(1080496180447948911) #jeu6
                await channel.send(embed=embed)
            elif(word == "[CG-Games-Project:equipe4-belhamdi-chuewaye-cornet]"):
                channel = bot.get_channel(1080496303571746856) #jeu5
                await channel.send(embed=embed)
            elif(word == "[CG-Games-Project:equipe6-germain-pierrevelcin-vanhove]"):
                channel = bot.get_channel(1080496085996421180) #jeu7
                await channel.send(embed=embed)

            elif(word == "[CG-Games-Project:main]"):
                channel = bot.get_channel(1080496525970509904) #main
                await channel.send(embed=embed)

            elif(word == "[SAE-IAMSI/CG-Games-Project]"):
                channel = bot.get_channel(1080496497054990468) #mergequest
                await channel.send(embed=embed) 
            
    else:
        roles = ["$ping", "$tloz", "$aol", "$alttp", "$la", "$oot", "$mm", "$ooa", "$oos", "$tww", "$fs", "$fsa", "$tp", "$ph", "$st", "$ss", "$albw", "$tfh", "$botw", "$hw", "$aoc", "$coh"]
        if(str(message.content) in roles):
            await message.delete()
        await bot.process_commands(message)


@bot.command()
async def tloz(ctx):
    role = get(ctx.guild.roles, id=928401913182035999)
    await ctx.send(f"{role.mention}")

@bot.command()
async def aol(ctx):
    role = get(ctx.guild.roles, id=928402198138863636)
    await ctx.send(f"{role.mention}")

@bot.command()
async def alttp(ctx):
    role = get(ctx.guild.roles, id=928402618403942411)
    await ctx.send(f"{role.mention}")

@bot.command()
async def la(ctx):
    role = get(ctx.guild.roles, id=928402815943061634)
    await ctx.send(f"{role.mention}")   

@bot.command()
async def oot(ctx):
    role = get(ctx.guild.roles, id=928403095510196274)
    await ctx.send(f"{role.mention}")       

@bot.command()
async def mm(ctx):
    role = get(ctx.guild.roles, id=928403211591778315)
    await ctx.send(f"{role.mention}")

@bot.command()
async def ooa(ctx):
    role = get(ctx.guild.roles, id=928403296576757780)
    await ctx.send(f"{role.mention}")   

@bot.command()
async def oos(ctx):
    role = get(ctx.guild.roles, id=928403472477458482)
    await ctx.send(f"{role.mention}")  

@bot.command()
async def tww(ctx):
    role = get(ctx.guild.roles, id=928403712693637151)
    await ctx.send(f"{role.mention}")

@bot.command()
async def fs(ctx):
    role = get(ctx.guild.roles, id=928404319504596993)
    await ctx.send(f"{role.mention}")  

@bot.command()
async def fsa(ctx):
    role = get(ctx.guild.roles, id=928404096287924244)
    await ctx.send(f"{role.mention}")    

@bot.command()
async def tp(ctx):
    role = get(ctx.guild.roles, id=928404790336184380)
    await ctx.send(f"{role.mention}") 

@bot.command()
async def ph(ctx):
    role = get(ctx.guild.roles, id=928404946729189378)
    await ctx.send(f"{role.mention}")

@bot.command()
async def st(ctx):
    role = get(ctx.guild.roles, id=928405048931782676)
    await ctx.send(f"{role.mention}")

@bot.command()
async def ss(ctx):
    role = get(ctx.guild.roles, id=928405127029751820)
    await ctx.send(f"{role.mention}")

@bot.command()
async def albw(ctx):
    role = get(ctx.guild.roles, id=928405234747838485)
    await ctx.send(f"{role.mention}")

@bot.command()
async def tfh(ctx):
    role = get(ctx.guild.roles, id=928405518404423740)
    await ctx.send(f"{role.mention}")

@bot.command()
async def botw(ctx):
    role = get(ctx.guild.roles, id=928405583432937483)
    await ctx.send(f"{role.mention}")

@bot.command()
async def hw(ctx):
    role = get(ctx.guild.roles, id=928405741121982524)
    await ctx.send(f"{role.mention}")

@bot.command()
async def aoc(ctx):
    role = get(ctx.guild.roles, id=928406210925977651)
    await ctx.send(f"{role.mention}")

@bot.command()
async def coh(ctx):
    role = get(ctx.guild.roles, id=928406339804360764)
    await ctx.send(f"{role.mention}")


@bot.command()
async def modo(ctx):
    role = get(ctx.guild.roles, id=772462882859778068)
    await ctx.send(f"{role.mention}")

@bot.command()
@commands.has_role('𝐋𝐚 𝐑𝐞𝐝𝐚𝐜𝐭𝐢𝐨𝐧')
async def post(ctx):
    role = get(ctx.guild.roles, id=946460804629286932)
    await ctx.send(f"{role.mention}")
'''
zzz
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

c = Connection()
c.lancer(bot)