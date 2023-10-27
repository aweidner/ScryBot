import discord
from discord.ext import commands

intents = discord.Intents(messages=True)

# Create a bot instance with a command prefix
bot = commands.Bot(command_prefix='!!', intents=intents)
