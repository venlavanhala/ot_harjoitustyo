from tkinter import Tk
from screen.interface import Interface


def main():
    window = Tk()
    window.title("Muistio")

    interface = Interface(window)
    interface.start()

    window.mainloop()


if __name__ == "__main__":
    main()