from tkinter import ttk, constants
from services.notefavors import notefavors

class NoteScreen:
    def __init__(self, root, logout):
        self._root=root
        self._frame=None
        self._user=notefavors.current_user()
        self._notes=notefavors.return_notes(self._user)
        self.logout=logout
        self.newnote=None
        self.format()

    def remove_screen(self):
        self._frame.destroy()

    #def all_notes(self):
        #self._notes=NoteFavors.return_notes(self._user)

    def new_note(self):
        text=self.newnote.get()
        notefavors.new_note(text)

    def pack(self):
        self._frame.pack(fill=constants.X)

    def format(self):
        self._frame = ttk.Frame(master=self._root)
        header=ttk.Label(master=self._frame, text="Muistiinpanosi", background = "#BFBFEF")
        #self.all_notes()
        for note in self._notes:
            content=ttk.Label(master=self._frame, text=note.text)
            content.pack()
        new=ttk.Label(master=self._frame, text="Uusi muistiinpano", background = "#BFBFEF")
        self.newnote=ttk.Entry(master=self._frame, text="teksti: ")
        self.new_note
        enter=ttk.Button(master=self._frame, text="Enter")
        out=ttk.Button(master=self._frame, text="Kirjaudu ulos", command=self.logout)
        header.pack()
        new.pack()
        self.newnote.pack()
        enter.pack()
        out.pack()
