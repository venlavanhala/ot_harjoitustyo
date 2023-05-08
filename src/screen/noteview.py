from tkinter import ttk, constants, StringVar
from services.notefavors import notefavors

class NoteScreen:
    def __init__(self, root, logout):
        self._root=root
        self._frame=None
        self._user=notefavors.current_user()
        self._notes=notefavors.return_notes()
        self.logout=logout
        self._note_variable=StringVar()
        #self.newnote=None
        self.format()

    def remove_screen(self):
        self._frame.destroy()

    #def all_notes(self):
        #self._notes=NoteFavors.return_notes(self._user)

    def new_note(self):
        #text=self.newnote.get()
        text=self._note_variable.get()
        notefavors.new_note(text)

    def pack(self):
        self._frame.pack(fill=constants.X)

    def format_note(self, note):
        #noteframe = ttk.Frame(master=self._frame)
        content = ttk.Label(master=self._root, text=note, font=('Times', 18))
        #noteframe.pack()
        content.pack()

    def initialize_notes(self):
        notes=ttk.Label(master=self._frame, text=self._notes)
        notes.pack()

    def store(self):
        self.new_note()
        self._note_variable.set("")

    def format(self):
        self._frame = ttk.Frame(master=self._root)
        header=ttk.Label(master=self._frame, text="Muistiinpanosi", font=('Times', 20), background = "#BFBFEF")
        #for note in self._notes:
            #self.format_note(note)
        self.initialize_notes()
        new=ttk.Label(master=self._frame, text="Uusi muistiinpano", background = "#BFBFEF")
        newnote=ttk.Entry(master=self._frame, textvariable=self._note_variable)
        enter=ttk.Button(master=self._frame, text="Enter", command=self.store)
        out=ttk.Button(master=self._frame, text="Kirjaudu ulos", command=self.logout)
        header.pack()
        #notes.pack()
        new.pack()
        newnote.pack()
        enter.pack()
        out.pack()

        # muistiinpano ilmestyy kenttään ja pysyy siellä vaikka kirjaudutaan välissä ulos
