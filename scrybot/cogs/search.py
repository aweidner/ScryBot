from discord.ext import commands

from scrybot.api.named import search_cards
from scrybot.api.search import search

import requests
import urllib
from urllib.parse import urlparse, urlunparse


def translate_url(api_url):
    parsed_url = urlparse(api_url)
    
    # Remove 'api.' prefix from netloc (domain)
    new_netloc = parsed_url.netloc.replace('api.', '', 1)
    
    # Remove '/cards' from path
    new_path = parsed_url.path.replace('/cards', '', 1)
    
    # Construct the new URL
    new_url = urlunparse((parsed_url.scheme, new_netloc, new_path, 
                          parsed_url.params, parsed_url.query, parsed_url.fragment))
    
    return new_url


def encode_url(url):
    # Parse the URL into its components
    parsed_url = urllib.parse.urlparse(url)
    
    # Parse the query string into a dictionary
    query_params = urllib.parse.parse_qs(parsed_url.query)
    
    # Convert the dictionary back to a query string, properly encoded
    encoded_query = urllib.parse.urlencode(query_params, doseq=True, quote_via=urllib.parse.quote)
    
    # Construct the new URL with the encoded query string
    new_url = parsed_url._replace(query=encoded_query).geturl()
    
    return new_url


class SearchCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        async with message.channel.typing():
            if str(self.bot.user.id) in message.content:
                result = await search(message.content)
                url = encode_url(result["content"])
                response = requests.get(url)
                if response.status_code == 200:
                    # TODO: If this is less than like 3 cards, output the card image.  Otherwise output
                    # The full link
                    translated_url = translate_url(url)
                    await message.channel.send(translated_url, reference=message)
                else:
                    body = response.json()
                    details = body["details"]
                    await message.channel.send("\n".join([f"Requested: {url}", details]), reference=message)
            else:
                images = await search_cards(message.content)
                
                if images:
                    await message.channel.send("\n".join(images), reference=message)