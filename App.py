import Login
import Signup
from Signup import *
from tkinter import *
from Login import *


class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("The Autoshop!")
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"800x600+{int((screen_width-800)/2)}+{int((screen_height-600)/2)}")
        self.resizable(False, False)
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        self.login_frame = Login(container,self)
        self.signup_frame = Signup(container,self)
        self.login_frame.grid(row=0, column=0)
        self.signup_frame.grid(row=0, column=0)
        self.show_frame("Login")
    def resize_window(self,width,height):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"{width}x{height}+{int((screen_width-width)/2)}+{int((screen_height-height)/2)}")



    def show_frame(self,frame_name):
            if frame_name == "Signup":
                self.resize_window(800,600)
                self.signup_frame.tkraise()
            elif frame_name == "Login":
                self.resize_window(800,600)
                self.login_frame.tkraise()

app = App()
app.mainloop()
