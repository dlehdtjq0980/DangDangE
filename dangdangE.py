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
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content.startswith("안녕하세요"):
        await message.channel.send("어서옵쇼!")


        
access_token = os.environ["BOT_TOKEN"]        
client.run(access_token)
