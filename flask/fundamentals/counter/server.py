from flask import Flask, render_template, redirect, session

count = Flask(__name__)
count.secret_key = "numbers"

@count.route("/")
def index():
    if 'num' in session:
        session['num'] += 1
    else:
        session['num'] = 1
    return render_template("index.html")

@count.route("/destroy_session")
def destroy():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    count.run(debug = True)