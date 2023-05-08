
from connect_database import get_database_connection
from repositories.user_repository import user_repository


class NoteTools:
    """
    Luokka, joka vastaa tietokannan käsittelystä
    """
    def __init__(self, database):
        self._database = database

        """
        Database on tietokantayhteyden olio
        """

    def new_note(self, user_id, content):
        """
        Args:
            note (Note) eli yksi uusi muistiinpano

        Returns:
            note eli muistiinpano
        """
        cursor = self._database.cursor()
        cursor.execute("INSERT into Notes (user_id, content) values (?,?)", [user_id, content])
        self._database.commit()

    def remove_notes(self):
        cursor = self._database.cursor()
        cursor.execute("DELETE from Notes")
        self._database.commit()

    def all_notes(self, id):
        try:
            cursor = self._database.cursor()
            every = cursor.execute("SELECT content from Notes where user_id=?", [id]).fetchall()
            return every
        except:
            return ""

note_repository = NoteTools(get_database_connection())


