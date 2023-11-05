# ScryBot

A Discord Scryfall Bot.  This bot supports two core functionalities:

* Searching scryfall for any named cards when a message is detected with text surrounded by `[[]]`
* Using a custom fine tuned gpt3.5 model to translate requests into scryfall api URLs

# Installing and setting up the development environment 

ScryBot uses poetry for dependency management and packaging

```python
pip install poetry
poetry install
poetry run python -m scrybot
```

This requires a `.env` file with two environment variables

* `DISCORD_BOT_TOKEN`: The secret key provided by discord for the bot this application runs under
* `OPENAI_API_KEY`: The secret key for making calls to OPENAI


# Fine tuning the API model with chatgpt

ChatGPT fine tuning data is located in `data/search_training.csv`.  This file is a two-column
csv file.  The first column is an example user message passed into the discord bot.  The second
column is the url generated from the user request in the first column. 

```
poetry run python tools/fine_tune_model.py
```