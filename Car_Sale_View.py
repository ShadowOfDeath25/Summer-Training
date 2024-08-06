from tkinter import *
from tkinter import messagebox

from PIL import Image, ImageTk
import mysql.connector
import DbConnection as db
import Util as ut
import Cars as cr
import bcrypt
import os


class Car_Sale_View(Frame):

    def __init__(self, parent, controller, car=None):
        super().__init__(parent)

        self.config(width=1280, height=720, bg="#FFFFFF")
        self.pack_propagate(False)
        self.grid_propagate(False)
        self.car = car
        self.back_fr, self.back_btn = ut.create_button(self, 105, 40, "red", text="Back")
        self.quit_fr, self.quit_btn = ut.create_button(self, 105, 40, "grey", text="Quit")
        self.description_lbl = Label(self, text="Description:", font=("Helvetica", 14, 'bold'), bg="#FFFFFF")
        self.car_fr, self.car_img = ut.create_image(self, 590, 320, os.path.normcase(self.car.photo_path))
        self.car_lbl = Label(self, image=self.car_img)
        self.engine_fr, self.engine_img = ut.create_image(self, 64, 64, 'photos/engine.png')
        self.horsepower_fr, self.horsepower_img = ut.create_image(self, 64, 64, 'photos/horsepower.png')
        self.speed_fr, self.speed_img = ut.create_image(self, 64, 64, 'photos/speed.png')
        self.calendar_fr, self.calendar_img = ut.create_image(self, 64, 64, 'photos/calendar.png')
        self.dollar_fr, self.dollar_img = ut.create_image(self, 64, 64, 'photos/dollar.png.')
        self.call_fr, self.call_img = ut.create_image(self, 64, 64, 'photos/call.png')
        self.engine_lbl = Label(self, font=("Helvetica", 18), text=str(self.car.engine_capacity) + " CC",
                                image=self.engine_img, compound=LEFT, bg="#FFFFFF", padx=10)
        self.speed_lbl = Label(self, font=("Helvetica", 18), text=str(self.car.top_speed) + " KM/H",
                               image=self.speed_img, compound=LEFT, bg="#FFFFFF", padx=10)
        self.power_lbl = Label(self, font=("Helvetica", 18), text=str(self.car.horsepower) + " HP",
                               image=self.horsepower_img, compound=LEFT, bg="#FFFFFF", padx=10)
        self.price_lbl = Label(self, font=("Helvetica", 32), text=str(self.car.price) + " L.E",
                               image=self.dollar_img, compound=LEFT, bg="#FFFFFF", padx=10)
        self.year_lbl = Label(self, font=("Helvetica", 18), text=str(self.car.year), image=self.calendar_img,
                              compound=LEFT, bg="#FFFFFF", padx=10)
        self.phone_lbl = Label(self, font=("Helvetica", 18), text=self.car.owner_phone, image=self.call_img,
                               compound=LEFT, bg="#FFFFFF", padx=10)
        self.car_name_lbl = ut.create_label(self, 669, 50,
                                            font=("Helvetica)", 32, "bold"),
                                            text=self.car.manu + " " + car.model + " " + str(car.year))
        # btn

        self.back_fr.place(x=990, y=650)
        self.back_btn.config(command=lambda: controller.show_frame("main_page"))
        self.quit_fr.place(x=1120, y=650)
        self.quit_btn.config(command=lambda: controller.show_frame("Login"))
        # img

        # lbl
        self.car_lbl.place(x=20, y=35)
        self.description_lbl.place(x=20, y=379)
        self.speed_lbl.place(x=726, y=205)
        self.price_lbl.place(x=814, y=302)
        self.year_lbl.place(x=1038, y=205)
        self.phone_lbl.place(x=20, y=635)
        self.engine_lbl.place(x=726, y=108)
        self.power_lbl.place(x=1038, y=108)
        self.car_name_lbl.place(x=611, y=35)
        self.frame = Frame(self, width=1250, height=160, bg="#FFFFFF")
        self.entry = Text(self.frame, bg="#FFFFFF", font=("Helvetica", 12), borderwidth=0, cursor="arrow")
        self.entry.insert(END, self.car.description)
        self.entry.config(state=DISABLED)
        self.frame.pack_propagate(False)
        self.entry.pack(fill=BOTH, expand=True, padx=10, pady=10)
        self.frame.place(x=10, y=420)
