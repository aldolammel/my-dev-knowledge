from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5   # Install = Bootstrap-Flask
from flask_sqlalchemy import SQLAlchemy  # Install = Flask-SQLAlchemy

# CREATING THE APP:
app = Flask(__name__, template_folder="templates", static_folder="static")
app.config["SECRET_KEY"] = "Gt7362956KjuU9206LBnb194ds"
bootstrap = Bootstrap5(app)

# CREATING THE DATABASE:
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books.db"  # setting SQLite db, relative to the app folder.
db = SQLAlchemy()  # Creating the extension
db.init_app(app)  # initializing the app with the extension


# CREATING THE TABLE:
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)


with app.app_context():  # Creating table schema in the database. Requires application context.
    db.create_all()


@app.route("/")
def go_home():
    # READING ALL RECORDS:
    books = db.session.execute(db.select(Book).order_by(Book.title)).scalars().all()  # this ".all()" make it
                                                                                      # countable, crucial to
                                                                                      # "items|length" validation
                                                                                      # on index.html.
    return render_template("index.html", books=books)


@app.route("/add", methods=["GET", "POST"])
def go_add():
    if request.method == "POST":
        # CREATING A NEW RECORD:
        new_book = Book(
            # "id" is a primary-key on SQL db, then it's automatically created, not needed to be declared here.
            title=request.form["title"],
            author=request.form["author"],
            rating=request.form["rating"])
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for("go_home"))
    return render_template("add.html")


@app.route("/edit", methods=["GET", "POST"])
def go_edit():
    if request.method == "POST":
        # UPDATING A RECORD BY PRIMARY KEY:
        book_id = request.form["id"]  # because when POST, it's not allow to request the value from URL (get method).
        book_to_update = db.get_or_404(Book, book_id)
        book_to_update.title = request.form["title"]
        book_to_update.author = request.form["author"]
        book_to_update.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for("go_home"))
    book_id = request.args.get("id")  # requesting the id through the URL (get method)
    book_selected = db.get_or_404(Book, book_id)
    return render_template("edit.html", book=book_selected)


@app.route("/delete")
def act_del():
    book_id = request.args.get("id")  # take the value of "id" declared in the URL.
    # DELETING A RECORD:
    book_to_delete = db.get_or_404(Book, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for("go_home"))


if __name__ == "__main__":
    app.run(debug=True)
