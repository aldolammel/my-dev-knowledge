"""
JSON (JavaScript Object Notation):

    JavaScript Object Notation file is a lightweight data-interchange format that is easy for humans to read and write,
    and easy for machines to parse and generate. JSON is primarily used to transmit data between a server and a
    web application.

    IMPORTANT:
    Json always returns a dictionary.

"""
import json
from datetime import datetime

# TODO: Create a JSON that share the current time:

# Preparing the data for JSON, creating a dictionary because JSON always asks a dictionary as input:
data_to_send = {
    "town": "Porto Alegre",
    "current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
}
# Convert the dictionary to a JSON object:
json_data = json.dumps(data_to_send, indent=4)
# Print json out:
print(json_data)
