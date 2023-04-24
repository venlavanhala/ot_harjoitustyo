from tkinter import ttk, constants
from services.notefavors import NoteFavors

class NoteScreen:
    def __init__(self, root, notes, logout):
        self._root=root
        self._notes=notes
        self._frame=None
        self._user=NoteFavors.current_user()
        self.logout=logout

        self.format()

    def remove_screen(self):
        self._frame.destroy()

    def all_notes(self):
        self._notes=NoteFavors.return_notes(self._user)

    def pack(self):
        self._frame.pack(fill=constants.X)

    def format(self):
        self.all_notes
        header=ttk.Label(master=self._root, text="Muistiinpanosi")
        for note in self._notes:
            content=ttk.Label(master=self._root, text=note.text)
            content.pack()
        out=ttk.Button(master=self._root, text="Kirjaudu ulos", command=self.logout)
        header.pack()
        out.pack()
