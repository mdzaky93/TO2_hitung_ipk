from app import app
from app.controller import controllerRoute
from flask import render_template

@app.route('/')
def index():
    # return "Hello, World!"
    message_value = "Hello, World"
    return render_template('index.html',message_key=message_value)    

@app.route('/ctr')
def tesctr():
    return controllerRoute.fungsiController()

@app.route('/ctr/')
@app.route('/ctr/<parameter>')
def tesctrParameter(parameter="kosong"):
    return controllerRoute.fungsiControllerParameter(parameter)



# @app.route('/users/')
# def tesParameter1():
#     return "ini users"

# @app.route('/user/<name>')
# @app.route('/user/')
# def tesParameter(name="kosong"):
#     return f"Hello, {name}!"
