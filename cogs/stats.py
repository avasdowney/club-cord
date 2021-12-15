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
		Service for getting details about users, channels, messages or any discord server related details. 
		View graphs/data visualizations related to server data
	"""

	def __init__(self, client):
		self.client = client

	def generate_message_stats(self, messages):
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

		#print(x)
		#print(y)	
		plt.figure(figsize=(15, 15))	
		plt.barh(x,y)
		plt.savefig('test.png')	
	

	@commands.Cog.listener()
	async def on_ready(self):
		print("Stats service is online ")

	
	@commands.command()
	async def cheer(self, ctx):	
		"""
		Randomly selects positive messages from a list an sends it to the server chat. 

		PARAMS
		ctx: Client wrapper object
		"""
		cheerymessage = ["You got this!", "Good job!", "Keep it up!", "You can accomplish all your goals", "If you put your mind to something, you can do it", "You're doing the best you can"]
		await ctx.send(random.choice(cheerymessage))

	
	@commands.command()
	async def channelstats(self, ctx):
		
		"""
		Sends bar chart image of users and message counts 

		PARAMS
		ctx: Client wrapper object
		"""
		messages = await self.client.get_channel(746034736660480030).history(limit=500).flatten()
		results = self.generate_message_stats(messages)
		self.generate_stats_chart(results)
		await ctx.send(file=discord.File('test.png'))
		

	@commands.command()
	async def users(self, ctx):
		"""
		Sends list of users in the discord server. Sends it to the #devops channel 

		PARAMS
		ctx: Client wrapper object
		"""
		user_list = [] 
		for user in self.client.users:
			user_list.append(user)

		for user in user_list:
			await ctx.send(user)


	@commands.command()
	async def channels(self, ctx):	
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
		print(text_channel)


	@commands.command()
	async def view_roles(self, ctx):	
		"""
		Sends list of roles in the discord server. Sends it to the #devops channel 

		PARAMS
		ctx: Client wrapper object
		"""
		roles_list = [] 
		for role in self.client.roles:
			roles_list.append(role)
		
		await ctx.send(roles_list) 


	@commands.command()
	async def help_test(self, ctx):
		"""
		Reads the README from the github repo and displays it as a message in the discord server. 
		
		PARAMS
		ctx: Client wrapper object
		"""
		# read readme.md file
		with open('README.md', 'r') as f:
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
