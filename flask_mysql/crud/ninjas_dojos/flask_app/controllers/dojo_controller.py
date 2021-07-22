from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route("/")
def index():
    return render_template("main.html", all_dojo = Dojo.get_all_dojos())


@app.route("/dojo/create", methods = ['POST'])
def create_dojo():
    Dojo.create(request.form)
    return redirect("/")


@app.route("/display/<int:id>")
def display(id):
    return render_template("display.html", dojo = Dojo.get_one_dojo({"id" : id}))