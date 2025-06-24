from flask import Flask, render_template
from random import randint
from datetime import date

app = Flask(__name__, template_folder="templates")


@app.route("/")
def go_home():
    random_number = randint(1, 50)
    current_year = date.today().year
    return render_template("index.html", num=random_number, year=current_year)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)  # This IP is a special that force Flask to run in all machines with app access.
