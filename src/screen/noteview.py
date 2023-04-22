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

    def show_note(self, note):
        pass

    def format(self):
        self._frame=ttk.Frame(master=self._root)
        header=ttk.Label(master=self._root, text="Muistiinpanosi")
        for note in self._notes:
            self.show_note(note)

        header.pack()
