import sqlite3

database = sqlite3.connect("muistio.db")

database.row_factory = sqlite3.Row


def get_database_connection():
    return database

