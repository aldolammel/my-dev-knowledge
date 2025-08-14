"""
    API CREATION:
    The logical behind to build up an API is the same logic of to build a website up with Flask.
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
def products():
    """ This function converts the book list to json format and print it out """
    return jsonify(books)


@app.route("/books/<int:book_id>", methods=["GET"])
def product(book_id):
    """ This function shows up a specific book """
    # For each book inside the books list:
    for book in books:
        # If the book ID is the same of the book_id:
        if book.get("ID") == book_id:
            # Return the book data in json format:
            return jsonify(book)
    # If the book searching fail, return the message:
    return "Product not found!"


@app.route("/books/<int:book_id>/edit", methods=["PUT"])
def update(book_id):
    """ This function update an existent product """
    # To receive an info from the user, use request.get_json():
    updated_book = request.get_json()
    for idx, book in enumerate(books):
        if book.get("ID") == book_id:
            books[idx].update(updated_book)
            return jsonify(books[idx])
    # If the book searching fail, return the message:
    return "Product not found!"


@app.route("/books/add", methods=["POST"])
def add_product():
    """ This function adds a new product to the books list """
    new_product = request.get_json()
    books.append(new_product)
    return jsonify(books)


@app.route("/books/<int:book_id>/edit", methods=["DELETE"])
def remove_product(book_id):
    for idx, book in enumerate(books):
        if book.get("ID") == book_id:
            del books[idx]
            return jsonify(books)


app.run(port=5000, host="localhost", debug=True)
