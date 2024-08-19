from flask import Flask, render_template, request
from database.db import *
app = Flask(__name__)

@app.route("/")
def home_page():
    return "<h1>hola desde EC2</h1>"

@app.route("/register_page")
def register_page():
    return render_template("register.html")

@app.route("/register_user", methods=["post"])
def register_user():
    id= request.form["id"]
    name= request.form["name"]
    lastname= request.form["lastname"]
    birthday= request.form["birthday"]
    insert_register(id, name, lastname, birthday)
   
    return "ok"

if __name__ == "__main__":
    host= "0.0.0.0"
    port= "80"
    app.run(host, port)
