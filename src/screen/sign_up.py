from tkinter import ttk, constants
from services.notefavors import notefavors

class SignUpScreen:
    """
    Rekisteröintinäkymä
    """
    def __init__(self, root, login):
        """
        Luokan konstruktori

        Args: 
        root : juuri
        login : Kutsutaan login arvoa kun kirjaudutaan sisään
        """
        self._root=root
        self._frame=None
        self._username=None
        self._password=None
        self.login=login
        self.format()

    def create_user(self):
        """
        Uuden käyttäjän luomisen hoitava metodi
        """
        name=self._username.get()
        password=self._password.get()
        notefavors.sign_up(name, password)
        #except:
            #raise Exception("Samanniminen käyttäjä on jo olemassa")

    def pack(self):
        self._frame.pack(fill=constants.X)

    def remove_screen(self):
        self._frame.destroy()

    def format(self):
        self._frame=ttk.Frame(master=self._root)
        label=ttk.Label(master=self._frame, text="Uuden käyttäjän luonti", background = "#BFBFEF")
        self._username=ttk.Entry(master=self._frame, text="Käyttäjänimi")
        self._password=ttk.Entry(master=self._frame, text="Salasana")
        enter=ttk.Button(master=self._frame, text="Luo", command=self.create_user)
        signing=ttk.Button(master=self._frame, text="Kirjaudu sisään", command=self.login)

        label.pack()
        self._username.pack()
        self._password.pack()
        enter.pack()
        signing.pack()
