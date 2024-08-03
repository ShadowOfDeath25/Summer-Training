from tkinter import *
from tkinter import ttk
import math
from PIL import ImageTk
from PIL import Image

import DbConnection as dbc
import Util as ut
import User as user
import Cars as cars


class CarGrid(Frame):
    def __init__(self, parent, controller, cars_arr):
        Frame.__init__(self, parent)
        self.pages = []
        self.curr_page=0
        self.cars_photos = []
        self.cars_labels = []
        self.config(width=1140,
                    height=423,
                    bg="#FFFFFF")
        self.pack_propagate(False)
        self.grid_propagate(False)
        # Determining the number of pages
        if len(cars_arr) == 0:
            self.number_of_pages = 1
        else:
            self.number_of_pages = math.ceil(len(cars_arr) / 8)
        #   Creating the pages
        for i in range(0, self.number_of_pages):
            self.pages.append(Frame(self, bg="#FFFFFF", width=1140, height=500))
            self.pages[i].grid_propagate(False)
            self.pages[i].grid(row=0, column=0)
        # Saving photos for the cars
        for car in cars_arr:
            photo = Image.open(car.photo_path)
            photo = photo.resize((247, 143), Image.LANCZOS)
            self.cars_photos.append(ImageTk.PhotoImage(photo))
        # Creating the Labels
        counter = 0
        pg_num = 0
        photo_counter = 0
        for car in cars_arr:
            if counter == 9:
                pg_num += 1
                counter = 0
            car_name = car.manu + " " + car.model + " " + str(car.year)
            lbl = Label(self.pages[pg_num],
                        text=car_name,
                        font=("Helvetica", 12),
                        image=self.cars_photos[photo_counter],
                        bg="#FFFFFF",
                        compound=TOP,
                        cursor="hand2")
            lbl.bind("<Button-1>", controller.show_frame("car_" + car.op_type.lower() + "_view"))
            self.cars_labels.append(lbl)

            photo_counter += 1
            counter += 1

        # Placing the labels
        row = 0
        col = 0
        counter = 0
        for label in self.cars_labels:
            if counter == 9:
                row = 0
                col = 0
            if col == 4:
                col = 0
                row += 1
            label.grid(row=row, column=col, padx=20, pady=30)
            label.bind("<Enter>", self.on_enter)
            label.bind("<Leave>", self.on_leave)

            col += 1
            counter += 1

    def on_enter(self, event):
        lbl = event.widget
        lbl.config(font=("Helvetica", 12, "underline", "bold"), fg="#EC221F")

    def on_leave(self, event):
        lbl = event.widget
        lbl.config(font=("Helvetica", 12, "normal"), fg="black")


