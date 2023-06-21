from flask import render_template, redirect
from datetime import datetime
from . import app

@app.route("/")
def home():
    return redirect("/display/0")

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )

@app.route("/api/data")
def get_date():
    return app.send_static_file("data.json")


@app.route("/display/<number>")
def display(number = 0):
    return render_template(
        "display.html",
        count=number
    )


