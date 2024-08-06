from tkinter import *
from tkinter import ttk

from PIL import ImageTk
from PIL import Image

import DbConnection as dbc
import User
import Util as ut
import User as user
import Cars as cars
import CarGrid as cg
import os as os


class MainPage(Frame):
    def __init__(self, parent, controller):

        super().__init__(parent)
        self.config(bg="#FFFFFF", width=1280, height=720)
        self.pack_propagate(False)
        self.grid_propagate(False)
        # Tabs
        self.for_sale_normal = PhotoImage(file="photos/for_sale_nrml.png")
        self.for_sale_clicked = PhotoImage(file="photos/for_sale_clicked.png")
        self.for_rent_normal = PhotoImage(file="photos/for_rent_nrml.png")
        self.for_rent_clicked = PhotoImage(file="photos/for_rent_clicked.png")
        self.for_rent_lbl = Label(self, image=self.for_rent_clicked, bg="#FFFFFF", cursor="hand2")
        self.for_sale_lbl = Label(self, image=self.for_sale_normal, bg="#FFFFFF", cursor="hand2")
        self.for_rent_lbl.place(x=647, y=66)
        self.for_sale_lbl.place(x=530, y=66)
        self.for_rent_lbl.bind("<Button-1>", self.for_rent)
        self.for_sale_lbl.bind("<Button-1>", self.for_sale)

        # Frames
        self.parent_frame = Frame(self, bg="#FFFFFF", width=1140, height=473)
        self.parent_frame.grid_propagate(False)
        db = dbc.connect_db()
        self.cars_for_rent = []
        self.cars_for_sale = []
        rent_cursor = db.cursor()
        rent_cursor.execute("SELECT"
                            " car_id,"
                            "owner_id,"
                            "model,"
                            "manu,"
                            "manu_year,"
                            "engine_capacity,"
                            "horsepower,"
                            "top_speed,"
                            "price,"
                            "photo,"
                            "car_description,"
                            "type,"
                            "state,"
                            "phone_number"
                            " FROM cars "
                            "JOIN users ON cars.owner_ID =users.ID "
                            " WHERE type = 'rent' AND state = 'available' "
                            )
        rent_results = rent_cursor.fetchall()
        sale_cursor = db.cursor()
        sale_cursor.execute("SELECT"
                            " car_id,"
                            "owner_id,"
                            "model,"
                            "manu,"
                            "manu_year,"
                            "engine_capacity,"
                            "horsepower,"
                            "top_speed,"
                            "price,"
                            "photo,"
                            "car_description,"
                            "type,"
                            "state,"
                            "phone_number"
                            " FROM cars "
                            "JOIN users ON cars.owner_ID =users.ID "
                            " WHERE type = 'sale' AND state = 'available' ")
        sale_results = sale_cursor.fetchall()
        db.close()
        for result in rent_results:
            self.cars_for_rent.append(
                cars.Cars(ID=result[0],
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
                          owner_phone=result[13]
                          ))
        for result in sale_results:
            self.cars_for_sale.append(
                cars.Cars(ID=result[0],
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
                          owner_phone=result[13]
                          ))

        self.for_sale_frame = cg.CarGrid(self.parent_frame, controller, self.cars_for_sale)
        self.for_rent_frame = cg.CarGrid(self.parent_frame, controller, self.cars_for_rent)
        self.for_sale_frame.grid_propagate(False)
        self.for_rent_frame.grid_propagate(False)
        self.for_sale_frame.grid(row=0, column=0)
        self.for_rent_frame.grid(row=0, column=0)
        self.for_sale_frame.tkraise()
        self.curr_view = "for_sale"
        self.parent_frame.place(x=60, y=123)

        # Bottom buttons
        self.listed_frame, self.listed_btn = ut.create_button(self, 135, 40, "red", "Listed Cars")
        self.rented_frame, self.rented_btn = ut.create_button(self, 135, 40, "red", "Rented Cars")
        self.back_btn_frame, self.back_btn = ut.create_button(self, 103, 40, "red", "Back")
        self.quit_btn_frame, self.quit_btn = ut.create_button(self, 103, 40, "grey", "Quit")
        self.listed_frame.place(x=743, y=667)
        self.rented_frame.place(x=896, y=667)
        self.back_btn_frame.place(x=1049, y=667)
        self.quit_btn_frame.place(x=1170, y=667)
        self.quit_btn.config(command=lambda: controller.destroy())
        self.back_btn.config(command=lambda: controller.show_frame("Login"))
        self.listed_btn.config(command=lambda: controller.show_frame("listed_cars"))
        self.rented_btn.config(command=lambda: controller.show_frame("rented_cars"))

        # Username label
        self.username_lbl_frame = Frame(self, width=234, height=64, bg="#FFFFFF")
        self.username_lbl_frame.pack_propagate(False)
        self.username_photo = PhotoImage(file="Photos/profile-user.png")
        self.username_label = Label(self.username_lbl_frame, text=user.current_user.full_name,
                                    font=("Helvetica ", 10, "bold"),
                                    bg="#FFFFFF", image=self.username_photo,compound=RIGHT,padx=10)
        self.username_label.pack(fill=BOTH, expand=True)
        self.username_lbl_frame.place(x=1034, y=15)

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


