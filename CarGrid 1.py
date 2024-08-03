from tkinter import *
from tkinter import ttk
import math
from PIL import ImageTk, Image

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
        self.config(width=1140, height=500, bg="#FFFFFF")
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
            self.number_of_pages = math.ceil(len(cars_arr) / 3)
        if self.number_of_pages == 1:
            self.next_btn.config(state=DISABLED)
            self.prev_btn.config(state=DISABLED)
        # Creating the pages
        for i in range(0, self.number_of_pages):
            self.pages.append(Frame(self, bg="#FFFFFF", width=1140, height=423))
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
            car_name = car.manu + " " + car.model + " " + str(car.year)
            photo_label = Label(self.pages[pg_num],
                        image=self.cars_photos[photo_counter],
                        bg="#FFFFFF",
                        cursor="hand2")
            photo_label.bind("<Button-1>", lambda e, car_view="car_" + car.op_type.lower() + "_view": controller.show_frame(car_view))

            name_label = Label(self.pages[pg_num],
                        text=car_name,
                        font=("Helvetica", 12),
                        bg="#FFFFFF",
                        cursor="hand2")
            name_label.bind("<Button-1>", lambda e, car_view="car_" + car.op_type.lower() + "_view": controller.show_frame(car_view))
            self.cars_labels.append((photo_label, name_label))

            # إنشاء زر المسح
            btn_delet = ut.create_button(self.pages[pg_num],
                                text="Delet",
                                width=117,
                                height=40,
                                command=lambda l=photo_label, n=name_label, b=btn_delet: self.delet_car(l, n, b))
            
            # وضع العناصر في الشبكة
            photo_label.grid(row=counter, column=0, padx=20, pady=10, sticky=W)  # وضع الصورة في عمود 0
            name_label.grid(row=counter, column=1, padx=(0, 10), pady=10, sticky=W)  # وضع التسمية في عمود 1
            btn_delet.grid(row=counter, column=2, padx=(0, 573), pady=10, sticky=W)  # وضع الزر في عمود 2 مع تحديد المسافة

            photo_counter += 1
            counter += 1
        self.pages[0].tkraise()

    def delet_car(self, photo_label, name_label, car_button):
        photo_label.destroy()
        name_label.destroy()
        car_button.destroy()

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