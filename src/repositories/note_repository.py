
from entities.note import Note
from database_connection import get_database_connection

class NoteTools:
    def __init__(self, db):
        self._db=db

    def new_note(self, note):
        cursor=self._db.cursor()
        cursor.execute("INSERT into Notes (user, text, time) values (?,?,?)",[note.user, note.text, note.time])
        self._db.commit()
        return note
    
    def remove_notes(self):
        cursor=self._db.cursor()
        cursor.execute("DELETE* from Notes")
        self._db.commit()

    def all_notes(self, user):
        cursor=self._db,cursor()
        every=cursor.execute("SELECT text, day from Notes where user_id=?",[user]).fetchall()
        return every

