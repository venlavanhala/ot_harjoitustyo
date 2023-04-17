
from connect_database import get_database_connection
from entities.user import User


class UserTools:
    def __init__(self, db):
        self._db = db

    def new_user(self, user):
        cursor = self._db.cursor()
        cursor.execute("INSERT into Users (name, password) values (?,?)", [
                       user.name, user.password])
        self._db.commit()
        return user

    def check_if_exist(self, name):
        cursor=self._db.cursor()
        person=cursor.execute("SELECT id from Users where name=?",[name]).fetchone()
        if id!=None:
            return False


    def remove_users(self):
        cursor = self._db.cursor()
        cursor.execute("DELETE* from Users")
        self._db.commit()

    def all_users(self):
        cursor = self._db.cursor()
        all = cursor.execute("SELECT * from Users").fetchall()
        self._db.commit()
        return all

    def find_user(self, sign, word):
        cursor = self._db.cursor()
        user = cursor.execute("SELECT name, password from Users where name=? and password=?", [
                              sign, word]).fetchone()
        self._db.commit()
        return user

    def find_id(self, name):
        cursor=self._db.cursor()
        user=cursor.execute("SELECT id from Users where name=?",[name]).fetchone()
        self._db.commit()
        return user