import sqlite3
from fastapi import Depends


DB_PATH = "inventory.db"

def get_connection():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS items (
        id TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        quantity INTEGER NOT NULL,
        price REAL NOT NULL
    )
    """)
    conn.commit()
    conn.close()


def get_db():
    conn = get_connection()
    try:
        yield conn
    finally:
        conn.close()