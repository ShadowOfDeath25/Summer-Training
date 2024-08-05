from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector
import os
import DbConnection as db
import Util as ut
import User as us
import Cars as cr
import bcrypt
import uuid
class rentedCars:
    root = Tk()
    query = ("SELECT * FROM RENTALS "
             "JOIN CARS on cars.car_id=rentals.car_id "
             "WHERE RENTALS.renter_id = %s")

    dbc = db.connect_db()
    cursor = dbc.cursor()
    cursor.execute(query,us.current_user.id)
    cars = cursor.fetchall()

    root.geometry('1280x720')
    root.config(bg="#FFFFFF")
    title =root.title("rented cars")
    car1 = Label(root, text="Hyundai Elantra 2022", font=("Helvetica", 16),background='white')
    car1.place(x=302, y=179, anchor='w')
    car2 = Label(root, text="BMW M3 2010", font=("Helvetica", 16),background='white')
    car2.place(x=302, y=346, anchor='w')
    car3 = Label(root, text="Volkswagen Golf 2005", font=("Helvetica", 16),background='white')
    car3.place(x=302, y=492, anchor='w')
    image1_path = "photos/download.jpg"
    image1 = Image.open(image1_path)
    image1 = image1.resize((247, 143))
    photo1 = ImageTk.PhotoImage(image1)
    lbl =Label(root,image=photo1,height=143,width=248,background='white')
    lbl.place(x=32,y=117)
    image2_path = "photos/2010-bmw-m3.jpg"
    image2 = Image.open(image2_path)
    image2 = image2.resize((248, 143))
    photo2 = ImageTk.PhotoImage(image2)
    lbl =Label(root,image=photo2,height=143,width=248,background='white')
    lbl.place(x=32,y=270)
    image3_path = "photos/images.jpg"
    image3 = Image.open(image3_path)
    image3 = image3.resize((248, 143))
    photo3 = ImageTk.PhotoImage(image3)
    lbl =Label(root,image=photo3,height=143,width=248,background='white')
    lbl.place(x=32,y=430)
   
    
    f="Helvetica", 17
    f1="Helvetica", 14
    lbl1=ut.create_label(root,width=274,height=17,text="Rented Cars",font=f)
    lbl1.place(x=32,y=30)
    fram1, btn_back = ut.create_button(root, 121, 40, color='red', text='Back', font=f1)
    fram1, btn_back.pack()
    fram1.place(x=980, y=660)
    fram2, btn_quit = ut.create_button(root, 121, 40, color='grey', text='Quit', font=(f1))
    fram2, btn_quit.pack()
    fram2.place(x=1127, y=660)
    def data(y,root):
        lbl1=ut.create_label(root,width=175,height=44,text="Rent Date : (Rent Date)\nReturn Date (Return Date)",font=("Helvetica", 7))
        lbl1.place(x=1086,y=y)
    data(133,root)
    data(319,root)
    data(469,root)
    def cancel(y,root):
        btn_cancel_fram, btn_cancel = ut.create_button(root, 77, 40, color='red', text='Cancel', font=("Helvetica", 14))
        btn_cancel_fram.place(x=1133,y=y)
    cancel(354,root)
    cancel(168,root)
    cancel(504,root)
    root.mainloop()
