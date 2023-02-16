import discord
import dotenv

client = discord.Client()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.command()
async def szia(ctx): 
    await ctx.send("asdasd")


client.run('your token here')

