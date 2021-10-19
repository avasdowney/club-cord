import discord
from pprint import pprint

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

text_channels = []
all_users = []  

def view_channels(type: str) -> list:

    text_channels = [] 

    for server in client.guilds:
        for channel in server.channels:
            if str(channel.type) == 'text':
                text_channels.append(channel)

    return text_channels

@client.event
async def view_messages_by_channel(channel):
    messages = await channel.history(limit=10).flatten()
    print(messages)
            

def view_users():
    user_list = [] 
    for user in client.users:
        user_list.append(user)
    
    return user_list 


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
    
    if message.content.startswith("$carter"):
        await message.channel.send('lame')

    if message.content.startswith("$channels"):
        results = view_channels('text')
        print(results)
        test_channel = results[0]
        await view_messages_by_channel(test_channel)

    # return all users 
    if message.content.startswith("$users"):
        results = view_users()
        test_user = results[1]


        #result = await client.fetch_user_profile(test_user.id)
        #pprint(result) 
    
        #pprint(test_user)
        

        #res = await client.fetch_user_profile(test_user["id"])
        #pprint(res)
        #for item in results:
        #    await message.channel.send(item["username"])

    
        


client.run("ODk5MzkxMTU2NDY1NTc4MDA0.YWyFSQ.sXiiOiGvi_b_F4MIkLtwQHIlCJM")


