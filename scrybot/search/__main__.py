import sys
import asyncio

from scrybot.search import search_cards

def main():
    print(asyncio.run(search_cards(sys.argv[1])))

if __name__ == "__main__":
    main()