import sqlite3
import os


dirname=os.path.dirname(__file__)

#basename=os.getenv("basename") or "muistio.db"
path=os.path.join(dirname, "muistio.db")
database=sqlite3.connect(path)

database.row_factory = sqlite3.Row


def chk_conn(conn): #check the connection
     try:
        conn.cursor()
        return True
     except Exception as ex:
        return False


def get_database_connection():
    print(chk_conn(database))
    return database

