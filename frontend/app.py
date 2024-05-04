# Frontend server

from flask import Flask
from flask import render_template

app = Flask(__name__, static_url_path="/static", static_folder="static")

@app.route("/login_view")
def hello_world():
    return app.send_static_file("index.html")
