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
        self.curr_page = 0
        self.cars_photos = []
        self.cars_labels = []

        self.config(width=1140,
                    height=500,
                    bg="#FFFFFF")
        self.grid_propagate(False)
        self.pack_propagate(False)
        # Next and previous buttons
        self.buttons = Frame(self, bg="#FFFFFF")
        self.buttons.grid(row=2, column=0)
        self.next_frame, self.next_btn = ut.create_button(self.buttons, 35, 40, "red", ">")
        self.prev_frame, self.prev_btn = ut.create_button(self.buttons, 35, 40, "red", "<")
        self.next_frame.pack(side=RIGHT, padx=10)
        self.prev_frame.pack(side=LEFT, padx=10)

        self.curr_page = 0
        self.next_btn.config(command=self.next_page)
        self.prev_btn.config(command=self.prev_page)
        self.prev_btn.config(state=DISABLED)
        # Determining the number of pages
        if len(cars_arr) == 0:
            self.number_of_pages = 1
        else:
            self.number_of_pages = math.ceil(len(cars_arr) / 8)
        if self.number_of_pages == 1:
            self.next_btn.config(state=DISABLED)
            self.prev_btn.config(state=DISABLED)
        #   Creating the pages

        for i in range(0, self.number_of_pages):
            self.pages.append(Frame(self, bg="#FFFFFF", width=1140, height=423))
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
            if counter == 8:
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
            lbl.bind("<Button-1>", lambda event, cr=car, control=controller: self.show_car(event, cr, control))
            self.cars_labels.append(lbl)

            photo_counter += 1
            counter += 1
        self.pages[0].tkraise()

        # Placing the labels
        row = 0
        col = 0
        counter = 0
        for label in self.cars_labels:
            if counter == 8:
                row = 0
                col = 0
            if col == 4:
                col = 0
                row += 1
            label.grid(row=row, column=col, padx=20, pady=10)
            label.bind("<Enter>", self.on_enter)
            label.bind("<Leave>", self.on_leave)

            col += 1
            counter += 1

        print(len(self.pages))

    def on_enter(self, event):
        lbl = event.widget
        lbl.config(font=("Helvetica", 12, "underline", "bold"), fg="#EC221F")

    def on_leave(self, event):
        lbl = event.widget
        lbl.config(font=("Helvetica", 12, "normal"), fg="black")

    def next_page(self):
        if self.curr_page == len(self.pages) - 2:
            self.next_btn.config(state=DISABLED)
        self.curr_page += 1
        self.pages[self.curr_page].tkraise()
        if self.curr_page > 0:
            self.prev_btn.config(state=ACTIVE)

        self.next_btn.config(bg="#EC221F")
        self.prev_btn.config(bg="#EC221F")

    def prev_page(self):
        if self.curr_page == 1:
            self.prev_btn.config(state=DISABLED)
        if self.curr_page <= len(self.pages) - 1:
            self.next_btn.config(state=ACTIVE)
        self.next_btn.config(bg="#EC221F")
        self.prev_btn.config(bg="#EC221F")
        self.curr_page -= 1
        self.pages[self.curr_page].tkraise()

    def show_car(self, event, cr, control):
        control.show_frame("car_" + cr.op_type.lower() + "_view", cr)
