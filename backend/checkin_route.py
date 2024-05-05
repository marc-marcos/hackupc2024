from flask import Flask, jsonify
import sqlite3

@app.route("/checkin_clicked", methods=["POST"])

def checkin_clicked():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT vidente FROM users WHERE email = ?, email")
    vidente = cursor.fetchone()
    if vidente:
        return jsonify({"message": "Voluntario"})
    else:
        return jsonify({"message": "Invidente"}) 