"""
PERSISTENT DATA: DATABASE WITH SQLAlchemy: CREATING



"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy                            # Install = Flask-SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column  # Install = SQLAlchemy
from sqlalchemy import Integer, String, Float, Boolean             # Install = SQLAlchemy

# CREATING THE APP:
app = Flask(__name__)
app.config["SECRET_KEY"] = "214j8gf97kf@kLI29cN#"  # A Flask secret key: a random string.


# CREATING THE DATABASE:
class Base(DeclarativeBase):
    pass


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database_name.db"  # it'll be in 'instance' folder.
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


# Creating table schema in the database, but if the db doesn't exist yet, it'll be created:
with app.app_context():
    db.create_all()
