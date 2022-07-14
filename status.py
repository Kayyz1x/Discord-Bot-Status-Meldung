import discord
from discord.ext import commands

client = commands.Bot(command_prefix = 'u')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('UltraScripts'))
    print('Online')

client.run('Token')
