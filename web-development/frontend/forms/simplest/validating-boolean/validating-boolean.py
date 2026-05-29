"""
FORM VALIDATION: BOOLEAN VALUES

    It doesn't matter if you are using Flask or Django or something else.

    TO TEST:
        1) Go to the app Postman or Insomnia;
        2) Select your Workspace;
        3) Create a POST Request to http://127.0.0.1:5000;
        4) In this request, select Body > x-www-form-urlencoded and set the inputs and values to test;
        5) Save it and Send the tests;
        6) With DB Browser, open the database and check if everything is fine.

"""
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Boolean

app = Flask(__name__)


# CREATE DB
class Base(DeclarativeBase):
    pass


# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Error Handling > Boolean form values:
def str_to_bool(value_from_form):
    """
    It receives a string, check if the string is a valid positive answer and return the result. This function goal is
    to make the dev life easier, basically during form tests.
    :param value_from_form: the input text on the form.
    :return: bool
    """
    if value_from_form in ["1", "YES", "Yes", "yes", "Y", "y", "TRUE", "True", "true", "T", "t"]:
        return True
    return False


# Cafe TABLE Configuration
class Cafe(db.Model):
    name: Mapped[str] = mapped_column(String(30), primary_key=True, nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)


@app.route("/", methods=["GET", "POST"])
def post_new_cafe():
    if request.method == "POST":
        # Building the new object from the form inputs:
        new_cafe = Cafe(
            name=request.form.get("name"),
            has_toilet=str_to_bool(request.form.get("has_toilet")),  # checking if the value is a valid True.
            has_wifi=str_to_bool(request.form.get("has_wifi"))  # checking if the value is a valid True.
        )
        # Including the new object in the db:
        db.session.add(new_cafe)
        # updating the db:
        db.session.commit()
        # Returning the message as json:
        return jsonify(response={"success": "Successfully added the new cafe."})
    return "<h1>Use the Postman/Insomnia to test!</h1>"


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
