from flask import Flask, render_template
from flask_bootstrap import Bootstrap5                    # Install bootstrap-flask


app = Flask(__name__, template_folder="templates", static_folder="static")
bootstrap = Bootstrap5(app)


@app.route("/")  # by default, all routes are method GET when "methods" are not declared.
def go_home():
    return render_template("index.html")


@app.route("/anotherpage")
def go_another_page():
    return render_template("another_page.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

