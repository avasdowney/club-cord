import discord
from discord.ext import commands
import markdown
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import numpy as np
import random


class Stats(commands.Cog):

	"""
		Stats service: 
			Information about users, channels and server details
			Retrieve graphs about server statistics 
	"""

	def __init__(self, client):
		self.client = client

	# this just ranks the users that have sent the most messages in a channel
	def generate_message_stats(self, messages):
		# get general chat channel id
		message_dict = {}
		for item in messages:
			if item.author.name in message_dict:
				message_dict[item.author.name] += 1
			else:
				message_dict[item.author.name] = 1

		return message_dict

	def generate_stats_chart(self, chart_dict):
		id_test = random.randint(1, 1000)
		x = [] 
		y = [] 
		for item in chart_dict.keys():
			x.append(item)
			y.append(chart_dict[item])

		#print(x)
		#print(y)	
		plt.figure(figsize=(15, 15))	
		plt.barh(x,y)
		plt.savefig('test.png')	
	

	@commands.Cog.listener()
	async def on_ready(self):
		print("Stats service is online ")


	@commands.command()
	async def channelstats(self, ctx):
		messages = await self.client.get_channel(746034736660480030).history(limit=500).flatten()
		results = self.generate_message_stats(messages)
		self.generate_stats_chart(results)
		await ctx.send(file=discord.File('test.png'))
		

	@commands.command()
	async def users(self, ctx):
		user_list = [] 
		for user in self.client.users:
			user_list.append(user)

		for user in user_list:
			await ctx.send(user)


	@commands.command()
	async def channels(self, ctx):
		text_channel = []
		for server in self.client.guilds:
			for channel in server.channels:
				if str(channel.type) == 'text':
					text_channel.append(channel)
		print(text_channel)


	@commands.command()
	async def view_roles(self, ctx):
		roles_list = [] 
		for role in self.client.roles:
			roles_list.append(role)
		
		await ctx.send(roles_list) 


	@commands.command()
	async def help_test(self, ctx):
		# read readme.md file
		with open('../README.md', 'r') as f:
			text = f.read()
			html = markdown.markdown(text)
		soup = BeautifulSoup(html, "html")

		# retrieve useful info
		readme = soup.find_all('p')
		readme = (str)(readme.pop(1)) 
		commands = readme.split('|')[7:][::3]
		commands = [i.replace('<code>', '**').replace('</code>', '**').strip() for i in commands]
		explanations = readme.split('|')[8:][::3]
		explanations = [i.strip() for i in explanations]

		# return message in discord chat
		indices = len(commands)
		help_msg = ''
		for x in range(indices):
			help_msg = help_msg + '{}: {}\n'.format(commands[x], explanations[x])
		print(help_msg)

		await ctx.send(help_msg)


def setup(client):
	client.add_cog(Stats(client))