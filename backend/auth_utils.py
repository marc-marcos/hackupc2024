import sqlite3
import random
import string

def create_db_tokens():
    conn = sqlite3.connect("database.db")

    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE tokens (
            token TEXT PRIMARY KEY,
            email TEXT NOT NULL,
            FOREIGN KEY (email) REFERENCES users(email)
        )
        """
    )

    conn.commit()

    conn.close()

def create_token(email):
    token = ''.join(random.choice(string.ascii_lowercase) for i in range(64))
    conn = sqlite3.connect("database.db")

    cursor = conn.cursor()

    cursor.execute("INSERT INTO tokens (token, email) VALUES (?, ?)", (token, email))

    conn.commit()

    conn.close()

def check_token(email, token):
    # check if the token of the specified email equals to the token
    conn = sqlite3.connect("database.db")

    cursor = conn.cursor()

    cursor.execute("SELECT FROM tokens WHERE email = ?", email)

    token_uno = cursor.fetchone()

    return token_uno == token

def destroy_token(email):
    conn = sqlite3.connect("database.db")

    cursor = conn.cursor()

    cursor.execute("DELETE FROM tokens WHERE email = ?", email)

if __name__ == '__main__':
    create_db_tokens()