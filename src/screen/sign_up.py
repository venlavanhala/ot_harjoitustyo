from tkinter import ttk, constants
from services.notefavors import NoteFavors

class SignUpScreen:
    def __init__(self, root):
        self._root=root
        self._frame=None
        self._username=None
        self._password=None
        self.format()

    def create_user(self):
        name=self._username.get()
        password=self._password.get()
        try:
            NoteFavors.sign_up(name, password)
        except:
            pass

    def pack(self):
        self._frame.pack(fill=constants.X)

    def remove_screen(self):
        self._frame.destroy()

    def format(self):
        self._frame=ttk.Frame(master=self._root)
        label=ttk.Label(master=self._root, text="Uuden käyttäjän luonti")
        self._username=ttk.Entry(master=self._root, text="Käyttäjänimi")
        self._password=ttk.Entry(master=self._root, text="Salasana")
        enter=ttk.Button(master=self._root, text="Luo")
        signing=ttk.Button(master=self._root, text="Kirjaudu sisään")

        label.pack()
        self._username.pack()
        self._password.pack()
        enter.pack()
        signing.pack()
