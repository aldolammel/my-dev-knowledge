"""
JSON (JavaScript Object Notation):

    JavaScript Object Notation file is a lightweight data-interchange format that is easy for humans to read and write,
    and easy for machines to parse and generate. JSON is primarily used to transmit data between a server and a
    web application.

    IMPORTANT:
    Json always returns a dictionary.

"""
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy                            # Install = Flask-SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column  # Install = SQLAlchemy
from sqlalchemy import Integer, String                             # Install = SQLAlchemy

# CREATING THE APP:
app = Flask(__name__)
app.config["SECRET_KEY"] = "94587JuhYGT45#4@!"


# CREATING THE DATABASE:
class Base(DeclarativeBase):
    pass


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CREATING THE TABLE:
class Time(db.Model):
    id: Mapped[str] = mapped_column(Integer, primary_key=True)
    time: Mapped[str] = mapped_column(String(50), nullable=False)
    city: Mapped[str] = mapped_column(String(50), nullable=False)

    def to_dict(self):
        # This function converts the object in a dictionary:
        return {
          self.id: {
              "city": self.city,
              "time": self.time
          }
        }


@app.route("/")
def get_json():
    # Reading a specific data from the database:
    data_to_send = db.get_or_404(Time, 1)  # Test purposes, I'm using the static ID.
    # Preparing the data for JSON, creating a dictionary because JSON always asks a dictionary as input:
    data_to_send = data_to_send.to_dict()
    # Return with Json:
    return jsonify(data_to_send)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
