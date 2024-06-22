"""
PERSISTENT DATA: DATABASE WITH SQLAlchemy: READING

    + How to read all entries from a specific table;
    + How to read a specific entry;
    + How to read a random entry;

    Important:
        The goal here is not where the result will be print out (json or html, for example),
        but how.

"""

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy                            # Install = Flask-SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column  # Install = SQLAlchemy
from sqlalchemy import Integer, String, Float, Boolean             # Install = SQLAlchemy
from random import randint

# CREATING THE APP:
app = Flask(__name__)
app.config["SECRET_KEY"] = "103p5Hf93km0kLI29bN@"  # A Flask secret key: a random string.


# CREATING THE DATABASE:
class Base(DeclarativeBase):
    pass


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database_name.db"
db = SQLAlchemy(model_class=Base)  # Creating the extension
db.init_app(app)  # initializing the app with the extension


# CREATING THE TABLE:
class Movie(db.Model):
    # This is a table in the database, but it's also an object to be used to create new entries in this database table.
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(80), unique=True, nullable=False)
    director: Mapped[str] = mapped_column(String(30), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    in_cinema: Mapped[bool] = mapped_column(Boolean, nullable=False)

    def to_dict(self):
        # Json asks for dict format.
        return {
            self.title: {
                "id": self.id,
                "director": self.director,
                "rating": self.rating,
                "in_cinema": self.in_cinema
            }
        }


@app.route("/")
@app.route("/movies")
def all_movies():
    # Reading all records:
    movies = db.session.execute(db.select(Movie).order_by(Movie.title)).scalars().all()  # this ".all()" make it
                                                                                         # countable, crucial to
                                                                                         # "items|length" validation
                                                                                         # on index.html.
    all_of_them = [movie.to_dict() for movie in movies]
    # As I don't want to build an HTML page only to show the result, I'm using a json result:
    return jsonify(movies=all_of_them)


@app.route("/movie/<int:movie_id>")
def movie_by_id(movie_id):
    movie = db.get_or_404(Movie, movie_id)
    # As I don't want to build an HTML page only to show the result, I'm using a json result:
    return jsonify(movie.to_dict())


@app.route("/movie/random")
def movie_random():
    movie_id = randint(1, Movie.query.count())  # checking the length of Movie table in database.
    movie = db.get_or_404(Movie, movie_id)
    # As I don't want to build an HTML page only to show the result, I'm using a json result:
    return jsonify(movie.to_dict())


# Starting the flask application:
if __name__ == "__main__":
    with app.app_context():  # Creating table schema in the database. Requires application context.
        db.create_all()
    app.run(port=5000, host="0.0.0.0", debug=True)


#  ------ TO TEST ------------------------------------------------------------------------------------------------------
# http://127.0.0.1:5000/movies/        <--- to check all entries
# http://127.0.0.1:5000/movie/3        <--- to check a specific one by id
# http://127.0.0.1:5000/movie/random   <--- random entry
