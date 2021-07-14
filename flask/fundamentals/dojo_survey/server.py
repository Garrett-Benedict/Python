from flask import Flask, render_template, request

survey = Flask(__name__)

@survey.route("/")
def index():
    return render_template("index.html")

@survey.route("/result", methods = ["POST"])
def result():
    return render_template (
    "display.html",
    name = request.form['name'],
    loca = request.form['loca'],
    lang = request.form['lang'],
    comm = request.form['comm']
    )


if __name__ == "__main__":
    survey.run(debug = True)