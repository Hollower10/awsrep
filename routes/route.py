from server import app
from controller.control import *


@app.route("/")
def home_page():
    return func_home_page()

@app.route("/register_page")
def register_page():
    return func_register_page()

@app.route("/register_user", methods=["post"])
def register_user():
    return func_register_user()