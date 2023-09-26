from flask import Flask
from random import randint

app = Flask(__name__)


@app.route("/")
def home():
    return "<title>Higher-Lower Game by @aldolammel</title>" \
           "<h1>Do it: guess a number between 0 and 9.</h1>" \
           "<p><b>How to play:</b> go to the browser address bar and type the number like this " \
           "'URL/<the number>' between 0 and 9.</p>" \
           "<img src='https://media.giphy.com/media/JdFEeta1hLNnO/giphy.gif'>"


@app.route("/<int:guess>")
def result(guess):
    random_number = randint(0, 9)
    if guess == random_number:
        return "<h1>You got it!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"
    elif guess > random_number:
        if guess > random_number + 2:
            return "<h1>Too high! You lose!</h1>" \
                   "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
        return f"<h1>Almost ({random_number}). You lose!</h1>"
    else:
        if guess < random_number - 2:
            return "<h1>Too low! You lose!</h1>" \
                   "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
        return f"<h1>Almost ({random_number}). You lose!</h1>"


if __name__ == "__main__":
    app.run(debug=True)
