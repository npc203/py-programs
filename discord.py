#id:601962388006109195
#token:Z2bY5j2llRqGRU-xoZ_0hgcqLbwVZmjX


import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')

client = MyClient()
client.run('Z2bY5j2llRqGRU-xoZ_0hgcqLbwVZmjX')
