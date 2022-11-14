from tkinter import Tk, Frame, Entry, Label, Button
from ttkbootstrap import * 
from ttkthemes import ThemedTk
class Login:
    def __init__(self) -> None:
        self.TelaLogin = ThemedTk(theme='arc')
        self.TelaLogin.title("Login")

        self.TelaLogin.mainloop()    