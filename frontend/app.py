# Frontend server

from flask import Flask
from flask import render_template

app = Flask(__name__, static_url_path="/static", static_folder="static")

@app.route("/login_view")
def hello_world():
    return app.send_static_file("login.html")

@app.route("/your_flights")
def your_flights():
    return app.send_static_file("YourFlights/yourflights.html")

@app.route("/registrar_no_vidente")
def registrar_no_vidente():
    return app.send_static_file("RegistrarNoVidente/RegistrarNoVidente.html")

@app.route("/comprando_vuelo")
def comprando_vuelo():
    return app.send_static_file("ComprandoVuelo/comprandovuelo.h tml")

@app.route("/vuelo_comprado")
def vuelo_comprado():
    return app.send_static_file("VueloComprado/index.html")
@app.route("/check_in")
def check_in():
    return app.send_static_file("CheckIn/checkin.html")

@app.route("/")
def index():
    return app.send_static_file("home/Pag_inicio.html")

@app.route("/roulete")
def roulete():
    return app.send_static_file("widget-ruleta/index.html")

