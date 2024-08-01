from tkinter import *
from tkinter import ttk, messagebox
import DbConnection as db
import Util as ut
import bcrypt
import mysql.connector
import User
class Login(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.config(width=800, height=600, bg="#FFFFFF")
        self.welcome_lbl = ut.create_label(self, 303, 31, "Welcome to the Autoshop!", ("Helvitica", 18, "bold"))
        self.welcome_lbl.place(x=248, y=189)
        self.username_lbl = ut.create_label(self, 78, 16, "Username")
        self.username_lbl.place(x=253, y=268)
        self.username_frame, self.username_entry = ut.create_entry(self, 294, 38)
        self.username_frame.place(x=253, y=289)
        self.password_lbl = ut.create_label(self, 74, 16, "Password")
        self.password_lbl.place(x=253, y=332)
        self.password_frame, self.password_entry = ut.create_password(self, 294, 38)
        self.password_frame.place(x=253, y=353)
        self.login_btn_frame, self.login_btn = ut.create_button(self, 122, 33, "red", "Log In")
        self.login_btn_frame.place(x=425, y=430)
        self.signup_btn_frame, self.signup_btn = ut.create_button(self, 122, 33, "grey", "Sign up")
        self.signup_btn_frame.place(x=252, y=430)
        self.signup_btn.config(command=lambda: self.sign_up(controller))
        self.login_btn.config(command=self.login)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        curr_db = db.connect_db()
        cursor = curr_db.cursor()
        password = password.encode("utf-8")

        cursor.execute(f"SELECT * FROM users WHERE username = %s ", (username,))
        user = cursor.fetchone()
        valid = False
        if user is None:
            messagebox.showwarning("Error", "Wrong username or password")
            self.password_entry.delete(0, END)
        elif bcrypt.checkpw(password, user[2].encode("utf-8")):
            messagebox.showinfo("Success", "Signed in successfully")
            self.password_entry.delete(0, END)
            self.username_entry.delete(0, END)
            User.current_user.id = user[0]
            User.current_user.username = user[1]
            User.current_user.full_name = user[3]
            User.current_user.phone_num = user[4]
            User.current_user.age = user[5]
        else:
            messagebox.showwarning("Error", "Wrong username or password")
            self.password_entry.delete(0, END)

    def sign_up(self, controller):
        self.username_entry.delete(0, END)
        self.password_entry.delete(0, END)
        controller.show_frame("Signup")
