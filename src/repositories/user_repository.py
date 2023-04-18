
from connect_database import get_database_connection
from entities.user import User


class UserTools:
    def __init__(self, database):
        self._database = database

    def new_user(self, user:User):
        cursor = self._database.cursor()
        cursor.execute("INSERT into Users (name, password) values (?,?)", [
                       user.name, user.password])
        self._database.commit()
        return user

    def check_if_exist(self, name):
        cursor=self._database.cursor()
        person=cursor.execute("SELECT id from Users where name=?",[name]).fetchone()
        if person!="None":
            return False
        else:
            return True

    def remove_users(self):
        cursor = self._database.cursor()
        cursor.execute("DELETE * from Users")
        self._database.commit()

    def all_users(self):
        cursor = self._database.cursor()
        all = cursor.execute("SELECT * from Users").fetchall()
        self._database.commit()
        return all

    def find_user(self, sign, word):
        cursor = self._database.cursor()
        user = cursor.execute("SELECT name, password from Users where name=? and password=?", [
                              sign, word]).fetchone()
        self._database.commit()
        return user

    def find_id(self, name):
        cursor=self._database.cursor()
        user=cursor.execute("SELECT id from Users where name=?",[name]).fetchone()
        self._database.commit()
        return user
    
user_repository=UserTools(get_database_connection())