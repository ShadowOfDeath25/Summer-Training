import Util as ut
from tkinter import *
from tkcalendar import Calendar
import mysql.connector
import DbConnection as db
from datetime import datetime
import Cars as cr
import uuid
def get_dates():
    start_date = start_cal.get_date()
    end_date = end_cal.get_date()
    start_lbl = ut.create_label(root, 90, 50, 'Start Date : \n\n' + start_date)
    end_lbl = ut.create_label(root, 90, 50, 'End Date : \n\n' + end_date)
    start_lbl.place(x=80, y=220)
    end_lbl.place(x=350, y=220)
    # Calculate price
    date_format = "%d/%m/%Y"
    delta = datetime.strptime(end_date, date_format) - datetime.strptime(start_date, date_format)
    price = delta.days * 50
    # Price label
    price_lbl = ut.create_label(root, 90, 50, 'Days : ' + str(delta.days) + '\n\nPrice : ' + str(price))
    price_lbl.place(x=220, y=280)

def set_data():
    curr_db = db.connect_db()
    cursor = curr_db.cursor()
    start_date = start_cal.get_date()
    end_date = end_cal.get_date()
    date_format = "%d/%m/%Y"
    delta = datetime.strptime(end_date, date_format) - datetime.strptime(start_date, date_format)
    price = delta.days * cr.Cars.price
    rental_id = str(uuid.uuid4())
    values=(rental_id, cr.Cars.id, cr.Cars.owner_id,start_date, end_date, price)
    cursor.execute(
        "INSERT INTO rentals (rental_id, car_id, owner_id, rental_date, return_date, price) VALUES (%s,%s,%s,%s,%s,%s)",
        values)
    cursor.execute("update cars set state='unavailable' where car_id=%s", cr.Cars.id)
    curr_db.commit()

root = Tk()
root.title("Date Picker")
window_width = 540
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.config(bg="#FFFFFF")
root.resizable(False, False)
frame = Frame(root)
frame.grid(row=0, column=0, sticky=(W, E, N, S))
frame.config(bg="#FFFFFF")
# Calendar widgets
start_cal = Calendar(frame, selectmode='day', year=2024, month=8, day=1, date_pattern="d/m/Y")
start_cal.grid(row=0, column=0, padx=10, pady=10)
end_cal = Calendar(frame, selectmode='day', year=2024, month=8, day=1, date_pattern="d/m/Y")
end_cal.grid(row=0, column=1, padx=10, pady=10)
# Button
rent_fr, rent_btn = ut.create_button(root, 105, 40, 'red', text='Set Dates')
rent_fr.place(x=220, y=220)
rent_btn.config(command=get_dates)
rent_fr, rent_btn = ut.create_button(root, 105, 40, 'red', text='Rent')
rent_fr.place(x=220, y=350)
rent_btn.config(command=set_data)
# Labels
start_lbl = ut.create_label(root, 90, 50, 'Start Date : \n\n' + start_cal.get_date())
end_lbl = ut.create_label(root, 90, 50, 'End Date : \n\n' + end_cal.get_date())
start_lbl.place(x=80, y=220)
end_lbl.place(x=350, y=220)
# Calculate price
date_format = "%d/%m/%Y"
delta = datetime.strptime(end_cal.get_date(), date_format) - datetime.strptime(start_cal.get_date(), date_format)
price = delta.days * 50
# Price label
price_lbl = ut.create_label(root, 90, 50, 'Days : ' + str(delta.days) + '\n\nPrice : ' + str(price))
price_lbl.place(x=220, y=280)

root.mainloop()
