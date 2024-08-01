import Login
import Signup
from Signup import *
from tkinter import *
from Login import *


class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("The Autoshop!")
        self.geometry("800x600")
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        self.login_frame = Login(container,self)
        self.signup_frame = Signup(container,self)
        self.login_frame.grid(row=0, column=0)
        self.signup_frame.grid(row=0, column=0)
        self.show_frame("Signup")

    def show_frame(self,frame_name):
            if frame_name == "Signup":
                self.signup_frame.tkraise()
            elif frame_name == "Login":
                self.login_frame.tkraise()

app = App()
app.mainloop()
