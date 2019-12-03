from flask import Flask, render_template
import sys

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("/html/index.html")

@app.route("/about")
def about():
    return render_template("/html/about.html")

@app.route("/projects")
def projects():
    return render_template("/html/projects.html")

@app.route("/train_game")
def train_game():
    return render_template("/html/train_game.html")

@app.route("/centaur_generator")
def centaur_generator():
    return render_template("/html/centaur_generator.html")

@app.route("/in_progress")
def in_progress():
    return render_template("/html/in_progress.html")


if __name__=="__main__":
    app.run(port=5000, debug=True)
