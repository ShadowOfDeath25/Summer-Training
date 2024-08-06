from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import DbConnection as dbc
import User
import Util as ut
import User as user
import Cars as cars
import CarGrid1 as cg
import os


class MainPage(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.config(bg="#FFFFFF", width=1280, height=720)
        self.pack_propagate(False)
        self.grid_propagate(False)

        self.for_sale_normal = PhotoImage(file="photos/for_sale_nrml.png")
        self.for_sale_clicked = PhotoImage(file="photos/for_sale_clicked.png")
        self.for_rent_normal = PhotoImage(file="photos/for_rent_nrml.png")
        self.for_rent_clicked = PhotoImage(file="photos/for_rent_clicked.png")
        self.for_rent_lbl = Label(self, image=self.for_rent_clicked, bg="#FFFFFF", cursor="hand2")
        self.for_sale_lbl = Label(self, image=self.for_sale_normal, bg="#FFFFFF", cursor="hand2")
        self.for_rent_lbl.place(x=648, y=24)
        self.for_sale_lbl.place(x=531, y=24)
        self.for_rent_lbl.bind("<Button-1>", self.for_rent)
        self.for_sale_lbl.bind("<Button-1>", self.for_sale)
        self.add_photo = PhotoImage(file='photos/add.png')
        self.lbl = Label(self, image=self.add_photo, background='white', text="Add Car",
                         font=("Helvetica", 12), compound=RIGHT, padx=10, cursor="hand2")
        self.lbl.place(x=1157, y=22)
        self.lbl.bind("<Button-1>", lambda event, control=controller: self.add_car(event, control))

        self.parent_frame = Frame(self, bg="#FFFFFF", width=1280, height=600)
        self.parent_frame.grid_propagate(False)
        db = dbc.connect_db()
        self.cars_for_rent = []
        self.cars_for_sale = []
        rent_cursor = db.cursor()
        rent_cursor.execute(
            "SELECT car_id,"
            " owner_id,"
            " model,"
            " manu,"
            " manu_year,"
            " engine_capacity,"
            " horsepower,"
            " top_speed,"
            " price,"
            " photo,"
            " car_description,"
            " type,"
            " state,"
            " phone_number"
            " FROM cars"
            " JOIN users ON cars.owner_ID = users.ID"
            " WHERE type = 'rent'"
            " AND state = 'available'"
            " AND cars.owner_ID = %s",
            (User.current_user.id,))
        rent_results = rent_cursor.fetchall()
        sale_cursor = db.cursor()
        sale_cursor.execute("SELECT car_id,"
                            " owner_id,"
                            " model,"
                            " manu,"
                            " manu_year,"
                            " engine_capacity,"
                            " horsepower,"
                            " top_speed,"
                            " price,"
                            " photo,"
                            " car_description,"
                            " type,"
                            " state,"
                            " phone_number"
                            " FROM cars"
                            " JOIN users ON cars.owner_ID = users.ID"
                            " WHERE type = 'sale'"
                            " AND state = 'available' "
                            " AND cars.owner_id = %s",
                            (User.current_user.id,))
        sale_results = sale_cursor.fetchall()
        db.close()

        for result in rent_results:
            self.cars_for_rent.append(cars.Cars(
                ID=result[0], owner_id=result[1], model=result[2], manu=result[3], year=result[4],
                engine_capacity=result[5], horsepower=result[6], top_speed=result[7], price=result[8],
                photo_path=os.path.normcase(result[9]), description=result[10], op_type=result[11],
                state=result[12], owner_phone=result[13]
            ))
        for result in sale_results:
            self.cars_for_sale.append(cars.Cars(
                ID=result[0], owner_id=result[1], model=result[2], manu=result[3], year=result[4],
                engine_capacity=result[5], horsepower=result[6], top_speed=result[7], price=result[8],
                photo_path=os.path.normcase(result[9]), description=result[10], op_type=result[11],
                state=result[12], owner_phone=result[13]
            ))

        self.for_sale_frame = cg.CarGrid(self.parent_frame, controller, self.cars_for_sale)
        self.for_rent_frame = cg.CarGrid(self.parent_frame, controller, self.cars_for_rent)
        self.for_sale_frame.grid_propagate(False)
        self.for_rent_frame.grid_propagate(False)
        self.for_sale_frame.grid(row=0, column=0)
        self.for_rent_frame.grid(row=0, column=0)
        self.for_sale_frame.tkraise()
        self.curr_view = "for_sale"
        self.parent_frame.place(x=0, y=100)

        self.back_btn_frame, self.back_btn = ut.create_button(self, 121, 40, "red", "Back")
        self.quit_btn_frame, self.quit_btn = ut.create_button(self, 121, 40, "grey", "Quit")
        self.back_btn_frame.place(x=980, y=660)
        self.quit_btn_frame.place(x=1127, y=660)
        self.quit_btn.config(command=lambda: controller.destroy())
        self.back_btn.config(command=lambda: controller.show_frame("main_page"))

    def for_sale(self, event):
        self.for_sale_lbl.config(image=self.for_sale_normal)
        self.for_rent_lbl.config(image=self.for_rent_clicked)
        self.for_sale_frame.tkraise()
        self.curr_view = "for_sale"

    def for_rent(self, event):
        self.for_rent_lbl.config(image=self.for_rent_normal)
        self.for_sale_lbl.config(image=self.for_sale_clicked)
        self.for_rent_frame.tkraise()
        self.curr_view = "for_rent"

    def add_car(self, event, control):
        control.show_frame("add_car")
