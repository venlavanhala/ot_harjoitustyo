from tkinter import ttk, constants, StringVar
from services.notefavors import notefavors

class NoteScreen:
    """Luokka, joka käsittelee ja luo muistiinpanonäkymän
    """
    def __init__(self, root, logout):
        """
        Args:
            logout: Kutsuttava metodi, jonka avulla uloskirjaudutaan
        """
        self._root=root
        self._frame=None
        self._user=notefavors.current_user()
        self._notes=notefavors.return_notes()
        self.logout=logout
        self._note_variable=StringVar()
        self.format()

    def remove_screen(self):
        """Poistaa näkymän
        """
        self._frame.destroy()

    def new_note(self):
        """Ottaa syötetyn muistiinpanon, ja käskee notefavors-luokkaa tallentamaan sen
        """
        text=self._note_variable.get()
        notefavors.new_note(text)

    def pack(self):
        """Luo näkymän
        """
        self._frame.pack(fill=constants.X)

    def format_note(self, note):
        """Määrittää, miten yksi muistiinpano näytetään

        Args:
            note: Yksi muistiinpano
        """
        content = ttk.Label(master=self._frame, text=note, font=('Times', 18))
        content.pack()

    def initialize_notes(self):
        """Alustaa muistiinpanot
        """
        item_frame=ttk.Frame(master=self._frame)
        try:
            for note in self._notes:
                note=ttk.Label(master=item_frame, text=note)
                note.pack()
        except:
            pass

    def store(self):
        """Kutsuu muistiinpanon tallennusfunktiota, ja sitten tyhjentää kirjoituskentän
        """
        self.new_note()
        self._note_variable.set("")

    def format(self):
        """Funktio, joka määrittää, mitä näkymään tulee
        """
        self._frame = ttk.Frame(master=self._root)
        header=ttk.Label(master=self._frame, text="Muistiinpanosi", font=('Times', 20), background = "#BFBFEF")
        self.initialize_notes()
        new=ttk.Label(master=self._frame, text="Uusi muistiinpano", background = "#BFBFEF")
        newnote=ttk.Entry(master=self._frame, textvariable=self._note_variable)
        enter=ttk.Button(master=self._frame, text="Enter", command=self.store)
        out=ttk.Button(master=self._frame, text="Kirjaudu ulos", command=self.logout)
        header.pack()
        new.pack()
        newnote.pack()
        enter.pack()
        out.pack()
