from tkinter import *
from tkinter import ttk
import math
from PIL import ImageTk, Image

import DbConnection as dbc
import Util as ut
import User as user
import Cars as cars
import os


class CarGrid(Frame):
    def __init__(self, parent, controller, cars_arr):
        Frame.__init__(self, parent)
        self.pages = []
        self.curr_page = 0
        self.cars_photos = []
        self.cars_frames = []
        self.config(width=1216, height=500, bg="#FFFFFF")
        self.tkraise()
        self.grid_propagate(False)
        self.pack_propagate(False)
        # Next and previous buttons
        self.buttons = Frame(self, bg="#FFFFFF")
        self.buttons.grid(row=2, column=0)
        self.next_frame, self.next_btn = ut.create_button(self.buttons, 35, 40, "red", ">")
        self.prev_frame, self.prev_btn = ut.create_button(self.buttons, 35, 40, "red", "<")
        self.next_frame.pack(side=RIGHT, padx=5)
        self.prev_frame.pack(side=LEFT, padx=5)

        self.curr_page = 0
        self.next_btn.config(command=self.next_page)
        self.prev_btn.config(command=self.prev_page)
        self.prev_btn.config(state=DISABLED)
        # Determining the number of pages
        if len(cars_arr) == 0:
            self.number_of_pages = 1
        else:
            self.number_of_pages = math.ceil(len(cars_arr) / 3)
        if self.number_of_pages == 1:
            self.next_btn.config(state=DISABLED)
            self.prev_btn.config(state=DISABLED)
        # Creating the pages
        for i in range(0, self.number_of_pages):
            self.pages.append(Frame(self, bg="#FFFFFF", width=1216, height=463))
            self.pages[i].grid_propagate(False)
            self.pages[i].grid(row=0, column=0)
        # Saving photos for the cars
        for car in cars_arr:
            photo = Image.open(car.photo_path)
            photo = photo.resize((247, 143), Image.LANCZOS)
            self.cars_photos.append(ImageTk.PhotoImage(photo))
        # Creating the Labels and Remove Buttons
        counter = 0
        pg_num = 0
        photo_counter = 0
        for car in cars_arr:
            if counter == 3:
                pg_num += 1
                counter = 0

            frame = Frame(self.pages[pg_num], bg="#FFFFFF", width=1216, height=143)
            frame.pack_propagate(False)
            frame.grid_propagate(False)

            car_name = car.manu + " " + car.model + " " + str(car.year)

            car_label = Label(frame,
                              image=self.cars_photos[photo_counter],
                              bg="#FFFFFF",
                              font=("Helvetica", 14, "bold"),
                              text=car_name,
                              compound=LEFT,
                              padx=20)

            delete_frame, btn_delet = ut.create_button(frame, 117, 40, "red", "Delete")
            car_label.place(x=0, y=0)
            delete_frame.place(x=1078, y=52)

            self.cars_frames.append(frame)
            btn_delet.config(
                command=lambda f=self.cars_frames[photo_counter]: self.delete_car(f, car))

            self.cars_frames[photo_counter].grid(row=counter, pady=10)

            photo_counter += 1
            counter += 1
        self.pages[0].tkraise()

    def delete_car(self, f, car):
        f.destroy()
        db = dbc.connect_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM cars WHERE car_id = %s", (car.id,))
        db.commit()
        db.close()

    def on_enter(self, event):
        lbl = event.widget
        lbl.config(font=("Helvetica", 12, "underline", "bold"), fg="#EC221F")

    def on_leave(self, event):
        lbl = event.widget
        lbl.config(font=("Helvetica", 12, "bold"), fg="black")

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
