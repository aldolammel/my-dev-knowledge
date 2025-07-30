"""
JSON (JavaScript Object Notation):

    JavaScript Object Notation file is a lightweight data-interchange format that is easy for humans to read and write,
    and easy for machines to parse and generate. JSON is primarily used to transmit data between a server and a
    web application.

    IMPORTANT:
    Json always returns a dictionary.

    Tools:
        Postman > it helps developers design, build, test and manage APIs.
        Insomnia > Postman alternative.

"""
from flask import Flask, jsonify
from datetime import datetime

# TODO: Create a JSON that share the current time:

app = Flask(__name__)


@app.route('/')
def get_time():
    # Preparing the data for JSON, creating a dictionary because JSON always asks a dictionary as input:
    data_to_send = {
        "town": "Porto Alegre",
        "current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    # Return the dictionary as a JSON response
    return jsonify(data_to_send)


if __name__ == '__main__':
    app.run(debug=True)
