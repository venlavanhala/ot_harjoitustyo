from tkinter import ttk, constants
from services.notefavors import notefavors, InvalidCredentialsError


class SignInScreen:
    """Luokka, joka käsittelee kirjautumisnäkymää
    """
    def __init__(self, root, login, signup):
        """
            login: Kutsuttava arvo, kun vaihdetaan muistiinpanonäkymään
            signup: Kutsuttava arvo, kun vaihdetaan rekisteröintinäkymään
        """
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
        """Ottaa syötetyn nimen ja salasanan, ja kutsuu kirjautumista hoitavaa funktiota
        """
        name = self._username.get()
        password = self._password.get()
        try:
            notefavors.sign_in(name, password)
            self.login()
        except InvalidCredentialsError:
            raise "Kirjautuminen ei onnistu" from InvalidCredentialsError

    def pack(self):
        """Luo näkymän
        """
        self._frame.pack(fill=constants.X)

    def remove_screen(self):
        """Poistaa näkymän
        """
        self._frame.destroy()

    def format(self):
        """Määrittää, mitä näkymään laitetaan
        """
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="Kirjaudu sisään", background = "#BFBFEF", font=('Times', 20))
        self._username = ttk.Entry(master=self._frame, text="Käyttäjänimi")
        self._password = ttk.Entry(master=self._frame, text="Salasana")
        enter = ttk.Button(master=self._frame, text="Enter", command=self.signin)
        signing = ttk.Button(master=self._frame, text="Rekisteröidy", command=self.signup)

        label.pack()
        self._username.pack()
        self._password.pack()
        enter.pack()
        signing.pack()
