import Util as ut
from tkinter import *
from tkcalendar import Calendar
import mysql.connector
import DbConnection as db
from datetime import datetime
import User as u
import uuid


class Date_Picker(Frame):
    def __init__(self, parent, controller, car=None):
        super().__init__(parent)
        self.config(width=540, height=400, bg="#FFFFFF")
        self.pack_propagate(False)
        self.grid_propagate(False)
        self.car = car
        self.frame = Frame(self)
        self.frame.grid(row=0, column=0, sticky=(W, E, N, S))
        self.frame.config(bg="#FFFFFF")
        # Calendar widgets
        self.start_cal = Calendar(self.frame, selectmode='day', year=2024, month=8, day=1, date_pattern="d/m/Y")
        self.start_cal.grid(row=0, column=0, padx=10, pady=10)
        self.end_cal = Calendar(self.frame, selectmode='day', year=2024, month=8, day=1, date_pattern="d/m/Y")
        self.end_cal.grid(row=0, column=1, padx=10, pady=10)
        # Labels
        self.start_lbl = ut.create_label(self, 90, 50, 'Start Date : \n\n' + self.start_cal.get_date())
        self.end_lbl = ut.create_label(self, 90, 50, 'End Date : \n\n' + self.end_cal.get_date())
        self.start_lbl.place(x=80, y=220)
        self.end_lbl.place(x=350, y=220)
        # Calculate price
        self.date_format = "%d/%m/%Y"
        self.delta = datetime.strptime(self.end_cal.get_date(), self.date_format) - datetime.strptime(
            self.start_cal.get_date(), self.date_format)
        self.price = self.delta.days * 50
        # Price label
        self.price_lbl = ut.create_label(self, 90, 50,
                                         'Days : ' + str(self.delta.days) + '\n\nPrice : ' + str(self.price))
        self.price_lbl.place(x=220, y=280)
        #btn
        self.set_fr, self.set_btn = ut.create_button(self, 105, 40, 'red', text='Set Dates')
        self.set_fr.place(x=220, y=220)
        self.set_btn.config(command=self.get_dates)
        self.rent_fr, self.rent_btn = ut.create_button(self, 105, 40, 'red', text='Rent')
        self.rent_fr.place(x=220, y=350)
        self.rent_btn.config(command=self.set_data(controller, car))

    def get_dates(self):
        start_date = self.start_cal.get_date()
        end_date = self.end_cal.get_date()
        start_lbl = ut.create_label(self, 90, 50, 'Start Date : \n\n' + start_date)
        end_lbl = ut.create_label(self, 90, 50, 'End Date : \n\n' + end_date)
        start_lbl.place(x=80, y=220)
        end_lbl.place(x=350, y=220)
        # Calculate price
        date_format = "%d/%m/%Y"
        delta = datetime.strptime(end_date, date_format) - datetime.strptime(start_date, date_format)
        price = delta.days * 50
        # Price label
        price_lbl = ut.create_label(self, 90, 50, 'Days : ' + str(delta.days) + '\n\nPrice : ' + str(price))
        price_lbl.place(x=220, y=280)

    def set_data(self, controller, car):
        #curr_db = db.connect_db()
        #cursor = curr_db.cursor()
        start_date = self.start_cal.get_date()
        end_date = self.end_cal.get_date()
        date_format = "%d/%m/%Y"
        delta = datetime.strptime(end_date, date_format) - datetime.strptime(start_date, date_format)
        price = delta.days * car.price
        #rental_id = str(uuid.uuid4())
        #values = (rental_id, car.id, car.owner_id, u.current_user.id, start_date, end_date, price)
        #cursor.execute(
        #    "INSERT INTO rentals (rental_id, car_id, owner_id,renter_id, rental_date, return_date, price) VALUES (%s,%s,%s,%s,%s,%s,%s)",
        #    values)
        #cursor.execute("update cars set state='unavailable' where car_id=%s", car.id)
        #curr_db.commit()
        #curr_db.close()
        controller.show_frame("main_page")