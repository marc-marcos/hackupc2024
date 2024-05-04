# Frontend server

from flask import Flask
from flask import render_template

app = Flask(__name__, static_url_path="/static", static_folder="static")

@app.route("/login_view")
def hello_world():
    return app.send_static_file("login.html")

@app.route("/your_flights")
def your_flights():
    print("test")
    return app.send_static_file("YourFlights/yourflights.html")

@app.route("/registrar_no_vidente")
def registrar_no_vidente():
    return app.send_static_file("RegistrarNoVidente/RegistrarNoVidente.html")

@app.route("/")
def index():
    return app.send_static_file("home/Pag_inicio.html")