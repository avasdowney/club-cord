import discord
from discord.ext import commands
import markdown
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from pprint import pprint
import numpy as np
import datetime
import random


class Stats(commands.Cog):
	"""
	Stats service: 
		Service for getting details about users, channels, messages or any discord server related details. 
		View graphs/data visualizations related to server data

	So discord doesn't let us collect any message data/when it was sent, so we can't really do any stats RIP
	"""

	def __init__(self, client):
		self.client = client

	
	@commands.Cog.listener()
	async def on_ready(self):
		print("Stats service is online ")

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

		plt.figure(figsize=(15, 15))	
		plt.barh(x,y)
		plt.savefig('test.png')	

	
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

	
	@commands.command()
	async def audit_log_report(self, ctx):

		count = 0
		action_count = {}
		last_5 = []	
		for server in self.client.guilds:
			async for entry in server.audit_logs(limit=100):
				if str(entry.action) not in action_count.keys():
					action_count[str(entry.action)] = 1
				else:	
					action_count[str(entry.action)] += 1
				
				if count < 3:
					value = '*{}*  did  __{}__ '.format(entry.user.name, entry.action)
					last_5.append(value)

				count += 1

		msg = "AUDIT LOG REPORT, count of audit actions done. LIMIT 100\n\n"
		for item in action_count:
			msg += "__{}__  : **{}** \n".format(item, action_count[item])

		msg += " \n **Most recent actions:** \n"
		for item in last_5:
			msg += item + "\n"
		
		await ctx.send(msg)

		
		
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
		commands = readme.split('|')[7:][::3] # what is this wizardry?
		commands = [i.replace('<code>', '**').replace('</code>', '**').strip() for i in commands]
		explanations = readme.split('|')[8:][::3]
		explanations = [i.strip() for i in explanations]

		# return message in discord chat
		indices = len(commands)
		help_msg = ''
		for x in range(indices):
			help_msg = help_msg + '{}: {}\n'.format(commands[x], explanations[x])
		#print(help_msg)
		await ctx.send(help_msg)

	
	@commands.command()
	async def cheer(self, ctx):	
		"""
		Randomly selects positive messages from a list an sends it to the server chat. 

		PARAMS
		ctx: Client wrapper object
		"""
		cheerymessage = ["You got this!", "Good job!", "Keep it up!", "You can accomplish all your goals", "If you put your mind to something, you can do it", "You're doing the best you can"]
		await ctx.send(random.choice(cheerymessage))


def setup(client):
	client.add_cog(Stats(client))
