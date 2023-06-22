from flask import render_template, redirect, request
from datetime import datetime
from . import app

@app.route("/")
def home():
    return "Hello!"
    # return redirect("/display/0")

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


@app.route("/count_up/<number>")
def count_up(number = 0):
    return render_template(
        "count_up.html",
        count=number
    )

@app.route('/stick', methods=['GET', 'POST'])
def stick():
    if request.method == 'POST':
        result = request.form['string1'] + request.form['string2']
        return render_template('stick.html', result=result)
    else:   
        return render_template('stick.html')
    

@app.route('/radiobuttons', methods =["GET", "POST"])
def radiobuttons():
    if request.method == "POST":
        lst = request.form
        
        if len(lst) == 0:
            return render_template("radiobuttons.html")
        
        result = request.form["fav_language"]
        return render_template("radiobuttons.html", result=result)
    return render_template("radiobuttons.html")

@app.route('/dynamic_radiobuttons', methods = ["GET", "POST"])
def dynamic_radiobuttons():

    radiobutton_list = ["Option 1", "Option 2", "Option 3", "Option 4"]
    # radiobutton_list = {"Option1": True}
    preselected_radiobutton = "Option 1"

    if request.method == "POST":
        if len(request.method) == 0:
            return render_template(
                "dynamic_radiobuttons.html",
                radiobutton_list=radiobutton_list,
                preselected_radiobutton=preselected_radiobutton
                )
        
        
    return  render_template(
                "dynamic_radiobuttons.html",
                radiobutton_list=radiobutton_list,
                preselected_radiobutton=preselected_radiobutton
                )

    


