from tkinter import ttk, StringVar, constants, Tk
from services.notefavors import notefavors

class SignInScreen:
    def __init__(self, root):
        self._root=root
        self._name=""
        self._password=""

    def view(self):
        label=ttk.Label(master=self._root, text="Kirjaudu sisään")
        self._name=ttk.Entry(master=self._root, text="Käyttäjänimi")
        self._password=ttk.Entry(master=self._root, text="Salasana")
        signing=ttk.Button(master=self._root, text="Rekisteröidy")

        label.pack()
        self._name.pack()
        self._password.pack()
        signing.pack()

    def check(self):
        pass
        #check if the name and password exist

window = Tk()
window.title("Kirjautuminen")

ui = SignInScreen(window)
ui.start()

window.mainloop()