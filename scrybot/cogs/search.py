from discord.ext import commands


class SearchCog(commands.Cog):
    def __init__(self, bot, channel_name):
        self.bot = bot
        self.channel_name = channel_name

    @commands.Cog.listener()
    async def on_message(self, message):
        # Check if the message is from the specified channel and not from the bot itself
        if message.channel.name == self.channel_name and message.author != self.bot.user:
            await self.process_message(message.content)

    async def process_message(self, message_content):
        # This function is called when a new message is received in the specified channel
        # For now, the function body is empty
        pass
