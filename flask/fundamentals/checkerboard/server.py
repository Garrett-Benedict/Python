from flask import Flask, render_template

check = Flask(__name__)

@check.route("/")
def index():
    return render_template("index.html", num=8 , numX = 8 , num1 = 8 , num2 = 8)

@check.route("/8/<int:numX>")
def num_x(numX):
    return render_template("index.html", num=8 , numX = numX , num1 = 8 , num2 = 8)

@check.route("/<int:num1>/<int:num2>")
def x_y(num1 , num2):
    return render_template("index.html", num=8 , numX = 8 , num1 = num1, num2 = num2)

if __name__ == "__main__":
    check.run(debug = True)
