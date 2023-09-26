from flask import Flask, render_template, redirect
from flask_bootstrap import Bootstrap5  # to install: pip install bootstrap-flask
from cafe_form import CafeForm
import csv

app = Flask(__name__, template_folder="templates", static_folder="static")
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
bootstrap = Bootstrap5(app)


# all Flask routes below
@app.route("/")
def go_home():
    return render_template("index.html")


@app.route("/add", methods=["GET", "POST"])
def go_add_cafe():
    form = CafeForm()
    if form.validate_on_submit():  # returns True if the form has been sent!
        with open("database.csv", mode="a", encoding="utf-8") as file:
            file.write(f"\n"
                       f"{form.cafe.data},"
                       f"{form.geo.data},"
                       f"{form.open.data},"
                       f"{form.close.data},"
                       f"{form.coffee_rating.data},"
                       f"{form.wifi_rating.data},"
                       f"{form.power_rating.data}")
        return redirect("/cafes")
    return render_template("add.html", form=form)


@app.route("/cafes")
def go_cafes():
    with open("database.csv", mode="r", newline="") as file:
        csv_data = csv.reader(file, delimiter=",")
        list_of_rows = list()
        for row in csv_data:
            list_of_rows.append(row)
    return render_template("cafes.html", cafes=list_of_rows)


if __name__ == "__main__":
    app.run(debug=True)
