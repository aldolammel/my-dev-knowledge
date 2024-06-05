"""
PERSISTENT DATA: DATABASE WITH SQLAlchemy

Install and update the modules:
    pip install -U Flask-SQLAlchemy
    pip install -U SQLAlchemy

Additional app for this: 'DB Browser for SQLite'

Tip: In addition to these things, the most crucial thing to figure out when working with any new database technology
     is how to "CRUD" data records ---> CRUD = Create, Read, Update, Delete.

To know: when you run this, if there's no the database, it will create automatically in a folder called 'instance'.
    To visualize your db, use the 'DB Browser for SQLite', opening manually the db from the project folder.

"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy                            # Install = Flask-SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column  # Install = SQLAlchemy
from sqlalchemy import Integer, String, Float                      # Install = SQLAlchemy

# CREATING THE APP:
app = Flask(__name__)
app.config["SECRET_KEY"] = "83j5Hf93kf0OI29bN@"  # A Flask secret key: a random string.


# CREATING THE DATABASE:
class Base(DeclarativeBase):
    pass


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database_name.db"  # Config SQLite db, relative to app folder
db = SQLAlchemy(model_class=Base)  # Creating the extension
db.init_app(app)  # initializing the app with the extension


# CREATING THE TABLE:
class TableName(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(50), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

    # Optional: this dunder-method will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<TableName {self.title}>'
        # The reason for creating a __repr__ (magic/dunder) method in a class like this is to improve how you see and
        # work with objects in your code. When you print a Book object or use repr() on it, you'll get a string that
        # includes the book's title. This makes it much easier to debug the object. Without it, you'd see a less helpful
        # default string like <Book object at 0x...>, which doesn't tell you much about the object.


with app.app_context():  # Creating table schema in the database. Requires application context.
    db.create_all()


# CREATING A NEW RECORD:
with app.app_context():
    new_book = TableName(title="Harry Potter", author="J. K. Rowling", rating=9.3)  # primary key field's (id) optional.
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
