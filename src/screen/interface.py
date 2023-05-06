
from screen.sign_in import SignInScreen
from screen.sign_up import SignUpScreen
from screen.noteview import NoteScreen

class Interface:
    def __init__(self, root):
        self._root = root
        self._view = None

    def start(self):
        self.sign_view()

    def remove_view(self):
        if self._view!=None:
            self._view.remove_screen()
        self._view = None

    def sign_view(self):
        self.remove_view()
        self._view = SignInScreen(self._root, self.note_view, self.signup_view)
        self._view.pack()

    def note_view(self):
        self.remove_view()
        self._view=NoteScreen(self._root, self.sign_view)
        self._view.pack()

    def signup_view(self):
        self.remove_view()
        self._view=SignUpScreen(self._root, self.sign_view)
        self._view.pack()


#window = Tk()
#window.title("Muistio")

#screen = Interface(window)
#screen.start()

#window.mainloop()
