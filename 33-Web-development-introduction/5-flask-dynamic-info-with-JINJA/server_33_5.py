from flask import Flask, render_template
import requests


app = Flask(__name__, template_folder="templates")
# app.jinja_env.finalize = lambda x: x if x is not None else ''  # when DB, makes Jinja doesn't print out NONE values.


@app.route("/")
def get_home():
    return render_template("index.html")


@app.route("/user/<name>")
def get_user(name):
    name_titled = name.title()

    response_age = requests.get(url=f"https://api.agify.io?name={name_titled}")
    response_age.raise_for_status()
    data_age = response_age.json()
    age = data_age["age"]

    response_gender = requests.get(url=f"https://api.genderize.io?name={name_titled}")
    response_gender.raise_for_status()
    data_gender = response_gender.json()
    gender = data_gender["gender"]

    return render_template("user.html", user_name=name_titled, user_age=age, user_gender=gender)


@app.route("/blog")
def get_blog():
    response = requests.get(url="https://api.npoint.io/9e5777b9acb15721ba93")
    all_posts = response.json()
    return render_template("blog.html", all_posts=all_posts)


@app.route("/blog/<int:post_id>")
def get_post(post_id):
    specific_post = list()
    response = requests.get(url="https://api.npoint.io/9e5777b9acb15721ba93")
    all_posts = response.json()
    for post in all_posts:
        if post["id"] == post_id:
            specific_post.append(post)
            return render_template("blog.html", all_posts=specific_post)
    return render_template("blog.html", all_posts=all_posts)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
