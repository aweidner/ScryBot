import json
import re
import requests
import concurrent.futures
import sys
import asyncio

def fetch_card_info(card_name):
    url = f"https://api.scryfall.com/cards/named?fuzzy={card_name}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch {card_name}: Status code {response.status_code}")
        return None

def get_card_info(card_names):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(fetch_card_info, card_names))
    return results

def find_bracketed_text(input_string):
    # Define the regular expression pattern
    pattern = re.compile(r'\[\[(.*?)\]\]')
    
    # Search for all matches in the input string
    matches = pattern.findall(input_string)

    return matches

async def search_cards(content):
    potential_cards = find_bracketed_text(content)
    results = get_card_info(potential_cards)

    images = []
    for card in results:
        if not card:
            continue

        # Check if 'image_uris' key exists in the card dictionary
        if 'image_uris' in card:
            # Add the 'image_uris' dictionary to the result list
            images.append(card['image_uris']['normal'])
            continue

        if 'card_faces' in card:
            for face in card['card_faces']:
                if 'image_uris' in face:
                    images.append(face['image_uris']['normal'])
                    continue

    return images

def main():
    print(asyncio.run(search_cards(sys.argv[1])))

if __name__ == "__main__":
    main()