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


class AddNewCar():
    root = Tk()
    root.geometry('1280x720')
    root.config(bg="#FFFFFF")
    title = root.title("Add A New Car")
    window_width = 1280
    window_height = 720
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)
    root.resizable(False, False)



    def __init__(self):



        self.filepath = None
        self.lbl1 = ut.create_label(self.root, width=293, height=62, text='Add A New Car', font=('Helvetica', 30))
        self.lbl1.pack()

        self.lbl2 = ut.create_label(self.root, width=95, height=23, text='Car Model', font=('Helvetica', 16))
        self.lbl2.pack()
        self.lbl2.place(x=60, y=95)

        self.fram1, self.text1 = ut.create_entry(self.root, width=365, height=35)
        self.fram1, self.text1.pack()
        self.fram1.place(x=60, y=120)

        self.lbl3 = ut.create_label(self.root, 115, 25, text='Horsepower', font=("Inter", 16))
        self.lbl3.pack()
        self.lbl3.place(x=830, y=95)

        self.fram2, self.text2 = ut.create_entry(self.root, width=365, height=35)
        self.fram2, self.text2.pack()
        self.fram2.place(x=830, y=120)

        self.lbl4 = ut.create_label(self.root, 170, 25, text='Car Manufacturer', font=("Inter", 16))
        self.lbl4.pack()
        self.lbl4.place(x=60, y=215)

        self.fram3, self.text3 = ut.create_entry(self.root, width=365, height=35)
        self.fram3, self.text3.pack()
        self.fram3.place(x=60, y=240)

        self.lbl5 = ut.create_label(self.root, 60, 25, text='Price', font=("Inter", 16))
        self.lbl5.pack()
        self.lbl5.place(x=830, y=215)

        self.fram4, self.text4 = ut.create_entry(self.root, width=356, height=35)
        self.fram4, self.text4.pack()
        self.fram4.place(x=830, y=240)

        self.lbl6 = ut.create_label(self.root, 170, 25, text='Engine Capacity', font=("Inter", 16))
        self.lbl6.pack()
        self.lbl6.place(x=60, y=335)

        self.fram5, self.text5 = ut.create_entry(self.root, width=365, height=35)
        self.fram5, self.text5.pack()
        self.fram5.place(x=60, y=360)

        self.lbl7 = ut.create_label(self.root, 55, 25, text='Year', font=("Inter", 16))
        self.lbl7.pack()
        self.lbl7.place(x=830, y=335)

        self.fram6, self.text6 = ut.create_entry(self.root, width=356, height=35)
        self.fram6, self.text6.pack()
        self.fram6.place(x=830, y=360)

        self.lbl_top = ut.create_label(self.root, 120, 25, text='Top Speed', font=("Inter", 16))
        self.lbl_top.pack()
        self.lbl_top.place(x=60, y=450)

        self.fram_top, self.top = ut.create_entry(self.root, width=365, height=35)
        self.fram_top, self.top.pack()
        self.fram_top.place(x=60, y=475)

        self.lbl8 = ut.create_label(self.root, 120, 25, text='Description', font=("Inter", 16))
        self.lbl8.pack()
        self.lbl8.place(x=60, y=565)

        self.fram7, self.text7 = ut.create_text_area(self.root, width=356, height=72)
        self.fram7, self.text7.pack()
        self.fram7.place(x=60, y=595)

        self.fram, self.btn_upload = ut.create_button(self.root, 170, 40, color='red', text='Upload Photo',
                                                      font=("Inter", 16))
        self.fram, self.btn_upload.pack()
        self.btn_upload.config(command=self.open_file)
        self.fram.place(x=830, y=460)

        self.lbl9 = ut.create_label(self.root, 100, 25, text='Photo.jpg', font=("Inter", 12))
        self.lbl9.pack()
        self.lbl9.place(x=1000, y=470)

        self.rbtn_var = StringVar()
        self.rbtn_var.set('sale')

        self.rbtn1 = Radiobutton(self.root, value='sale', text="For Sale",
                                 variable=self.rbtn_var, bg="#FFFFFF")
        self.rbtn2 = Radiobutton(self.root, value='rent', text="For Rent", variable=self.rbtn_var, bg="#FFFFFF")

        self.rbtn1.pack()
        self.rbtn1.place(x=830, y=530)
        self.rbtn2.pack()
        self.rbtn2.place(x=1000, y=530)

        self.fram1, self.btn_confirm = ut.create_button(self.root, 130, 40, color='red', text='Confirm',
                                                        font=("Inter", 14))
        self.fram1, self.btn_confirm.pack()
        self.btn_confirm.config(command=self.confirm)
        self.fram1.place(x=800, y=600)

        self.fram2, self.btn_back = ut.create_button(self.root, 130, 40, color='red', text='Back', font=("Inter", 14))
        self.fram2, self.btn_back.pack()
        self.fram2.place(x=950, y=600)

        self.fram3, self.btn_quit = ut.create_button(self.root, 130, 40, color='grey', text='Quit', font=("Inter", 14))
        self.fram3, self.btn_quit.pack()
        self.fram3.place(x=1100, y=600)

        self.root.mainloop()

        self.photo = ''


    def open_file(self):
        filepath =filedialog.askopenfilename()
        self.photo = filepath



    def confirm(self):
        car_id = str(uuid.uuid4())
        owner_id = User.current_user.id
        model = self.text1.get()
        horsepower = int(self.text2.get())
        manu = self.text3.get()
        year = self.text6.get()
        engine_capacity = int(self.text5.get())
        top_speed = int(self.top.get())
        price = int(self.text4.get())
        photo_path = self.photo
        car_description = self.text7.get("1.0",END)
        op_type = self.rbtn_var.get()
        state = "available"
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


window = AddNewCar()
