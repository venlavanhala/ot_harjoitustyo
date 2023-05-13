
from connect_database import get_database_connection

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
            note (Note): uusi muistiinpano
        """
        cursor = self._database.cursor()
        cursor.execute("INSERT into Notes (user_id, content) values (?,?)", [user_id, content])
        self._database.commit()

    def remove_notes(self):
        """
        Funktio, joka poistaa kaikki tallennetut muistiinpanot
        """
        cursor = self._database.cursor()
        cursor.execute("DELETE from Notes")
        self._database.commit()

    def all_notes(self, idnumber):
        """
        Funktio palauttaa tallennetut muistiinpanot listana

        Args:
            idnumber: Muistiinpanon id-numero

        Returns:
            notelist: Lista muistiinpanoista
        """
        notelist=[]
        try:
            cursor = self._database.cursor()
            every = cursor.execute("SELECT content from Notes where user_id=?", [idnumber]).fetchall()
            for unit in every:
                notelist.append(unit)
            return notelist
        except Exception:
            return ""

note_repository = NoteTools(get_database_connection())
