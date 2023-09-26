"""
PERSISTENT DATA: DATABASE WITH SQLAlchemy

Additional app for this: 'DB Browser for SQLite'

Tip: In addition to these things, the most crucial thing to figure out when working with any new database technology
     is how to "CRUD" data records ---> CRUD = Create, Read, Update, Delete.

"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# CREATING THE APP:
app = Flask(__name__)  # creating the app
app.config["SECRET_KEY"] = "9HykU38rE39lOO900"

# CREATING THE DATABASE:
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database_name.db"  # configuring the SQLite database, relative to the app instance folder
db = SQLAlchemy()  # Creating the extension
db.init_app(app)  # initializing the app with the extension


# CREATING THE TABLE:
class TableName(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(50), nullable=False)
    rating = db.Column(db.Float, nullable=False)


with app.app_context():  # Creating table schema in the database. Requires application context.
    db.create_all()


# CREATING A NEW RECORD:
with app.app_context():
    new_book = TableName(title="Harry Potter 4", author="J. K. Rowling", rating=9.3)  # the primary key fields (id) is optional.
    db.session.add(new_book)
    db.session.commit()


# READING ALL RECORDS:
with app.app_context():
    results = db.session.execute(db.select(TableName).order_by(TableName.title))  # To read all the records we first need to create a "query" to select things from the database.
    all_books = results.scalars()  # We then use scalars() to get the individual elements rather than entire rows.


# READING A PARTICULAR RECORD BY QUERY:
with app.app_context():
    book = db.session.execute(db.select(TableName).where(TableName.title == "Harry Potter 2")).scalar()  # To get a single element we can use scalar() instead of scalars().


# UPDATING A RECORD BY PRIMARY KEY:
with app.app_context():
    book_to_update = db.session.execute(db.select(TableName).where(TableName.id == 1)).scalar()
    # or book_to_update = db.get_or_404(TableName, 1)
    book_to_update.title = "Harry Potter and the Goblet of Fire"
    db.session.commit()


# DELETING A PARTICULAR RECORD BY PRIMARY KEY:
with app.app_context():
    book_to_delete = db.session.execute(db.select(TableName).where(TableName.id == 1)).scalar()
    # or book_to_delete = db.get_or_404(TableName, 1)
    db.session.delete(book_to_delete)
    db.session.commit()
