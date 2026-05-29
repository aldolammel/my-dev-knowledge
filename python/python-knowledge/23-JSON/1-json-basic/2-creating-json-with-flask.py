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
