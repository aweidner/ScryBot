import random

def colorProvider(identity=False):
    # Define the MTG colors and nicknames for color combinations
    colors = ["red", "blue", "green", "black", "white"]
    color_combinations = {
        'azorius': ['white', 'blue'],
        'dimir': ['blue', 'black'],
        'rakdos': ['black', 'red'],
        'gruul': ['red', 'green'],
        'selesnya': ['green', 'white'],
        'orzhov': ['white', 'black'],
        'izzet': ['blue', 'red'],
        'golgari': ['black', 'green'],
        'boros': ['red', 'white'],
        'simic': ['green', 'blue'],
        'bant': ['white', 'blue', 'green'],
        'esper': ['white', 'blue', 'black'],
        'grixis': ['blue', 'black', 'red'],
        'jund': ['black', 'red', 'green'],
        'naya': ['red', 'green', 'white'],
        'abzan': ['white', 'black', 'green'],
        'jeskai': ['blue', 'red', 'white'],
        'sultai': ['black', 'green', 'blue'],
        'mardu': ['red', 'white', 'black'],
        'temur': ['green', 'blue', 'red'],
        'chaos': ['blue', 'black', 'red', 'green'],
        'aggression': ['black', 'red', 'green', 'white'],
        'altruism': ['red', 'green', 'white', 'blue'],
        'growth': ['green', 'white', 'blue', 'black'],
        'artifice': ['white', 'blue', 'black', 'red']
    }

    corid = "color" if not identity else "id"

    # Step 1: Pick the first color, with a 3% chance of being colorless
    if random.random() < 0.03:
        return "colorless"
    else:
        chosen_colors = [random.choice(colors)]

    # Step 2 to 5: Decide how many more colors to pick
    probabilities = [1, 0.2, 0.05, 0.025]  # Probabilities for 2nd, 3rd, 4th and 5th color
    for prob in probabilities:
        if random.random() < prob:
            # Pick a new color that is not already chosen
            new_color = random.choice([color for color in colors if color not in chosen_colors])
            chosen_colors.append(new_color)
        else:
            break

    # Step 6: Decide whether to collapse the colors into MTG nicknames
    if len(chosen_colors) > 1 and random.random() < 0.5:
        # Try to find a nickname for the color combination
        for nickname, combo in color_combinations.items():
            if sorted(chosen_colors) == sorted(combo):
                return f"{corid}:{nickname}"
        # If no nickname is found, fall through to returning the string of colors

    # Return a string with the chosen colors
    if len(chosen_colors) > 1:
        corid = "color"

    return ' '.join(f"{corid}:{color}" for color in chosen_colors)


def spellPermanantHistoricAdornment():
    adornments = ["spell", "permanent", "historic"]

    return random.choice(adornments)


def landTypeProvider():
    types = ["Basic", "Snow", "Legendary"]

    return random.choice(types)


def creatureTypeProvider():
    types = ["Advisor",
    "Aetherborn",
    "Alien",
    "Ally",
    "Angel",
    "Antelope",
    "Ape",
    "Archer",
    "Archon",
    "Army",
    "Artificer",
    "Assassin",
    "Assembly-Worker",
    "Astartes",
    "Atog",
    "Aurochs",
    "Automaton",
    "Avatar",
    "Azra",
    "Badger",
    "Balloon",
    "Barbarian",
    "Bard",
    "Basilisk",
    "Bat",
    "Bear",
    "Beast",
    "Beeble",
    "Beholder",
    "Berserker",
    "Bird",
    "Blinkmoth",
    "Boar",
    "Brainiac",
    "Bringer",
    "Brushwagg",
    "C'tan",
    "Camarid",
    "Camel",
    "Capybara",
    "Caribou",
    "Carrier",
    "Cat",
    "Centaur",
    "Cephalid",
    "Chicken",
    "Child",
    "Chimera",
    "Citizen",
    "Cleric",
    "Clown",
    "Cockatrice",
    "Construct",
    "Coward",
    "Crab",
    "Crocodile",
    "Custodes",
    "Cyberman",
    "Cyclops",
    "Dalek",
    "Dauthi",
    "Demigod",
    "Demon",
    "Deserter",
    "Detective",
    "Devil",
    "Dinosaur",
    "Djinn",
    "Doctor",
    "Dog",
    "Dragon",
    "Drake",
    "Dreadnought",
    "Drone",
    "Druid",
    "Dryad",
    "Dwarf",
    "Efreet",
    "Egg",
    "Elder",
    "Eldrazi",
    "Elemental",
    "Elephant",
    "Elf",
    "Elk",
    "Employee",
    "Eye",
    "Faerie",
    "Ferret",
    "Fish",
    "Flagbearer",
    "Fox",
    "Fractal",
    "Frog",
    "Fungus",
    "Gamer",
    "Gargoyle",
    "Germ",
    "Giant",
    "Gith",
    "Gnoll",
    "Gnome",
    "Goat",
    "Goblin",
    "God",
    "Golem",
    "Gorgon",
    "Graveborn",
    "Gremlin",
    "Griffin",
    "Guest",
    "Hag",
    "Halfling",
    "Hamster",
    "Harpy",
    "Head",
    "Hellion",
    "Hippo",
    "Hippogriff",
    "Homarid",
    "Homunculus",
    "Hornet",
    "Horror",
    "Horse",
    "Human",
    "Hydra",
    "Hyena",
    "Illusion",
    "Imp",
    "Incarnation",
    "Inkling",
    "Inquisitor",
    "Insect",
    "Jackal",
    "Jellyfish",
    "Juggernaut",
    "Kavu",
    "Kirin",
    "Kithkin",
    "Knight",
    "Kobold",
    "Kor",
    "Kraken",
    "Lamia",
    "Lammasu",
    "Leech",
    "Leviathan",
    "Lhurgoyf",
    "Licid",
    "Lizard",
    "Manticore",
    "Masticore",
    "Mercenary",
    "Merfolk",
    "Metathran",
    "Minion",
    "Minotaur",
    "Mite",
    "Mole",
    "Monger",
    "Mongoose",
    "Monk",
    "Monkey",
    "Moonfolk",
    "Mouse",
    "Mutant",
    "Myr",
    "Mystic",
    "Naga",
    "Nautilus",
    "Necron",
    "Nephilim",
    "Nightmare",
    "Nightstalker",
    "Ninja",
    "Noble",
    "Noggle",
    "Nomad",
    "Nymph",
    "Octopus",
    "Ogre",
    "Ooze",
    "Orb",
    "Orc",
    "Orgg",
    "Otter",
    "Ouphe",
    "Ox",
    "Oyster",
    "Pangolin",
    "Peasant",
    "Pegasus",
    "Pentavite",
    "Performer",
    "Pest",
    "Phelddagrif",
    "Phoenix",
    "Phyrexian",
    "Pilot",
    "Pincher",
    "Pirate",
    "Plant",
    "Praetor",
    "Primarch",
    "Prism",
    "Processor",
    "Rabbit",
    "Raccoon",
    "Ranger",
    "Rat",
    "Rebel",
    "Reflection",
    "Reveler",
    "Rhino",
    "Rigger",
    "Robot",
    "Rogue",
    "Sable",
    "Salamander",
    "Samurai",
    "Sand",
    "Saproling",
    "Satyr",
    "Scarecrow",
    "Scientist",
    "Scion",
    "Scorpion",
    "Scout",
    "Sculpture",
    "Serf",
    "Serpent",
    "Servo",
    "Shade",
    "Shaman",
    "Shapeshifter",
    "Shark",
    "Sheep",
    "Siren",
    "Skeleton",
    "Slith",
    "Sliver",
    "Slug",
    "Snail",
    "Snake",
    "Soldier",
    "Soltari",
    "Spawn",
    "Specter",
    "Spellshaper",
    "Sphinx",
    "Spider",
    "Spike",
    "Spirit",
    "Splinter",
    "Sponge",
    "Spy",
    "Squid",
    "Squirrel",
    "Starfish",
    "Surrakar",
    "Survivor",
    "Teddy",
    "Tentacle",
    "Tetravite",
    "Thalakos",
    "Thopter",
    "Thrull",
    "Tiefling",
    "Time Lord",
    "Treefolk",
    "Trilobite",
    "Triskelavite",
    "Troll",
    "Turtle",
    "Tyranid",
    "Unicorn",
    "Urzan",
    "Vampire",
    "Vedalken",
    "Viashino",
    "Volver",
    "Wall",
    "Walrus",
    "Warlock",
    "Warrior",
    "Wasp",
    "Weird",
    "Werewolf",
    "Whale",
    "Wizard",
    "Wolf",
    "Wolverine",
    "Wombat",
    "Worm",
    "Wraith",
    "Wurm",
    "Yeti",
    "Zombie",
    "Zubera"]

    first = random.choice(types)

    # 50% chance to choose a second type
    if random.random() < 0.1:
        second = random.choice(types)
        while second == first:
            second = random.choice(types)
        return f"type:{first} type:{second}"
    else:
        return f"type:{first}"


def keywordAbilityProvider():
    abilities = ["Living weapon",
    "Jump-start",
    "Discover",
    "Commander ninjutsu",
    "Legendary landwalk",
    "Nonbasic landwalk",
    "Totem armor",
    "Megamorph",
    "Haunt",
    "Forecast",
    "Graft",
    "Fortify",
    "Frenzy",
    "Gravestorm",
    "Hideaway",
    "Level Up",
    "Infect",
    "Reach",
    "Rampage",
    "Phasing",
    "Multikicker",
    "Morph",
    "Provoke",
    "Modular",
    "Ninjutsu",
    "Replicate",
    "Recover",
    "Poisonous",
    "Prowl",
    "Reinforce",
    "Persist",
    "Retrace",
    "Rebound",
    "Miracle",
    "Overload",
    "Outlast",
    "Prowess",
    "Renown",
    "Myriad",
    "Shroud",
    "Trample",
    "Vigilance",
    "Shadow",
    "Storm",
    "Soulshift",
    "Splice",
    "Transmute",
    "Ripple",
    "Suspend",
    "Vanishing",
    "Transfigure",
    "Wither",
    "Undying",
    "Soulbond",
    "Unleash",
    "Ascend",
    "Assist",
    "Afterlife",
    "Companion",
    "Fabricate",
    "Embalm",
    "Escape",
    "Fuse",
    "Menace",
    "Ingest",
    "Melee",
    "Improvise",
    "Mentor",
    "Partner",
    "Mutate",
    "Scavenge",
    "Tribute",
    "Surge",
    "Skulk",
    "Undaunted",
    "Riot",
    "Spectacle",
    "Forestwalk",
    "Islandwalk",
    "Mountainwalk",
    "Double strike",
    "Cumulative upkeep",
    "First strike",
    "Encore",
    "Deathtouch",
    "Defender",
    "Amplify",
    "Affinity",
    "Bushido",
    "Convoke",
    "Bloodthirst",
    "Absorb",
    "Aura Swap",
    "Changeling",
    "Conspire",
    "Cascade",
    "Annihilator",
    "Battle Cry",
    "Cipher",
    "Bestow",
    "Dash",
    "Awaken",
    "Crew",
    "Aftermath",
    "Afflict",
    "Flanking",
    "Foretell",
    "Fading",
    "Fear",
    "Eternalize",
    "Entwine",
    "Epic",
    "Dredge",
    "Delve",
    "Evoke",
    "Exalted",
    "Evolve",
    "Extort",
    "Dethrone",
    "Exploit",
    "Devoid",
    "Emerge",
    "Escalate",
    "Flying",
    "Haste",
    "Hexproof",
    "Indestructible",
    "Intimidate",
    "Lifelink",
    "Horsemanship",
    "Kicker",
    "Madness",
    "Swampwalk",
    "Desertwalk",
    "Craft",
    "Plainswalk",
    "Split second",
    "Augment",
    "Double agenda",
    "Reconfigure",
    "Ward",
    "Partner with",
    "Daybound",
    "Nightbound",
    "Decayed",
    "Disturb",
    "Squad",
    "Enlist",
    "Read Ahead",
    "Ravenous",
    "Blitz",
    "Offering",
    "Living metal",
    "Backup",
    "Banding",
    "Hidden agenda",
    "For Mirrodin!",
    "Friends forever",
    "Casualty",
    "Protection",
    "Compleated",
    "Devour",
    "Enchant",
    "Flash",
    "Boast",
    "Landwalk",
    "Demonstrate",
    "Sunburst",
    "Flashback",
    "Cycling",
    "Equip",
    "Buyback",
    "Hexproof from",
    "More Than Meets the Eye",
    "Cleave",
    "Champion",
    "Specialize",
    "Training",
    "Prototype",
    "Toxic",
    "Unearth",
    "Intensity",
    "Plainscycling",
    "Swampcycling",
    "Typecycling",
    "Wizardcycling",
    "Mountaincycling",
    "Basic landcycling",
    "Islandcycling",
    "Forestcycling",
    "Slivercycling",
    "Landcycling",
    "Bargain",
    "Choose a background",
    "Echo",
    "Doctor's companion"]

    return random.choice(abilities) 


def keywordActionProvider():
    actions = [
            "Seek",
    "Activate",
    "Attach",
    "Cast",
    "Counter",
    "Create",
    "Destroy",
    "Discard",
    "Double",
    "Exchange",
    "Exile",
    "Adapt",
    "Support",
    "Play",
    "Regenerate",
    "Reveal",
    "Sacrifice",
    "Shuffle",
    "Tap",
    "Untap",
    "Vote",
    "Goad",
    "Transform",
    "Surveil",
    "Planeswalk",
    "Mill",
    "Learn",
    "Connive",
    "Venture into the dungeon",
    "Exert",
    "Open an Attraction",
    "Food",
    "Conjure",
    "Abandon",
    "Explore",
    "Amass",
    "Treasure",
    "Roll to Visit Your Attractions",
    "Set in motion",
    "Fateseal",
    "Manifest",
    "Populate",
    "Detain",
    "Investigate",
    "Monstrosity",
    "Clash",
    "Scry",
    "Incubate",
    "Proliferate",
    "Meld",
    "Convert",
    "Fight",
    "Bolster",
    "Assemble",
    "Role token"
    ]

    return random.choice(actions)


def abilityWordsProvider():
    words = [
            "Battalion",
    "Bloodrush",
    "Channel",
    "Chroma",
    "Cohort",
    "Constellation",
    "Converge",
    "Delirium",
    "Domain",
    "Fateful hour",
    "Ferocious",
    "Formidable",
    "Grandeur",
    "Hellbent",
    "Heroic",
    "Imprint",
    "Inspired",
    "Join forces",
    "Kinship",
    "Landfall",
    "Lieutenant",
    "Metalcraft",
    "Morbid",
    "Parley",
    "Radiance",
    "Raid",
    "Rally",
    "Spell mastery",
    "Strive",
    "Sweep",
    "Tempting offer",
    "Threshold",
    "Will of the council",
    "Adamant",
    "Addendum",
    "Council's dilemma",
    "Eminence",
    "Enrage",
    "Hero's Reward",
    "Kinfall",
    "Landship",
    "Legacy",
    "Revolt",
    "Underdog",
    "Undergrowth",
    "Descend",
    "Fathomless descent",
    "Magecraft",
    "Teamwork",
    "Pack tactics",
    "Coven",
    "Alliance",
    "Corrupted",
    "Secret council",
    "Celebration",
    "Paradox"
    ]


def oracleProvider():
    pass


def manaCostProvider():
    # Choose the category
    category = "manavalue" if random.random() < 0.01 else "mana"

    if category == "manavalue":
        # Choose an operator
        operators = ["<", ">", "!=", "<=", ">=", ":"]
        operator = random.choice(operators)

        # Choose a number or even/odd
        if operator == ":":
            number = random.choice(["even", "odd"])
        else:
            number = random.randint(0, 10)

        # Concatenate components
        mana_cost = f"{category}{operator}{number}"

    else:
        operators = ["<", ">", "!=", "<=", ">=", ":"]
        operator = random.choice(operators)
        # Append ":" and choose a random number
        mana_cost = f"{category}{operator}"
        #mana_number = random.randint(0, 10)
        #mana_cost += str(mana_number)

        # Choose symbols
        symbols = ["{R}", "{B}", "{G}", "{U}", "{W}"]

        probabilities = [1, 0.8, 0.3, 0.1]  # Probabilities for 2nd, 3rd, 4th and 5th color
        for prob in probabilities:
            if random.random() < prob:
                mana_cost += random.choice(symbols)
            else:
                break

    return mana_cost


def powerToughnessLoyaltyProvider():
    pass


def spellPermanentEffectsProvider():
    pass


def orTransformer(parameters):
    if random.random() < .1:
       nonwrapped = " or ".join(parameters.split(" "))
       return "(" + nonwrapped + ")"
    return parameters


def negationTransformer(parameters):
    return " ".join(["-" + p if random.random() < .1 else p for p in parameters.split(" ")])


def queryParameterProvider():
    creatureStuff = orTransformer(negationTransformer(creatureTypeProvider())) if random.random() < .8 else " "
    colorStuff = orTransformer(negationTransformer(colorProvider(True if random.random() < .9 else False)))
    manaStuff = manaCostProvider()
    return (
        creatureStuff + " " + manaStuff
    ).strip()
    #return manaStuff.strip()


while True:
    parameter = queryParameterProvider()
    while not parameter:
        parameter = queryParameterProvider()

    print(parameter)
    description = input()
    line = description + ",https://api.scryfall.com/cards/search?q=" + parameter
    with open("../data/search_training.csv", "a") as f:
      f.write("\n" + line)
