"""
API (Application Programming Interface):
An API is a set of commands, functions, protocols, and objects that programmers can use to create software or interact
with an external system.

CREATING:
The logical behind to build up an API is the same logic of to build a website up with Flask.

"""

import pandas as pd
from flask import Flask, jsonify

# Setting the Flash to an object:
app = Flask(__name__)


# Endpoint of API status page:
@app.route("/")
def status():
    return "<p>API is running!</p><p><a href='/sales'>See total sales amount</p>"


# Endpoint of total sales amount:
@app.route("/sales")
def total_sales():
    # Setting the file to an object:
    file = pd.read_csv("db.csv")
    # Response need to be a dictionary:
    response = {
        "Total sales": file["Vendas"].sum()
    }
    return jsonify(response["Total sales"])


# Start Flask:
app.run()
