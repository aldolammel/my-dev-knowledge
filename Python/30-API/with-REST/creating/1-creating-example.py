"""
API CREATION:
The logical behind to build up an API is the same logic of to build a website up with Flask.

THIS API PLANNING:
1: Goal > define the reason of this api exists.
    >> Print out the total of sales amount.
2: Where > what URL this API will be available.
    >> localhost
3: Endpoints > what locations with this API that accepts requests and send back responses.
    >> total_sales()
4: Resources > what resources you want to provide with this API.
    >> check the total sales amount

    Tools:
        Postman > it helps developers design, build, test and manage APIs.
        Insomnia > Postman alternative.

"""

import pandas as pd
from flask import Flask, jsonify

# Setting the Flask to an object:
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
app.run(debug=True)
