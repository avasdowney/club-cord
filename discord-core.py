import discord


intents = discord.Intents.default()
intents.members = True
TOKEN = "ODk5MzkxMTU2NDY1NTc4MDA0.YWyFSQ.sXiiOiGvi_b_F4MIkLtwQHIlCJM" 

# Core lib for discord py essentials ~ Shay

class PyCordClient(discord.Client):

    # view channels by text or voice
    def view_channels(self, channel_type: str) -> list:
        text_channels = [] 
        for server in client.guilds:
            for channel in server.channels:
                if str(channel.type) == 'text':
                    text_channels.append(channel)

        return text_channels

    async def view_message(self, text_channel, message_id):
        # message_id: Id of the message
        result = await text_channel.fetch_message(message_id)
        print(result)
 
    async def view_messages_by_channel(self, channel) -> list:
        messages = await channel.history(limit=10).flatten()
        return messages
    
    async def on_ready(self):
        print(f'Logged in as {self.user}')

    # equivalent of our main method 
    async def on_message(self, message):
        if message.author == client.user:
            return

        if message.content.startswith('$hello'):
            await message.channel.send('Hello!')
    
        if message.content.startswith("$carter"):
            await message.channel.send('lame')

        if message.content.startswith("$channels"):
            results = self.view_channels('text')
            #print(results)
            test_channel = results[0]
            message_by_channel = await self.view_messages_by_channel(test_channel)
            single_message = message_by_channel[3] 
            print(single_message.id)
            testing = await self.view_message(test_channel, single_message.id)
            print(testing)

        # return all users 
        if message.content.startswith("$users"):
            results = view_users()
            test_user = results[1]

client = PyCordClient()
client.run(TOKEN)
