from flask import Flask, jsonify, request, current_app, g
import sqlite3
import click

app = Flask(__name__)


@app.route("/login", methods=["POST"])
def login():
    data = request.json

    email = data["email"]
    password = data["password"]

    conn = sqlite3.connect("database.db")

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, password))

    user = cursor.fetchone()

    if user is None:
        return jsonify({"message": "Invalid credentials"}), 401
    
    else:
        vidente = user[4]
        return jsonify({"message": "Login successful", "vidente": vidente})

    
@app.route("/register_vidente", methods=["POST"])
def register_vidente():
    data = request.json

    email = data["email"]
    name = data["name"]
    surname = data["surname"]
    password = data["password"]
    vidente = True

    conn = sqlite3.connect("database.db")

    cursor = conn.cursor()

    cursor.execute("INSERT INTO users (email, name, surname, password, vidente) VALUES (?, ?, ?, ?, ?)", (email, name, surname, password, vidente))

    conn.commit()

    conn.close()

    return jsonify({"message": "Vidente registered"})

@app.route("/register_invidente", methods=["POST"])
def register_invidente():
    data = request.json

    email = data["email"]
    name = data["name"]
    surname = data["surname"]
    password = data["password"]
    vidente = False 

    conn = sqlite3.connect("database.db")

    cursor = conn.cursor()

    cursor.execute("INSERT INTO users (email, name, surname, password, vidente) VALUES (?, ?, ?, ?, ?)", (email, name, surname, password, vidente))

    conn.commit()

    conn.close()

    return jsonify({"message": "Invidente registered"})


@app.route("/")
def hello_world():
    return "<p>Hello World!</p>"

if __name__ == "__main__":
    app.run(debug=True)  # Enable debug mode for better error messages during development
