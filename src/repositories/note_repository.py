
from connect_database import get_database_connection
from entities.note import Note


class NoteTools:
    def __init__(self, database):
        self._database = database

    def new_note(self, note:Note):
        cursor = self._database.cursor()
        cursor.execute("INSERT into Notes (user, text, time) values (?,?,?)", [
                       note.user, note.text, note.time])
        self._database.commit()
        return note

    def remove_notes(self):
        cursor = self._database.cursor()
        cursor.execute("DELETE* from Notes")
        self._database.commit()

    def all_notes(self, user):
        cursor = self._database.cursor()
        every = cursor.execute(
            "SELECT text, day from Notes where user_id=?", [user]).fetchall()
        return every

note_repository = UserTools(get_database_connection())