import argparse

parser = argparse.ArgumentParser(description='Run a Discord bot.')
parser.add_argument('channel_name', help='Name of the channel to monitor')
parser.add_argument('token_file', help='Path to a file containing the Discord bot token')