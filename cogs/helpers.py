import discord
from discord.ext import commands
import markdown
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from pprint import pprint
import numpy as np
import datetime
import random


class Helpers(commands.Cog):
	"""
	Helper service:
		Main help meny for bot. Functions to show how each service works 
	"""

	def __init__(self, client):
		self.client = client

	
	@commands.Cog.listener()
	async def on_ready(self):
		print("Helper service is online ")
	
	@commands.command()
	async def clubcord_help(self, ctx):
		"""
		Reads the README from the github repo and displays it as a message in the discord server. 
		
		PARAMS
		ctx: Client wrapper object
		"""
		# read readme.md file
		with open('README.md', 'r') as f:
			text = f.read()
			html = markdown.markdown(text)
		soup = BeautifulSoup(html, "html.parser")

		# retrieve useful info
		readme = soup.find_all('p')
		readme = (str)(readme.pop(7)) # this will need to be changed if more gets added to readme above the table
		commands = readme.split('|')[7:][::3] # what is this wizardry? <-- it chops off the first 7 and last three cells of the readme table
		commands = [i.replace('<code>', '**').replace('</code>', '**').strip() for i in commands]
		explanations = readme.split('|')[8:][::3]
		explanations = [i.strip() for i in explanations]

		# return message in discord chat
		indices = len(commands)
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
	client.add_cog(Helpers(client))
