import sys

import discord

from scrybot.parser import parser
from scrybot import bot


args = parser.parse_args()

# Read the token from the provided file
try:
    with open(args.token_file, 'r') as file:
        token = file.read().strip()
except FileNotFoundError:
    print("Error: Token file not found.", file=sys.stderr)
    sys.exit(1)

# Check if the token is present
if not token:
    print("Error: Token not found in the provided file.", file=sys.stderr)
    sys.exit(1)

# Run the bot with the provided token
bot.run(token)