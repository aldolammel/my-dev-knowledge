from flask import Flask, render_template
from random import randint
from datetime import date

app = Flask(__name__, template_folder="templates")


@app.route("/")
def home():
    random_number = randint(1, 50)
    current_year = date.today().year
    return render_template("index.html", num=random_number, year=current_year)


if __name__ == "__main__":
    app.run(debug=True)
