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

@app.route("/anadir_vuelo", methods=["POST"])
def anadir_vuelo():
    data = request.json

    codigo = data["codigo"]
    origen = data["origen"]
    destino = data["destino"]
    fecha = data["fecha"]
    hora = data["hora"]

    conn = sqlite3.connect("database.db")

    cursor = conn.cursor()

    cursor.execute("INSERT INTO vuelos (codigo, origen, destino, fecha, hora) VALUES (?, ?, ?, ?, ?)", (codigo, origen, destino, fecha, hora))

    conn.commit()

    conn.close()

    return jsonify({"message": "Vuelo añadido"})

@app.route("/asociar_vuelo", methods=["POST"])
def asociar_vuelo():
    data = request.json

    email = data["email"]
    codigo = data["codigo"]

    conn = sqlite3.connect("database.db")

    cursor = conn.cursor()

    cursor.execute("INSERT INTO reservas (email, codigo) VALUES (?, ?)", (email, codigo))

    conn.commit()

    conn.close()

    return jsonify({"message": "Vuelo asociado"}) 

@app.route("/pedir_ayuda", methods=["POST"])
def pedir_ayuda():
    data = request.json

    email = data["email"]
    codigo = data["codigo"]

    conn = sqlite3.connect("database.db")

    cursor = conn.cursor()

    cursor.execute("INSERT INTO ayuda (email, codigo) VALUES (?, ?)", (email, codigo))

    conn.commit()

    conn.close()

    return jsonify({"message": f"Ayuda pedida por {email} en el vuelo {codigo}"})

@app.route("/ayudar", methods=["GET"])
def ayudar():
    data = request.json

    email = data["email"]

    # Check if the user is vidente, if he's not, return an error message

    conn = sqlite3.connect("database.db")

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE email = ?", (email,))

    user = cursor.fetchone()

    if user is None:
        return jsonify({"message": "User not found"}), 404
    
    else:
        vidente = user[4]

        if not vidente:
            return jsonify({"message": "User is not vidente"}), 403

        # vuelos should be a list of flights where the user with email has a reservation and another user has requested help
        cursor.execute("SELECT * FROM reservas WHERE codigo IN (SELECT codigo FROM ayuda) AND email = ?", (email,))

        vuelos = cursor.fetchall()
        return jsonify({"message": "User is vidente y todos los vuelos en los que puede ayudar.", "vuelos" : vuelos})

@app.route("/ofrecer_ayuda", methods=["POST"])
def ofrecer_ayuda():
    data = request.json

    email_vidente = data["email_vidente"]
    email_no_vidente = data["email_no_vidente"]
    codigo = data["codigo"]

    conn = sqlite3.connect("database.db")

    cursor = conn.cursor()

    cursor.execute("INSERT INTO ofrecimientos (email_vidente, email_no_vidente, codigo) VALUES (?, ?, ?)", (email_vidente, email_no_vidente, codigo))

    conn.commit()

    conn.close()

    return jsonify({"message": f"Ayuda ofrecida de {email_vidente} a {email_no_vidente} en el vuelo {codigo}"})



@app.route("/")
def hello_world():
    return "<p>Hello World!</p>"

if __name__ == "__main__":
    app.run(debug=True)  # Enable debug mode for better error messages during development