from flask import Flask, render_template
from post import Post
import requests

posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
post_objects = list()
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)


app = Flask(__name__, template_folder="templates", static_folder="static")
# app.jinja_env.finalize = lambda x: x if x is not None else ''  # when DB, makes Jinja doesn't print out NONE values.


@app.route("/")  # by default, all routes are method GET when "methods" are not declared.
def get_home():
    return render_template("index.html", all_posts=post_objects)


@app.route("/post/<int:post_id>")
def get_post(post_id):
    for blog_post in post_objects:
        if blog_post.id == post_id:
            return render_template("post.html", post=blog_post)
    return render_template("404.html", post_id=post_id)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
