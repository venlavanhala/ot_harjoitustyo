from entities.user import User
from database_connection import get_database_connection

class UserTools:
    def __init__(self, db):
        self._db=db

    def new_user(self, user):
        cursor=self._db.cursor()
        cursor.execute("INSERT into Users (name, password) values (?,?)",[user.name, user.password])
        self._db.commit()
        return user
    
    def remove_users(self):
        cursor=self._db.cursor()
        cursor.execute("DELETE* from Users")
        self._db.commit()


