import sqlite3

def dbconnection():
    return sqlite3.connect("products.db")

def create_table():
    con = dbconnection()
    cursor = con.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            quantity INTEGER NOT NULL
        )
    ''')

    con.commit()
    con.close()

def execute_query(query, params=(), commit=False):
    con = dbconnection()
    cursor = con.cursor()

    cursor.execute(query, params)
    
    if commit:
        con.commit()
    
    result = cursor.fetchall()
    con.close()
    return result

def execute_commit(query, params=()):
    con = dbconnection()
    cursor = con.cursor()
    cursor.execute(query, params)
    con.commit()
    con.close()