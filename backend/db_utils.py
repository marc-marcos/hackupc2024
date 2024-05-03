import sqlite3

def create_db():
    conn = sqlite3.connect("database.db")

    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE users (
            email TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            surname TEXT NOT NULL,
            password TEXT NOT NULL,
            vidente BOOLEAN NOT NULL
        )
        """
    )

    conn.commit()

    conn.close()

if __name__ == "__main__":
    create_db()