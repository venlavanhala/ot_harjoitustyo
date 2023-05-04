
from connect_database import get_database_connection
from repositories.user_repository import user_repository
from entities.note import Note


class NoteTools:
    """
    Luokka, joka vastaa tietokannan käsittelystä
    """
    def __init__(self, database):
        self._database = database

        """
        Database on tietokantayhteyden olio
        """

    def new_note(self, note:Note):
        """
        Args:
            note (Note) eli yksi uusi muistiinpano

        Returns:
            note eli muistiinpano
        """
        cursor = self._database.cursor()
        cursor.execute("INSERT into Notes (user, day, content) values (?,?,?)", [
                       note.user, note.time, note.text])
        self._database.commit()
        return note

    def remove_notes(self):
        cursor = self._database.cursor()
        cursor.execute("DELETE* from Notes")
        self._database.commit()

    def all_notes(self, user):
        identity=user_repository.find_id(user.name)
        cursor = self._database.cursor()
        every = cursor.execute("SELECT day, content from Notes where user_id=?", [identity]).fetchall()
        return every

note_repository = NoteTools(get_database_connection())
