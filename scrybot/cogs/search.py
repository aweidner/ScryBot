from discord.ext import commands

from scrybot.api.named import search_cards

class SearchCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        images = await search_cards(message.content)
        
        if images:
            await message.channel.send("\n".join(images), reference=message)