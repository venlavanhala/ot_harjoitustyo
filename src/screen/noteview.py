from tkinter import ttk, constants
from services.notefavors import NoteFavors

class NoteScreen:
    def __init__(self, root, logout):
        self._root=root
        self._frame=None
        favors=NoteFavors()
        self._user=favors.current_user()
        self._notes=favors.return_notes(self._user)
        self.logout=logout
        self.newnote=None
        self.format()

    def remove_screen(self):
        self._frame.destroy()

    #def all_notes(self):
        #self._notes=NoteFavors.return_notes(self._user)

    def new_note(self):
        content=self.newnote.get()
        NoteFavors.new_note(content)

    def pack(self):
        self._frame.pack(fill=constants.X)

    def format(self):
        header=ttk.Label(master=self._root, text="Muistiinpanosi")
        #self.all_notes()
        for note in self._notes:
            content=ttk.Label(master=self._root, text=note.text)
            content.pack()
        new=ttk.Label(master=self._root, text="Uusi muistiinpano")
        self.newnote=ttk.Entry(master=self._root, text="teksti: ")
        self.new_note
        out=ttk.Button(master=self._root, text="Kirjaudu ulos", command=self.logout)
        header.pack()
        new.pack()
        self.newnote.pack()
        out.pack()
