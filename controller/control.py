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
    confirm_user = add_user(id, name, lastname, birthday)
    if confirm_user:
        return "<h1>The user was created sucessfully</h1>"
    else:
        return "<h1>Error: The user was not created</h1>"
        
def func_consult_user():
    obj_user = request.get_json()
    id = obj_user["id"]
    passw = obj_user["passw"] # Es solo para pruebas no se utiliza
    consult_user(id)
    return "OK"
    