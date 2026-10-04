import sqlite3
from config import DATABASE_PATH

def get_database_connection():
    c=sqlite3.connect(DATABASE_PATH); c.row_factory=sqlite3.Row; return c

def initialize_database():
    c=get_database_connection()
    try:
        c.execute('''CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, roll_no TEXT NOT NULL UNIQUE, email TEXT NOT NULL, course TEXT NOT NULL)'''); c.commit()
    finally: c.close()
