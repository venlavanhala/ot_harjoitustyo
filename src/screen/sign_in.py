from tkinter import ttk, Tk
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
        enter=ttk.Button(master=self._root, text="Enter")
        signing=ttk.Button(master=self._root, text="Rekisteröidy")

        label.pack()
        self._name.pack()
        self._password.pack()
        enter.pack()
        signing.pack()

    def check(self):
        name=self._name.get()
        password=self._password.get()
        notefavours.sign_in(name, password)
        
        #check if the name and password exist

window = Tk()
window.title("Kirjautuminen")

ui = SignInScreen(window)
ui.start()

window.mainloop()