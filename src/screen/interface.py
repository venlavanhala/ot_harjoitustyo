from tkinter import Tk
from screen.sign_in import SignInScreen

class Interface:
    def __init__(self, root):
        self._root = root
        self._view = None

    def start(self):
        self._sign_view()
    
    def sign_view(self):
        self._view = SignInScreen(self._root)

window = Tk()
window.title("User Interface")

screen = Interface(window)
screen.start()

window.mainloop()