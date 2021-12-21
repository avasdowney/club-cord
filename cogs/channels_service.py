import discord
from discord.ext import commands
import matplotlib.pyplot as plt
from pprint import pprint
from termcolor import colored
import numpy as np
import datetime
import random


class Channels(commands.Cog):
	"""
	Channels service:
		Wrappers for channel related data 

	"""

	def __init__(self, client):
		self.client = client

	
	@commands.Cog.listener()
	async def on_ready(self):
		print(colored("[+]", "green"), colored("Channels online ", "yellow"))

	
	@commands.command()
	async def get_channels(self, ctx):	
		"""
		Sends list of text channels in the discord server. Sends it to the #devops channel 

		PARAMS
		ctx: Client wrapper object
		"""
		text_channel = []
		for server in self.client.guilds:
			for channel in server.channels:
				if str(channel.type) == 'text':
					text_channel.append(channel)
		return text_channel

	
	def generate_channel_stats(self, messages):
		"""
		Creates a dictionary using the users as a key, the value is the amount of messages they've sent

		PARAMS
		messages: List of discord message objects
		"""
		message_dict = {}
		for item in messages:
			if item.author.name in message_dict:
				message_dict[item.author.name] += 1
			else:
				message_dict[item.author.name] = 1

		return message_dict


	
	def generate_stats_chart(self, chart_dict):
		"""
		Creats a bar chart of all users and the amount of messages that have been sent
	
		PARAMS
		chart_dict: Message dictionary, key value of user and message counts. This can be returned from the generate_message_stats() function above. 
		
		"""
		id_test = random.randint(1, 1000)
		x = [] 
		y = [] 
		for item in chart_dict.keys():
			x.append(item)
			y.append(chart_dict[item])

		plt.figure(figsize=(15, 15))	
		plt.barh(x,y)
		plt.savefig('test.png')

		
	@commands.command()
	async def channelstats(self, ctx):		
		"""
		Sends bar chart image of users and message counts 

		PARAMS
		ctx: Client wrapper object
		channel_name: Name of a channel
		"""
	
		messages = await self.client.get_channel(746034736660480030).history(limit=500).flatten()
		results = self.generate_channel_stats(messages)
		self.generate_stats_chart(results)
		await ctx.send(file=discord.File('test.png'))

	
	@commands.command()
	async def channel_activity_report(self, ctx):	
		"""
		Creates a channel activity report. Shows most active channels based on different messages sent in a certain time frame. 
		Mesaures the time from first and last message sent between users in a channel. 

		PARAMS
		ctx: Client wrapper object
	
		"""	
		channel_messages = {}
		message_lengths = {} 
		for server in self.client.guilds:
			for channel in server.channels:
				if str(channel.type) == "text":
					chan = self.client.get_channel(channel.id)
					messages = await chan.history(limit=20).flatten()
					first = messages[0].created_at
					last = messages[len(messages) - 1].created_at
					channel_messages[str(chan.name)] = first-last

		results = sorted(channel_messages.items(), key=lambda p: p[1])
		msg = " Message stats for each channel. Contains the name of the channel and the time frame. \nTime frame is the date from the first message sent to the last with a limit of 200+ messages. \n \n LIMIT: 20 \n\n"
		for r in results:
			val = "{} : {} \n".format("**" + r[0] + "**", r[1])
			msg += val

		await ctx.send(msg)



def setup(client):
	client.add_cog(Channels(client))
