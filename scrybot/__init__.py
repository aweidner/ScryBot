import discord
from discord.ext import commands

from scrybot.cogs import SearchCog


intents = discord.Intents(messages=True, message_content=True)

# Create a bot instance with a command prefix
bot = commands.Bot(command_prefix='!!', intents=intents)

@bot.event
async def on_ready():
    await bot.add_cog(SearchCog(bot))
    print("All cogs added")