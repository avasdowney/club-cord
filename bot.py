import discord
import os
from discord.ext import commands

try:
    import ConfigParser
except:
    import configparser as ConfigParser
import sys

# intents needs to be set to true for bot to view ALL users. 
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix="$", intents=intents)

@client.command()
async def load(ctx, extension):
	client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
	client.unload_extension(f'cogs.{extension}')

# load extensions
for filename in os.listdir('./cogs'):
	if filename.endswith('.py'):
		file_split = filename.split('.')
		name = file_split[0]
		client.load_extension(f'cogs.{name}')


# set up auth token using config parser
config = ConfigParser.RawConfigParser()
config.read('./token.conf')

# grab auth token details from token.conf file
try:
    bot_token = config.get('clubcord', 'bot_token')
except ConfigParser.NoOptionError:
    print('Could not read configuration file.')
    sys.exit(1)

client.run(bot_token)	
