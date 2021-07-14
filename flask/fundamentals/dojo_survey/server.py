from flask import Flask, render_template, request, session, redirect

survey = Flask(__name__)
survey.secret_key = "account info"

@survey.route("/")
def index():
    return render_template("index.html")

@survey.route("/result", methods = ["POST"])
def process():
    session['name'] = request.form['name']
    session['loca'] = request.form['loca']
    session['lang'] = request.form['lang']
    session['comm'] = request.form['comm']
    return redirect ("/present")

@survey.route("/present")
def display():
    return render_template("display.html")


if __name__ == "__main__":
    survey.run(debug = True)