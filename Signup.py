from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector
import DbConnection as db
import Util as ut
import bcrypt
import uuid
class Signup:
    mainWindow = Tk()
    signup_lbl = ut.create_label(mainWindow, width=138, height=65, text="Sign Up", font=("Helvetica", 26, "bold"))
    username_lbl = ut.create_label(mainWindow, 78, 19, "Username")
    username_frame, username_entry = ut.create_entry(mainWindow, 243, 33)
    fullname_lbl = ut.create_label(mainWindow, 75, 19, "Full name")
    fullname_frame, fullname_entry = ut.create_entry(mainWindow, 243, 33)
    age_lbl = ut.create_label(mainWindow, 30, 19, "Age")
    age_frame, age_entry = ut.create_entry(mainWindow, 243, 33)
    phone_num_lbl = ut.create_label(mainWindow, 113, 19, "Phone Number")
    phone_num_frame, phone_num_entry = ut.create_entry(mainWindow, 243, 33)
    password_lbl = ut.create_label(mainWindow, 74, 19, "Password")
    password_frame, password_entry = ut.create_password(mainWindow, 243, 33)
    confirm_password_lbl = ut.create_label(mainWindow, 139, 19, "Confirm Password")
    confirm_password_frame, confirm_password_entry = ut.create_password(mainWindow, 243, 33)
    back_frame, back_btn = ut.create_button(mainWindow, 106, 40, "grey", text="Back")
    signup_frame, signup_btn = ut.create_button(mainWindow, 106, 40, "red", text="Sign Up")

    def __init__(self):
        screen_width = self.mainWindow.winfo_screenwidth()
        screen_height = self.mainWindow.winfo_screenheight()
        x = int((screen_width - 800) / 2)
        y = int((screen_height - 600) / 2)
        self.mainWindow.title("The Autoshop")
        self.mainWindow.config(bg="#FFFFFF")
        self.mainWindow.resizable(False, False)
        self.mainWindow.geometry(f"800x600+{x}+{y}")
        self.signup_lbl.place(x=331, y=73)
        self.username_lbl.place(x=35, y=191)
        self.username_frame.place(x=35, y=210)
        self.fullname_lbl.place(x=35, y=265)
        self.fullname_frame.place(x=35, y=284)
        self.age_lbl.place(x=35, y=334)
        self.age_frame.place(x=35, y=357)
        self.phone_num_lbl.place(x=521, y=187)
        self.phone_num_frame.place(x=521, y=210)
        self.password_lbl.place(x=521, y=265)
        self.password_frame.place(x=521, y=284)
        self.confirm_password_lbl.place(x=521, y=334)
        self.confirm_password_frame.place(x=521, y=357)
        self.signup_frame.place(x=417, y=453)
        self.signup_btn.config(command=self.signup)
        self.back_frame.place(x=277, y=453)
        self.mainWindow.mainloop()

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

    def back(self):
        pass


signup = Signup()
