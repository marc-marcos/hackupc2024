import sqlite3

def create_db_ofrecimientos():
    conn = sqlite3.connect("database.db")

    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE ofrecimientos (
            email_vidente TEXT NOT NULL,
            email_no_vidente TEXT NOT NULL,
            codigo TEXT NOT NULL,
            FOREIGN KEY (email_vidente) REFERENCES users(email_vidente),
            FOREIGN KEY (email_no_vidente) REFERENCES users(email_no_vidente),
            FOREIGN KEY (codigo) REFERENCES vuelos(codigo)
        )
        """
    )

def create_db_usuarios():
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

def create_db_ayuda():
    conn = sqlite3.connect("database.db")

    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE ayuda (
            email TEXT NOT NULL,
            codigo TEXT NOT NULL,
            FOREIGN KEY (email) REFERENCES users(email),
            FOREIGN KEY (codigo) REFERENCES vuelos(codigo)
        )
        """
    )

    conn.commit()

    conn.close()

def create_db_vuelos():
    conn = sqlite3.connect("database.db")

    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE vuelos (
            codigo TEXT PRIMARY KEY,
            origen TEXT NOT NULL,
            destino TEXT NOT NULL,
            fecha TEXT NOT NULL,
            hora TEXT NOT NULL
        )
        """
    )

    conn.commit()

    conn.close()

def create_db_reservas():
    conn = sqlite3.connect("database.db")

    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE reservas (
            email TEXT NOT NULL,
            codigo TEXT NOT NULL,
            FOREIGN KEY (email) REFERENCES users(email),
            FOREIGN KEY (codigo) REFERENCES vuelos(codigo)
        )
        """
    )

    conn.commit()

    conn.close()

if __name__ == "__main__":
    create_db_reservas()
    create_db_vuelos()
    create_db_ayuda()
    create_db_usuarios()
    create_db_ofrecimientos()