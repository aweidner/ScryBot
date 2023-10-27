import sys
import os

from scrybot import bot

# Run the bot with the provided token
token = os.environ.get('DISCORD_BOT_TOKEN')
bot.run(token)