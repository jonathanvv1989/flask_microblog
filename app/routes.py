from flask import render_template
from app import app

@app.route("/")
@app.route("/index")
def index():
    user = {"username": "Jonathan"}
    posts = [
        {"author": {"username": "Kerry"},
         "body": "Women are powerful"},
        {"author": {"username": "Rennor"},
         "body": "Norway is the most powerful country"},
        {"author": {"username": "Yanglang"},
         "body": "Love is everything"}
    ]

    return render_template("index.html", title="Home", user=user, posts=posts)
