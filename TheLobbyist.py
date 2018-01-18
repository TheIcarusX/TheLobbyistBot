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
	if message.content.upper().startswith('!PING'):	
		userID = message.author.id
		await client.send_message(message.channel, "<@%s> Pong!" % (userID))

	if message.content.upper().startswith('!SAY'):
		args = message.content.split(" ")
		await client.delete_message(message)
		await client.send_message(message.channel, "%s" % (" ".join(args[1:])))

	if message.content.upper().startswith('!RULES'):
		userID = message.author.id
		await client.send_message(message.channel, "<@%s> See <#%s> for a full rundown of the Game Lobby rules!" % (userID,rulesID))

	if message.content.upper().startswith('!POGCHAMP'):
		await client.delete_message(message)
		await client.send_message(message.channel, "emote-id")

	if message.content.upper().startswith('!SUGGESTIONS'):
		userID = message.author.id
		await client.send_message(message.channel, "<@%s> See <#%s> to suggest new features for The Lobbyist!" % (userID,suggestionsID))

	if message.content.upper().startswith('!TEST'):	
		userID = message.author.id
		await client.send_message(message.channel, "<@%s> Testing!" % (userID))

	elif message.content.upper().startswith('!FLIP'):
		flip = random.choice(['Heads','Tails'])
		await client.send_message(message.channel, flip)

	elif message.content.upper().startswith('!ROLL'):
		roll = random.choice(['1','2','3','4','5','6'])
		await client.send_message(message.channel, roll)

	elif message.content.upper().startswith('!ADDQUOTE'):
		if not os.path.isfile("quote_file.pk1"):
			quote_list = []
		else:
			with open("quote_file.pk1", "r") as quote_file:
				quote_list = json.load(quote_file)
		quote_list.append(message.content[9:])
		with open("quote_file.pk1" , "w") as quote_file:
			json.dump(quote_list, quote_file)
	elif message.content.upper().startswith("!QUOTE"):
		with open("quote_file.pk1", "r") as quote_file:
			quote_list = json.load(quote_file)
		await client.send_message(message.channel, random.choice(quote_list))


client.run("token")
