from tkinter import ttk, Tk
from services.notefavors import NoteFavors


class SignInScreen:
    def __init__(self, root, login, signup):
        self._root = root
        self._name = ""
        self._password = ""
        self._frame=None
        self._username=username
        self._password=password
        self.login=login
        self.signup=signup
        self.format()

    def signin(self):
        name = self._username.get()
        password = self._password.get()
        try:
            NoteFavors.sign_in(name, password)
            self.login()
        except:
            pass
        
    def remove_screen(self):
        self._frame.destroy()

    def format(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._root, text="Kirjaudu sisään")
        self._name = ttk.Entry(master=self._root, text="Käyttäjänimi")
        self._password = ttk.Entry(master=self._root, text="Salasana")
        enter = ttk.Button(master=self._root, text="Enter")
        signing = ttk.Button(master=self._root, text="Rekisteröidy")

        self._frame.pack()
        label.pack()
        self._name.pack()
        self._password.pack()
        enter.pack()
        signing.pack()

