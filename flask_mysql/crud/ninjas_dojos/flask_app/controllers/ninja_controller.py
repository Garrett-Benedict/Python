from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route("/index/ninja")
def ninja_index():
    return render_template("create.html", results = Dojo.get_all_dojos())

@app.route("/create/ninja", methods = ["POST"])
def create_ninja():
    print("inside controller")
    Ninja.create(request.form)
    return redirect("/")


