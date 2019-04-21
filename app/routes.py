from flask import render_template
from app import app

@app.route("/")
@app.route("/index")
def index():
    user = {"username": "Jonathan"}
    posts = [
        {"author": {"username": "Kerry"},
         "body": "Gender equality is the way forward"},
        {"author": {"username": "Rennor"},
         "body": "Norway is the most powerful country"},
        {"author": {"username": "Yanglang"},
         "body": "Love is everything"},
        {"author": {"username": "Jonathan"},
         "body": "Knowledge is your inspiration"}
    ]

    return render_template("index.html", title="Home", user=user, posts=posts)
