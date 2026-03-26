"""
WEB DEVELOPMENT WITH FLASK FRAMEWORK:

1) All html files to render must be in 'templates' folder;
2) All static files (like images), need to be in 'static' folder;

"""

from flask import Flask, render_template

app = Flask(__name__, template_folder="templates", static_folder="static")


@app.route("/")
def go_home():
    return render_template("cv.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)  # This IP is a special that force Flask to run in all machines with app access.

