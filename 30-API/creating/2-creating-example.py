"""
API CREATION:
The logical behind to build up an API is the same logic of to build a website up with Flask.

PLANNING THIS API:

- API goal:
    >> Create an API to consulting, creating, updating and deleting books.
- Where:
    >> Localhost
- Endpoints:
    >> localhost/books/add (POST to add a new book)
    >> localhost/books (GET to return all books)
    >> localhost/books/id (GET to return a specific book)
    >> localhost/books/id (PUT to update a specific book)
    >> localhost/books/id (DELETE to delete a specific book)
- Resources:
    >> Books list.

"""

from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
    {
        "ID": 1,
        "TITLE": "Dia 922",
        "AUTHOR": "Aldo Lammel"
    },
    {
        "ID": 2,
        "TITLE": "Trilhando Sonhos",
        "AUTHOR": "Thiago Fantinatti"
    },
    {
        "ID": 3,
        "TITLE": "O Mundo ao Lado",
        "AUTHOR": "Arthur Simões"
    }
]


@app.route("/")
def home():
    """ This function is our book store home page """
    return "<p>Check <a href='/books'>all books</a></p>"


@app.route("/books", methods=["GET"])
def all_books():
    """ This function converts the book list to json format """
    return jsonify(books)


app.run(port=5000, host="localhost", debug=True)
