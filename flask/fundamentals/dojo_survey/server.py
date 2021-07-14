from flask import Flask, render_template, request, session

survey = Flask(__name__)
survey.secret_key = "account info"

@survey.route("/")
def index():
    return render_template("index.html")

@survey.route("/result", methods = ["POST"])
def result():
    session['name'] = request.form['name']
    session['loca'] = request.form['loca']
    session['lang'] = request.form['lang']
    session['comm'] = request.form['comm']
    return render_template (
    "display.html",
    name = request.form['name'],
    loca = request.form['loca'],
    lang = request.form['lang'],
    comm = request.form['comm']
    )


if __name__ == "__main__":
    survey.run(debug = True)