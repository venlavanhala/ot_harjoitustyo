import sqlite3
import os


dirname=os.path.dirname(__file__)

basename=os.getenv("basename") or "muistio.db"
path=os.path.join(dirname, "..", basename)
database=sqlite3.connect(path)
#database = sqlite3.connect("muistio.db")

database.row_factory = sqlite3.Row


def get_database_connection():
    return database

