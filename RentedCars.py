from tkinter import *
from tkinter import ttk

from PIL import ImageTk
from PIL import Image

import DbConnection as dbc
import User
import Util as ut
import User as user
import Cars_For_Rent as car
import CarGrid2 as cg
import os as os
import datetime


class MainPage(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.config(bg="#FFFFFF", width=1280, height=720)
        self.pack_propagate(False)
        self.grid_propagate(False)
        # Tabs
        self.lbl1 = ut.create_label(self, width=274, height=17, text="Rented Cars", font=("Helvetica", 17))
        self.lbl1.place(x=32, y=30)

        # Frames
        self.parent_frame = Frame(self, bg="#FFFFFF", width=1280, height=600)
        self.parent_frame.grid_propagate(False)
        db = dbc.connect_db()
        self.cars_for_rent = []

        rent_cursor = db.cursor()
        rent_cursor.execute("SELECT"
                            " cars.car_id,"
                            " cars.owner_id,"
                            " model,"
                            " manu,"
                            " manu_year,"
                            " engine_capacity,"
                            " horsepower,"
                            " top_speed,"
                            " cars.price,"
                            " photo,"
                            " car_description,"
                            " type,"
                            " state,"
                            " rental_date,"
                            " return_date"
                            " FROM RENTALS "
                            " JOIN CARS ON cars.car_id = rentals.car_id "
                            " WHERE type = 'rent'"
                            " AND Rentals.renter_id = %s"
                            , (user.current_user.id,))
        rent_results = rent_cursor.fetchall()
        db.close()
        for result in rent_results:
            self.cars_for_rent.append(
                car.Cars(ID=result[0],
                         owner_id=result[1],
                         model=result[2],
                         manu=result[3],
                         year=result[4],
                         engine_capacity=result[5],
                         horsepower=result[6],
                         top_speed=result[7],
                         price=result[8],
                         photo_path=os.path.normcase(result[9]),
                         description=result[10],
                         op_type=result[11],
                         state=result[12],
                         rental_date=result[13],
                         return_date=result[14]
                         ))

        self.for_rent_frame = cg.CarGrid(self.parent_frame, controller, self.cars_for_rent)
        self.for_rent_frame.grid_propagate(False)
        self.for_rent_frame.grid(row=0, column=0)

        self.parent_frame.place(x=30, y=100)

        self.back_btn_frame, self.back_btn = ut.create_button(self, 121, 40, "red", "Back")
        self.quit_btn_frame, self.quit_btn = ut.create_button(self, 121, 40, "grey", "Quit")

        self.back_btn_frame.place(x=980, y=660)
        self.quit_btn_frame.place(x=1127, y=660)
        self.quit_btn.config(command=lambda: controller.destroy())
        self.back_btn.config(command=lambda: controller.show_frame("main_page"))
