from tkinter import *
from tkinter import ttk, messagebox

import mysql.connector

import DbConnection as db
import Util as ut
import bcrypt
import uuid


class Signup(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.config(width=1280, height=720, bg="#FFFFFF")
        self.mainWindow = Frame(self)
        self.signup_lbl = ut.create_label(self, width=138, height=65, text="Sign Up",
                                          font=("Helvetica", 26, "bold"))
        self.username_lbl = ut.create_label(self, 78, 19, "Username")
        self.username_frame, self.username_entry = ut.create_entry(self, 243, 33)
        self.fullname_lbl = ut.create_label(self, 75, 19, "Full name")
        self.fullname_frame, self.fullname_entry = ut.create_entry(self, 243, 33)
        self.age_lbl = ut.create_label(self, 30, 19, "Age")
        self.age_frame, self.age_entry = ut.create_entry(self, 243, 33)
        self.phone_num_lbl = ut.create_label(self, 113, 19, "Phone Number")
        self.phone_num_frame, self.phone_num_entry = ut.create_entry(self, 243, 33)
        self.password_lbl = ut.create_label(self, 74, 19, "Password")
        self.password_frame, self.password_entry = ut.create_password(self, 243, 33)
        self.confirm_password_lbl = ut.create_label(self, 139, 19, "Confirm Password")
        self.confirm_password_frame, self.confirm_password_entry = ut.create_password(self, 243, 33)
        self.back_frame, self.back_btn = ut.create_button(self, 106, 40, "grey", text="Back")
        self.signup_frame, self.signup_btn = ut.create_button(self, 106, 40, "red", text="Sign Up")
        self.signup_lbl.place(x=571, y=102)
        self.username_lbl.place(x=275, y=262)
        self.username_frame.place(x=275, y=281)
        self.fullname_lbl.place(x=275, y=336)
        self.fullname_frame.place(x=275, y=355)
        self.age_lbl.place(x=275, y=405)
        self.age_frame.place(x=275, y=428)
        self.phone_num_lbl.place(x=761, y=258)
        self.phone_num_frame.place(x=761, y=281)
        self.password_lbl.place(x=761, y=336)
        self.password_frame.place(x=761, y=355)
        self.confirm_password_lbl.place(x=761, y=405)
        self.confirm_password_frame.place(x=761, y=428)
        self.signup_frame.place(x=657, y=581)
        self.signup_btn.config(command=self.signup)
        self.back_frame.place(x=517, y=581)
        self.back_btn.config(command=lambda: controller.show_frame("Login"))

    def signup(self):
        curr_db = db.connect_db()
        cursor = curr_db.cursor()
        username = self.username_entry.get()
        password = self.password_entry.get()
        age = self.age_entry.get()
        fullname = self.fullname_entry.get()
        phone_num = self.phone_num_entry.get()
        password = password.encode("utf-8")
        hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
        user_id = str(uuid.uuid4())
        errors = []
        if len(password) < 8:
            errors.append("Password must be at least 8 characters")
        if len(phone_num) < 11 or not phone_num.isdigit():
            errors.append("Invalid phone number")
        if not age.isdigit() or int(age) < 1:
            errors.append("Invalid age")
        if self.password_entry.get() != self.confirm_password_entry.get():
            errors.append("Passwords do not match")

        values = (user_id, username, hashed_password, fullname, phone_num, age)
        try:
            cursor.execute(
                "INSERT INTO users (ID, username, passw, full_name, phone_number, age) VALUES (%s,%s,%s,%s,%s,%s)",
                values)

        except (mysql.connector.IntegrityError, mysql.connector.DatabaseError) as err:
            errors.append("Username is already taken")
        if len(errors) == 0:
            curr_db.commit()
            messagebox.showinfo(title="Success", message="You have successfully Signed up")
        else:
            msg = "Couldn't sign you up because of the following error(s): \n"
            for error in errors:
                msg += error + "\n"
            messagebox.showerror(title="Error", message=msg)
        curr_db.close()
