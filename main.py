import discord
from discord.ext import commands
from discord.ext.commands import Bot,has_permissions
import dotenv
import os

dotenv.load_dotenv()


intents = discord.Intents.default().all()
intents.members = True

description = "ASDSD"

client = Bot(command_prefix='@',description=description, intents=intents)

# @client.event
# async def on_ready():
#     print(f'We have logged in as {client.user}')

@client.command()
async def szia(ctx): 
    await ctx.send("asdasd")


# The below code bans player.
@client.command()
@has_permissions(ban_members=True)
async def ban(self, ctx, member: discord.Member, *, reason=None):
     await member.ban(reason=reason)
     await ctx.send(f'User {member} has been kick')

client.run(os.environ.get("DISCORD_BOT_TOKEN"))

