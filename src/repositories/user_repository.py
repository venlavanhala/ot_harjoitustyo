
from connect_database import get_database_connection
from entities.user import User


class UserTools:
    """
    UserTools-luokka vastaa Users-tietokantataulun käsittelystä
    """
    def __init__(self, database):
        """
        Luokan UserTools konstruktori

        Args:
            database: Tietokantayhteyden olio
        """
        self._database = database

    def new_user(self, user:User):
        """Metodi lisää uuden käyttäjän tietokantaan

        Args:
            user (User)

        Raises:
            Exception: Palauttaa virheviestin, jos on tyhjiä kenttiä

        Returns:
            user (User)
        """
        if len(user.name)>0 and len(user.password)>0:
            cursor = self._database.cursor()
            cursor.execute("INSERT into Users (name, password) values (?,?)", [
                        user.name, user.password])
            self._database.commit()
            return user
        else:
            raise Exception("Käyttäjänimi tai salasana eivät saa olla tyhjiä")

    def check_if_exist(self, name):
        cursor=self._database.cursor()
        person=cursor.execute("SELECT id from Users where name=?",[name]).fetchone()
        self._database.commit()
        if person==None:
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
                              sign, word]).fetchone()[0]
        self._database.commit()
        return user

    def find_id(self, person):
        cursor=self._database.cursor()
        user=cursor.execute("SELECT id from Users where name=?",[person.name]).fetchone()
        self._database.commit()
        return user

user_repository=UserTools(get_database_connection())
