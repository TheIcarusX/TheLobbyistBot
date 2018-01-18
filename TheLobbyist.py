import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

import json
import os
import random

#Client = discord.Client() 
client = discord.Client() 
#client = commands.Bot(command_prefix = "!")
bot = commands.Bot(command_prefix = "!")
rulesID = 'rules-channel-id'
suggestionsID = 'suggestions-channel-id'
#prefix = "!"


@client.event 
async def on_ready():
    print("Bot is online and connected to Discord")

@client.event
async def on_message(message):
    messageDetector = message.content.upper().startswith
    messageSend = client.send_message
    messageDelete = client.delete_message
    if messageDetector('!PING'):
        userID = message.author.id
        await messageSend(message.channel, "<@%s> Pong!" % (userID))

    if messageDetector('!SAY'):
        args = message.content.split(" ")
        await messageDelete(message)
        await messageSend(message.channel, "%s" % (" ".join(args[1:])))

    if messageDetector('!RULES'):
        userID = message.author.id
        await messageSend(message.channel, "<@%s> See <#%s> for a full rundown of the Game Lobby rules!" % (userID,rulesID))

    if messageDetector('!POGCHAMP'):
        await messageDelete(message)
        await messageSend(message.channel, "emote-id")

    if messageDetector('!SUGGESTIONS'):
        userID = message.author.id
        await messageSend(message.channel, "<@%s> See <#%s> to suggest new features for The Lobbyist!" % (userID,suggestionsID))

    if messageDetector('!TEST'): 
        userID = message.author.id
        await messageSend(message.channel, "<@%s> Testing!" % (userID))

    elif messageDetector('!FLIP'):
        flip = random.choice(['Heads','Tails'])
        await messageSend(message.channel, flip)

    elif messageDetector('!ROLL'):
        roll = random.choice(['1','2','3','4','5','6'])
        await messageSend(message.channel, roll)

    elif messageDetector('!ADDQUOTE'):
        if not os.path.isfile("quote_file.pk1"):
            quote_list = []
        else:
            with open("quote_file.pk1", "r") as quote_file:
                quote_list = json.load(quote_file)
        quote_list.append(message.content[9:])
        with open("quote_file.pk1" , "w") as quote_file:
            json.dump(quote_list, quote_file)
    elif messageDetector("!QUOTE"):
        with open("quote_file.pk1", "r") as quote_file:
            quote_list = json.load(quote_file)
        await messageSend(message.channel, random.choice(quote_list))


client.run("token")


