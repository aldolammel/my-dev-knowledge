from flask import Flask, render_template, request, redirect, url_for     # Install = flask
from flask_sqlalchemy import SQLAlchemy                                  # Install = Flask-SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column        # Install = SQLAlchemy
from sqlalchemy import Integer, String                                   # Install = SQLAlchemy

# CREATING APP:
app = Flask(__name__, template_folder="templates", static_folder="static")


# PLANNING THE DATABASE: -----------------------------------------------------------------------------------------------
class Base(DeclarativeBase):
    pass


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"  # Config SQLite db, relative to app folder
db = SQLAlchemy(model_class=Base)  # Creating the extension
db.init_app(app)  # initializing the app with the extension


# PLANNING A TABLE:
class Coffee(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(40), unique=False, nullable=False)
    description: Mapped[str] = mapped_column(String(1000), unique=False, nullable=False)
    country: Mapped[str] = mapped_column(String(40), unique=False, nullable=False)
    photo: Mapped[str] = mapped_column(String(140), unique=False, nullable=True)

    def __repr__(self):
        return f"<Coffee {self.name}>"


# ----------------------------------------------------------------------------------------------------------------------

@app.route("/")
def go_home():
    # Reading all records:
    items = db.session.execute(db.select(Coffee).order_by(Coffee.name)).scalars().all()     # this ".all()" make it
                                                                                            # countable, crucial to
                                                                                            # "items|length" validation
                                                                                            # on index.html.
    return render_template("index.html", items=items)


@app.route("/add", methods=["GET", "POST"])
def go_add():
    if request.method == "POST":
        item_new = Coffee(
           name=request.form["name"],
           description=request.form["description"],
           country=request.form["country"],
           photo=request.form["photo"]
        )
        db.session.add(item_new)
        db.session.commit()
        return redirect(url_for("go_home"))
    return render_template("add.html")


@app.route("/edit", methods=["GET", "POST"])
def go_edit():
    if request.method == "POST":
        item_edit = db.get_or_404(Coffee, request.form["id"])
        item_edit.name = request.form["name"]
        item_edit.description = request.form["description"]
        item_edit.country = request.form["country"]
        item_edit.photo = request.form["photo"]
        db.session.commit()
        return redirect(url_for("go_home"))
    item_selected = db.get_or_404(Coffee, request.args.get("id"))
    return render_template("edit.html", item=item_selected)


@app.route("/delete")
def act_del():
    item_del = db.get_or_404(Coffee, request.args.get("id"))
    db.session.delete(item_del)
    db.session.commit()
    return redirect(url_for("go_home"))


if __name__ == "__main__":
    # Creating the database:
    with app.app_context():
        db.create_all()
    # Finally it runs the web page:
    app.run(host="0.0.0.0", debug=True)
