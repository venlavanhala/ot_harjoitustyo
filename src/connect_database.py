import sqlite3
db=sqlite3.connect("muistio.db")

db.row_factory = sqlite3.Row


def get_database_connection():
    return db

