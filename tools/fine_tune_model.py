import csv
import os
import json
import tempfile
from chatgpt_fine_tune import TrainGPT


def translate_csv_to_json(csv_filename):
    # Open the CSV file
    with open(csv_filename, 'r') as csv_file:
        # Create a CSV reader
        reader = csv.reader(csv_file)
        
        # Translate the data to the required JSON format
        json_list = []
        for row in reader:
            message, result = row
            entry = {
                "messages": [
                    {"role": "system", "content": "Act as a scryfall api bot that accepts a user query and translates it into a search URL.  Output only the url."},
                    {"role": "user", "content": message},
                    {"role": "assistant", "content": result}
                ]
            }
            json_list.append(entry)
    
    return json_list


# create a temporary file for the json data
with tempfile.NamedTemporaryFile(mode='w+', suffix='.json', delete=True) as temp_json:
    # Read in the csv data
    formatted_data = translate_csv_to_json("data/search_training.csv")

    # Write formatted data to the json file
    for item in formatted_data:
        temp_json.write(json.dumps(item) + "\n")

    temp_json.flush()

    # Train a gpt 3.5 model using the formatted json
    trainer = TrainGPT()
    trainer.create_file(temp_json.name)
    trainer.start_training()
    trainer.list_jobs()
