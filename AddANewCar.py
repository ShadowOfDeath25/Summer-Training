from tkinter import *
import mysql.connector
from tkinter import messagebox
from tkinter.ttk import *
import os
import Util as ut
import User as us
import Cars as cr
import DbConnection as db





class AddNewCar:
    root = Tk()
    root.geometry('1280x720')
    root.config(bg="#FFFFFF")
    title =root.title("Add A New Car")
    window_width = 1280
    window_height = 720
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)
    root.resizable(False, False)






    lbl1 =ut.create_label(root,width=293,height=62,text='Add A New Car',font=('Helvetica',30))
    lbl1 .pack()

    lbl2 = ut.create_label(root, width=95, height=23, text='Car Model', font=('Helvetica', 16))
    lbl2.pack()
    lbl2.place(x =60, y =95)

    fram1,text1=ut.create_entry(root,width=365,height=35)
    fram1,text1.pack()
    fram1.place(x =60, y =120)

    lbl3=ut.create_label(root,115,25,text='Horsepower',font=("Inter",16))
    lbl3.pack()
    lbl3.place(x =830, y =95)

    fram2,text2=ut.create_entry(root,width=365,height=35)
    fram2,text2.pack()
    fram2.place(x =830, y =120)

    lbl4=ut.create_label(root,170,25,text='Car Manufacturer',font=("Inter",16))
    lbl4.pack()
    lbl4.place(x =60, y =215)

    fram3,text3 = ut.create_entry(root,width=365,height=35)
    fram3,text3.pack()
    fram3.place(x =60, y =240)

    lbl5 = ut.create_label(root,60,25,text='Price',font=("Inter",16))
    lbl5.pack()
    lbl5.place(x =830, y =215)

    fram4,text4 = ut.create_entry(root,width=356,height=35)
    fram4,text4.pack()
    fram4.place(x =830, y =240)

    lbl6 = ut.create_label(root,170,25,text='Engine Capacity',font=("Inter",16))
    lbl6.pack()
    lbl6.place(x =60, y =335)

    fram5,text5 = ut.create_entry(root,width=365,height=35)
    fram5,text5.pack()
    fram5.place(x =60, y =360)

    lbl7 = ut.create_label(root,55,25,text='Year',font=("Inter",16))
    lbl7.pack()
    lbl7.place(x =830, y =335)

    fram6,text6 = ut.create_entry(root,width=356,height=35)
    fram6,text6.pack()
    fram6.place(x =830, y =360)

    lbl8 = ut.create_label(root,120,25,text='Description',font=("Inter",16))
    lbl8.pack()
    lbl8.place(x =60, y =460)

    fram7,text7 = ut.create_entry(root,width=356,height=130)
    fram7,text7.pack()
    fram7.place(x =60, y =485)

    fram , btn_upload = ut.create_button(root,170,40,color = 'red',text='Upload Photo',font=("Inter",16))
    fram , btn_upload.pack()
    fram.place(x =830, y =460)

    lbl9 = ut.create_label(root,100,25,text='Photo.jpg',font=("Inter",12))
    lbl9.pack()
    lbl9.place(x=1000, y =470)



    rbtn_var =StringVar()
    rbtn_var.set('For Sale')

    rbtn1 = Radiobutton(root,text='For Sale',value='For Sale',variable=rbtn_var)
    rbtn2 = Radiobutton(root,text='For Rent',value='For Rent',variable=rbtn_var)

    rbtn1.pack()
    rbtn1.place(x =830, y =530)
    rbtn2.pack()
    rbtn2.place(x=1000, y =530)

    fram1, btn_confirm = ut.create_button(root, 130, 40, color='red', text='Confirm', font=("Inter", 14))
    fram1, btn_confirm.pack()
    fram1.place(x=800, y=600)

    fram2, btn_back = ut.create_button(root, 130, 40, color='red', text='Back', font=("Inter", 14))
    fram2, btn_back.pack()
    fram2.place(x=950, y=600)

    fram3, btn_quit = ut.create_button(root, 130, 40, color='grey', text='Quit', font=("Inter", 14))
    fram3, btn_quit.pack()
    fram3.place(x=1100, y=600)

    root.mainloop()