from tkinter import *
from tkinter import ttk
import DbConnection as db
import Util as ut


class Signup:
    mainWindow = Tk()
    signup_lbl = ut.create_label(mainWindow, width=138, height=65, text="Sign Up", font=("Helvetica", 26, "bold"))
    username_lbl = ut.create_label(mainWindow, 78, 19, "Username")
    username_entry = ut.create_entry(mainWindow, 243, 33)
    fullname_lbl = ut.create_label(mainWindow, 75, 19, "Full name")
    fullname_entry = ut.create_entry(mainWindow, 243, 33)
    age_lbl = ut.create_label(mainWindow, 30, 19, "Age")
    age_entry = ut.create_entry(mainWindow, 243, 33)
    phone_num_lbl = ut.create_label(mainWindow, 113, 19, "Phone Number")
    phone_num_entry = ut.create_entry(mainWindow, 243, 33)
    password_lbl = ut.create_label(mainWindow, 74, 19, "Password")
    password_entry = ut.create_password(mainWindow, 243, 33)
    confirm_password_lbl = ut.create_label(mainWindow, 139, 19, "Confirm Password")
    confirm_password_entry = ut.create_password(mainWindow, 243, 33)
    back_frame, back_btn = ut.create_button(mainWindow, 106, 40, "grey", text="Back")
    signup_frame, signup_btn = ut.create_button(mainWindow, 106, 40, "red", text="Sign Up")

    def __init__(self):
        self.mainWindow.title("The Autoshop")
        self.mainWindow.config(bg="#FFFFFF")
        self.mainWindow.resizable(False, False)
        self.mainWindow.geometry("800x600")
        self.signup_lbl.place(x=331, y=73)
        self.username_lbl.place(x=35, y=191)
        self.username_entry.place(x=35, y=210)
        self.fullname_lbl.place(x=35, y=265)
        self.fullname_entry.place(x=35, y=284)
        self.age_lbl.place(x=35, y=334)
        self.age_entry.place(x=35, y=357)
        self.phone_num_lbl.place(x=521, y=187)
        self.phone_num_entry.place(x=521, y=210)
        self.password_lbl.place(x=521, y=265)
        self.password_entry.place(x=521, y=284)
        self.confirm_password_lbl.place(x=521, y=334)
        self.confirm_password_entry.place(x=521, y=357)
        self.signup_frame.place(x=417,y=453)
        self.back_frame.place(x=277,y=453)
        self.mainWindow.mainloop()

    def signup(self):
        pass

    def back(self):
        pass



signup = Signup()

