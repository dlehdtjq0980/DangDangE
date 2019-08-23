import discord
import os


client = discord.Client()



@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    print("~~~~~~~~~~~~~")
    
    game = discord.Game("크라우드한테 부려져 일")
    await client.change_presence(game=discord.Game(name='', type=1))


@client.event
async def on_message(message):
    if message.content.startswith("안녕하세요"):
        await client.send.message(message.channel, "안녕하세요")


        
access_token = os.environ["BOT_TOKEN"]        
client.run(access_token)
