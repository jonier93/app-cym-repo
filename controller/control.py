from flask import render_template, request
from database.db import *

def func_home_page():
    return render_template("home.html")
    
def func_register_page():
    return render_template("register.html")

def func_consult_page():
    return render_template("consult.html")

def func_register_user():
    id = request.form["id"]
    name = request.form["name"]
    lastname = request.form["lastname"]
    birthday = request.form["birthday"]
    print(id, name, lastname, birthday)
    add_user(id, name, lastname, birthday)
    return "Ok"