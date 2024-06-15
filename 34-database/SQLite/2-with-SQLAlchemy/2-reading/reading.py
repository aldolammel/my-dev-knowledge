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
from sqlalchemy import Integer, String, Float, Boolean             # Install = SQLAlchemy

# CREATING THE APP:
app = Flask(__name__)
app.config["SECRET_KEY"] = "103j5Hf93kf0kLI29bN@"  # A Flask secret key: a random string.


# CREATING THE DATABASE:
class Base(DeclarativeBase):
    pass


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database_name.db"
db = SQLAlchemy(model_class=Base)  # Creating the extension
db.init_app(app)  # initializing the app with the extension


# CREATING THE TABLE:
class TableName(db.Model):
    # This is a table in the database, but it's also an object to be used to create new entries in this database table.
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    director: Mapped[str] = mapped_column(String(50), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    in_cinema: Mapped[bool] = mapped_column(Boolean, nullable=False)

    # Optional: this dunder-method will allow each movie object to be identified easier when printed out:
    def __repr__(self):
        return f'<TableName {self.title} by {self.director}>'


# Starting the flask application:
if __name__ == "__main__":
    with app.app_context():  # Creating table schema in the database. Requires application context.
        db.create_all()
    app.run(port=5000, host="0.0.0.0", debug=True)
