from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from PIL import Image, ImageTk
import mysql.connector
import DbConnection as db
import Util as ut
import Cars as cr
import bcrypt


class Car_Rental_View(Frame):

    def __init__(self, parent, controller, car=None):
        super().__init__(parent)
        self.rent_fr, self.rent_btn = ut.create_button(self, 105, 40, "red", text="Rent")
        self.back_fr, self.back_btn = ut.create_button(self, 105, 40, "red", text="Back")
        self.quit_fr, self.quit_btn = ut.create_button(self, 105, 40, "grey", text="Quit")
        self.description_lbl = ut.create_label(self, 149, 25, "Description :", ("Helvetica", 12, 'bold'))
        self.car_fr, self.car_img = ut.create_image(self, 590, 320, 'photos/01.jpg')
        self.engine_fr, self.engine_img = ut.create_image(self, 64, 64, 'photos/engine.png')
        self.horsepower_fr, self.horsepower_img = ut.create_image(self, 64, 64, 'photos/horsepower.png')
        self.speed_fr, self.speed_img = ut.create_image(self, 64, 64, 'photos/speed.png')
        self.calendar_fr, self.calendar_img = ut.create_image(self, 64, 64, 'photos/calendar.png')
        self.dollar_fr, self.dollar_img = ut.create_image(self, 64, 64, 'photos/dollar.png.')
        self.call_fr, self.call_img = ut.create_image(self, 64, 64, 'photos/call.png')
        self.engine_lbl = ut.create_label(self, 130, 50, str(car.engine_capacity) + ' CC')
        self.speed_lbl = ut.create_label(self, 130, 50, str(car.top_speed) + ' Km/h')
        self.power_lbl = ut.create_label(self, 130, 50, str(car.horsepower) + ' HP')
        self.price_lbl = ut.create_label(self, 130, 50, str(car.price) + ' L.E/Day')
        self.year_lbl = ut.create_label(self, 130, 50, str(car.year))
        self.phone_lbl = ut.create_label(self, 130, 50, car.owner_phone)
        self.car_name_lbl = ut.create_label(self, 320, 40, car.manu + " ", car.model + " " + str(car.year))
        self.dtxt_lbl = ut.create_label(self, 1110, 160, car.description)
        # btn
        self.rent_fr.place(x=860, y=650)
        self.rent_btn.config(command=lambda: controller.show_frame("date_picker"))
        self.back_fr.place(x=990, y=650)
        self.back_btn.config(command=lambda: controller.show_frame("main_page"))
        self.quit_fr.place(x=1120, y=650)
        self.quit_btn.config(command=lambda: controller.show_frame("quit"))
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
