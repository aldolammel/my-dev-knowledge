"""
WEB DEVELOPMENT INTRODUCTION: FLASK FRAMEWORK

Important: make sure this file is in the root of the project folder with its own venv folder (own virtual environment).

0) Since exactly from the project's folder root,
    type through Terminal to create the virtual environment: virtualenv venv
    If the command wasn't recognized, install the virtualenv module: pip install virtualenv
1) Use te minimal code (e.g. seem down below)
2) Install the Flask module
3) Set the environment through the terminal: set FLASK_APP=app.py

"""

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World! from myPythonStudies</p>"


if __name__ == "__main__":  # MAIN and NOT NAME. Be careful!
    app.run(host="0.0.0.0")  # This IP is a special that force Flask to run in all machines with app access.
