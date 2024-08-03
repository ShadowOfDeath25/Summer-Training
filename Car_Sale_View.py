from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from PIL import Image, ImageTk
import mysql.connector
import DbConnection as db
import Util as ut
import Cars as cr
import bcrypt
import App

class Car_Sale_View(Frame):
    root = Tk()
    sale_fr, sale_btn = ut.create_button(root, 105, 40, "red", text="Sale")
    back_fr, back_btn = ut.create_button(root, 105, 40, "red", text="Back")
    quit_fr, quit_btn = ut.create_button(root, 105, 40, "grey", text="Quit")
    description_lbl = ut.create_label(root, 149, 25, "Description :", ("Helvetica", 12, 'bold'))
    car_fr, car_img = ut.create_image(root, 590, 320, 'photos/01.jpg')
    engine_fr, engine_img = ut.create_image(root, 64, 64, 'photos/engine.png')
    horsepower_fr, horsepower_img = ut.create_image(root, 64, 64, 'photos/horsepower.png')
    speed_fr, speed_img = ut.create_image(root, 64, 64, 'photos/speed.png')
    calendar_fr, calendar_img = ut.create_image(root, 64, 64, 'photos/calendar.png')
    dollar_fr, dollar_img = ut.create_image(root, 64, 64, 'photos/dollar.png.')
    call_fr, call_img = ut.create_image(root, 64, 64, 'photos/call.png')
    engine_lbl = ut.create_label(root, 130, 50, str(cr.Cars.engine_capacity) + ' CC')
    speed_lbl = ut.create_label(root, 130, 50, str(cr.Cars.top_speed) + ' Km/h')
    power_lbl = ut.create_label(root, 130, 50, str(cr.Cars.horsepower) + ' HP')
    price_lbl = ut.create_label(root, 130, 50, str(cr.Cars.price) + ' L.E')
    year_lbl = ut.create_label(root, 130, 50, str(cr.Cars.year))
    phone_lbl = ut.create_label(root, 130, 50, "01205764096")
    car_name_lbl = ut.create_label(root, 320, 40, "Car Name")
    dtxt_lbl = ut.create_label(root, 1110, 160, cr.Cars.description)

    def __init__(self,parent, controller):
        Frame.__init__(self,parent)
        self.root.title("Car Sale View")
        window_width = 1280
        window_height = 720
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)
        self.root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        self.root.config(bg="#FFFFFF")
        self.root.resizable(False, False)
        # btn
        self.sale_fr.place(x=860, y=650)
        self.sale_btn.config(command=lambda: self.sale(controller))
        self.back_fr.place(x=990, y=650)
        self.back_btn.config(command=lambda: self.back(controller))
        self.quit_fr.place(x=1120, y=650)
        self.quit_btn.config(command=lambda: self.quit(controller))
        # img
        self.car_fr.pack()
        self.car_img.place(x=20, y=35)
        self.call_fr.pack()
        self.call_img.place(x=20, y=625)
        self.dollar_fr.pack()
        self.dollar_img.place(x=800, y=302)
        self.calendar_fr.pack()
        self.calendar_img.place(x=981, y=205)
        self.engine_fr.pack()
        self.engine_img.place(x=719, y=108)
        self.horsepower_fr.pack()
        self.horsepower_img.place(x=981, y=108)
        self.speed_fr.pack()
        self.speed_img.place(x=719, y=205)
        # lbl
        self.description_lbl.place(x=20, y=379)
        self.speed_lbl.place(x=791, y=223)
        self.price_lbl.place(x=890, y=315)
        self.year_lbl.place(x=1160, y=220)
        self.phone_lbl.place(x=100, y=635)
        self.engine_lbl.place(x=792, y=127)
        self.power_lbl.place(x=1061, y=127)
        self.car_name_lbl.place(x=760, y=35)
        self.dtxt_lbl.place(x=20, y=420)

        self.root.mainloop()

    def quit(self, controller):
        controller.show_frame("Login")
    def back(self, controller):
        controller.show_frame("MainPage")
    def sale(self, controller):
        curr_db = db.connect_db()
        cursor = curr_db.cursor()
        cursor.execute("update cars set state='unavailable' where car_id=%s", cr.Cars.id)
        curr_db.commit()
        controller.show_frame("MainPage")

win = Tk()
frame = Frame(win)
Car_Sale_View(frame,win)