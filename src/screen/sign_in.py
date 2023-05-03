from tkinter import ttk, constants
from services.notefavors import notefavors, InvalidCredentialsError


class SignInScreen:
    def __init__(self, root, login, signup):
        self._root = root
        self._name = ""
        self._password = ""
        self._frame=None
        self._username=None
        self._password=None
        self.login=login
        self.signup=signup
        self.format()

    def signin(self):
        name = self._username.get()
        password = self._password.get()
        try:
            notefavors.sign_in(name, password)
            self.login
        except InvalidCredentialsError:
            raise ("Kirjautuminen ei onnistu")
        #if notefavors.sign_in(name, password)==None:
            #raise Exception("Kirjautuminen ei onnistunut")
        #else:
            #self._user=notefavors.sign_in(name, password)

    def pack(self):
        self._frame.pack(fill=constants.X)

    def remove_screen(self):
        self._frame.destroy()

    def format(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="Kirjaudu sisään", background = "#BFBFEF")
        self._username = ttk.Entry(master=self._frame, text="Käyttäjänimi")
        self._password = ttk.Entry(master=self._frame, text="Salasana")
        #self.signin
        enter = ttk.Button(master=self._frame, text="Enter", command=self.signin)
        signing = ttk.Button(master=self._frame, text="Rekisteröidy", command=self.signup)

        label.pack()
        self._username.pack()
        self._password.pack()
        enter.pack()
        signing.pack()
