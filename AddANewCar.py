import datetime
from tkinter import *
from tkinter import filedialog
import mysql.connector
from tkinter import messagebox
from tkinter import ttk
import os
import uuid
import User
import Util as ut
import User as us
import Cars as cr
import DbConnection as db


class AddNewCar(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.pack_propagate(False)
        self.grid_propagate(False)
        self.config(width=1280, height=720, bg="#FFFFFF")
        self.lbl1 = ut.create_label(self, width=293, height=62, text='Add A New Car', font=('Helvetica', 30))
        self.lbl1.place(x=493, y=40)

        self.lbl2 = ut.create_label(self, width=95, height=23, text='Car Model', font=('Helvetica', 16))

        self.lbl2.place(x=60, y=105)

        self.fram1, self.text1 = ut.create_entry(self, width=365, height=35)
        self.fram1.place(x=60, y=130)

        self.lbl3 = ut.create_label(self, 115, 25, text='Horsepower', font=("Inter", 16))
        self.lbl3.place(x=830, y=105)

        self.fram2, self.text2 = ut.create_entry(self, width=365, height=35)
        self.fram2.place(x=830, y=130)

        self.lbl4 = ut.create_label(self, 170, 25, text='Car Manufacturer', font=("Inter", 16))
        self.lbl4.place(x=60, y=225)

        self.fram3, self.text3 = ut.create_entry(self, width=365, height=35)
        self.fram3.place(x=60, y=250)

        self.lbl5 = ut.create_label(self, 60, 25, text='Price', font=("Inter", 16))
        self.lbl5.place(x=830, y=225)

        self.fram4, self.text4 = ut.create_entry(self, width=356, height=35)
        self.fram4.place(x=830, y=250)

        self.lbl6 = ut.create_label(self, 170, 25, text='Engine Capacity', font=("Inter", 16))
        self.lbl6.place(x=60, y=345)

        self.fram5, self.text5 = ut.create_entry(self, width=365, height=35)
        self.fram5.place(x=60, y=370)

        self.lbl7 = ut.create_label(self, 55, 25, text='Year', font=("Inter", 16))
        self.lbl7.place(x=830, y=345)

        self.fram6, self.text6 = ut.create_entry(self, width=356, height=35)
        self.fram6.place(x=830, y=370)

        self.lbl_top = ut.create_label(self, 120, 25, text='Top Speed', font=("Inter", 16))
        self.lbl_top.place(x=60, y=460)

        self.fram_top, self.top = ut.create_entry(self, width=365, height=35)
        self.fram_top.place(x=60, y=485)

        self.lbl8 = ut.create_label(self, 120, 25, text='Description', font=("Inter", 16))
        self.lbl8.place(x=60, y=575)

        self.fram7, self.text7 = ut.create_text_area(self, width=356, height=72)
        self.fram7.place(x=60, y=605)

        self.fram, self.btn_upload = ut.create_button(self, 170, 40, color='red', text='Upload Photo',
                                                      font=("Inter", 16))
        self.btn_upload.config(command=self.open_file)
        self.fram.place(x=830, y=470)

        self.file_name_var = ""
        self.lbl9 = Label(self, text='', font=("Inter", 10), bg="#FFFFFF")
        self.lbl9.place(x=1015, y=480)

        self.rbtn_var = StringVar()
        self.rbtn_var.set('sale')

        self.rbtn1 = Radiobutton(self, value='sale', text="For Sale",
                                 variable=self.rbtn_var, bg="#FFFFFF", font=("Inter", 10, "bold"))
        self.rbtn2 = Radiobutton(self, value='rent', text="For Rent", variable=self.rbtn_var, bg="#FFFFFF",
                                 font=("Inter", 10, "bold"))

        self.rbtn1.place(x=830, y=540)
        self.rbtn2.place(x=1000, y=540)

        self.fram1, self.btn_confirm = ut.create_button(self, 130, 40, color='red', text='Confirm',
                                                        font=("Inter", 14))
        self.btn_confirm.config(command=self.confirm)
        self.fram1.place(x=803, y=656)

        self.fram2, self.btn_back = ut.create_button(self, 130, 40, color='red', text='Back', font=("Inter", 14))
        self.btn_back.config(command=lambda: controller.show_frame("listed_cars"))
        self.fram2.place(x=966, y=656)

        self.fram3, self.btn_quit = ut.create_button(self, 130, 40, color='grey', text='Quit', font=("Inter", 14))
        self.btn_quit.config(command=lambda: controller.show_frame("Login"))
        self.fram3.place(x=1129, y=656)

        self.photo = ''

    def open_file(self):
        filepath = filedialog.askopenfilename(initialdir="photos/", filetypes=(("JPG photos", "*.jpg"),
                                                                               ("PNG photos", "*.PNG"),
                                                                               ("JPEG photos", "*.jpeg")))
        self.photo = filepath
        self.lbl9.config(text=os.path.basename(self.photo))

    def confirm(self):
        car_id = str(uuid.uuid4())
        owner_id = User.current_user.id
        model = self.text1.get()

        manu = self.text3.get()
        year = self.text6.get()

        photo_path = os.path.normcase(self.photo)
        car_description = self.text7.get("1.0", END)
        op_type = self.rbtn_var.get()
        state = "available"
        errors = []
        if self.photo == '':
            errors.append("Invalid/Empty Photo")
        if not self.text2.get().isdigit():
            errors.append("Invalid Horsepower")
        else:
            horsepower = int(self.text2.get())
        if not self.top.get().isdigit():
            errors.append("Invalid Top Speed")
        else:
            top_speed = int(self.top.get())
        if not self.text4.get().isdigit():
            errors.append("Invalid Price")
        else:
            price = int(self.text4.get())

        if not self.text5.get().isdigit():
            errors.append("Invalid Engine Capacity")
        else:
            engine_capacity = int(self.text5.get())
        if not self.text6.get().isdigit() or len(
                self.text6.get()) > 4 or int(year) < 1900 or int(year) > 2024:
            errors.append("Invalid Year")

        if len(errors) > 0:
            errors_string = ""
            for error in errors:
                errors_string += error + "\n"
            messagebox.showerror(title="Error",
                                 message="Couldn't add car due to the following error(s):\n" + errors_string)

        else:
            dbc = db.connect_db()
            cursor = dbc.cursor()
            cursor.execute("INSERT INTO cars "
                           "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                           (car_id,
                            owner_id,
                            model,
                            manu,
                            year,
                            engine_capacity,
                            horsepower,
                            top_speed,
                            price,
                            photo_path,
                            car_description,
                            op_type,
                            state))
            dbc.commit()
            dbc.close()
            self.text5.delete(0, END)
            self.text1.delete(0, END)
            self.text2.delete(0, END)
            self.text3.delete(0, END)
            self.text4.delete(0, END)
            self.text6.delete(0, END)
            self.top.delete(0, END)
            self.text7.delete("1.0", END)
            self.photo = ""
            self.lbl9.config(text="")
