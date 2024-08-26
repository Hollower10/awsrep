from database.db import *
from flask import render_template,request
def func_home_page():
    return "<h1>hola desde EC2</h1>"


def func_register_page():
    return render_template("register.html")


def func_register_user():
    id= request.form["id"]
    name= request.form["name"]
    lastname= request.form["lastname"]
    birthday= request.form["birthday"]
    insert_register(id, name, lastname, birthday)
   
    return "ok"