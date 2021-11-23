import discord
from pprint import pprint
from message import MessageMiner
import random
from discord.utils import get

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

	if message.content.startswith('$hello'):
		await message.channel.send('Hello!')
	
	if message.content.startswith("$channels"):
		results = view_channels('text')
		for item in results:
			#print(type(item))
			print("Name: {}, Id: {} ".format(item.name, item.id))

	# return all users 
	if message.content.startswith("$users"):
		results = view_users()
		for item in results:
			print(item.name)
	
	if message.content.startswith("$roles"):
		roles = view_roles()
		for item in roles:
			print(item)
			
	if message.content.startswith("$cheer"):
		cheerymessage = ["You got this!", "Good job!", "Keep it up!", "You can accomplish all your goals", "If you put your mind to something, you can do it", "You're doing the best you can"]
		print(random.choice(cheerymessage))
			
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

	# add your commands to this function after fully implemented
	# also add your commmand and function to the readme.md file
	if message.content.startswith("$help"):
		await message.channel.send('$help, $hello, $channels, $users, $channelmessage')
	
			

	




# set up auth token
config = ConfigParser.RawConfigParser()
config.read('./token.conf')

try:
	bot_token = config.get('clubcord', 'bot_token')
except ConfigParser.NoOptionError:
	print('Could not read configuration file.')
	sys.exit(1)
 
client.run(bot_token)


