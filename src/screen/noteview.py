from tkinter import ttk
from services.notefavors import NoteFavors

class NoteScreen:
    def __init__(self, root, notes):
        self._root=root
        self._notes=notes
        self._frame=None

        self.format()

    def remove_screen(self):
        self._frame.destroy()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def format(self):
        header=ttk.Label(master=self._root, text="Muistiinpanosi")
        for note in self._notes:
            content=ttk.Label(master=self._root, text=note.text)
            content.pack()
        header.pack()
        self._frame.pack()
