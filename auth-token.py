import discord
from pprint import pprint
from message import MessageMiner
import random
from discord.utils import get
import markdown
from bs4 import BeautifulSoup

try:
	import ConfigParser
except:
	import configparser as ConfigParser
import sys


text_channels = []
all_users = []	

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)


def view_channels(type: str) -> list:

	text_channels = [] 

	for server in client.guilds:
		for channel in server.channels:
			if str(channel.type) == 'text':
				text_channels.append(channel)

	return text_channels

def view_users():
	user_list = [] 
	for user in client.users:
		user_list.append(user)
	
	return user_list 

def view_roles():
	roles_list = [] 
	for role in client.roles:
		roles_list.append(role)
	
	return roles_list 

@client.event
async def view_messages_by_channel(channel):
	messages = await channel.history(limit=10).flatten()
	for message in messages:
		#print(message.id)
		await channel.fetch_message(message.id)

@client.event
async def on_ready():
	print('Logged in as {0.user}'.format(client))

# how do we get user info?
@client.event
async def on_message(message):
	if message.author == client.user:
		return

	# return hello message
	if message.content.startswith('$hello'):
		await message.channel.send('Hello!')
	
	# return channels
	if message.content.startswith("$channels"):
		results = view_channels('text')
		channel_msg = ''
		for item in results:
			channel_msg += "Name: {}, Id: {} \n".format(item.name, item.id)
		await message.channel.send(channel_msg)

	# return all users 
	if message.content.startswith("$users"):
		results = view_users()
		user_msg = ''
		for item in results:
			user_msg += '{} \n'.format(item.name)
		await message.channel.send(user_msg)
	
	# BROKEN
	# return all roles
	if message.content.startswith("$roles"):
		roles = view_roles()
		for item in roles:
			await message.channel.send(item)

	# return random cheery message	
	if message.content.startswith("$cheer"):
		cheerymessage = ["You got this!", "Good job!", "Keep it up!", "You can accomplish all your goals", "If you put your mind to something, you can do it", "You're doing the best you can"]
		await message.channel.send(random.choice(cheerymessage))

	# return graph of channel message count		
	if message.content.startswith("$channelmessage"):
		messages = await client.get_channel(746034736660480030).history(limit=500).flatten()

		instance = MessageMiner(messages)
		results = instance.generate_message_stats()
		#pprint(results)
		#test = str(results)
		#await message.channel.send(test)
		instance.generate_stats_chart(results)
		await message.channel.send(file=discord.File('test.png'))
		"""
		for item in messages:
			#print(type(item))
			print("Message Content: ", item.content)
			print("Author: ", item.author)
			print("Activity: ", item.activity)	
			print("Reactions: ", item.reactions)
			print("Embeds: ", item.embeds)
			print("====================================================================")

		"""

	# pull commands from readme.md file
	if message.content.startswith("$help"):

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
		await message.channel.send(help_msg)

# set up auth token
config = ConfigParser.RawConfigParser()
config.read('./token.conf')

try:
	bot_token = config.get('clubcord', 'bot_token')
except ConfigParser.NoOptionError:
	print('Could not read configuration file.')
	sys.exit(1)
 
client.run(bot_token)


