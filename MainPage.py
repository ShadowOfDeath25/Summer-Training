from tkinter import *
from tkinter import ttk

from PIL import ImageTk
from PIL import Image

import DbConnection as dbc
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

        # Search Bar
        self.search_parent = Frame(self, width=617, height=40, bg="#D9D9D9")
        self.search_parent.grid_propagate(False)
        self.search_frame, self.search_box = ut.create_entry(self.search_parent, 617 - 32, 40)
        self.search_frame.pack(side=RIGHT)
        self.search_icon = PhotoImage(file="photos/glass.png")
        self.search_lbl = Label(self.search_parent, image=self.search_icon, bg="#D9D9D9", cursor="hand2")
        self.search_lbl.pack(side=LEFT, padx=4)
        self.search_parent.place(x=331, y=27)
        self.search_lbl.bind("<Button-1>", self.search)

        # Tabs
        self.for_sale_normal = PhotoImage(file="photos/for_sale_nrml.png")
        self.for_sale_clicked = PhotoImage(file="photos/for_sale_clicked.png")
        self.for_rent_normal = PhotoImage(file="photos/for_rent_nrml.png")
        self.for_rent_clicked = PhotoImage(file="photos/for_rent_clicked.png")
        self.for_rent_lbl = Label(self, image=self.for_rent_clicked, bg="#FFFFFF", cursor="hand2")
        self.for_sale_lbl = Label(self, image=self.for_sale_normal, bg="#FFFFFF", cursor="hand2")
        self.for_rent_lbl.place(x=647, y=108)
        self.for_sale_lbl.place(x=530, y=108)
        self.for_rent_lbl.bind("<Button-1>", self.for_rent)
        self.for_sale_lbl.bind("<Button-1>", self.for_sale)

        # frames
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
                          owner_phone=result[17]
                          ))
        self.cars_for_sale.append(cars.Cars(manu="Toyota", model="Camry", year=2020, ID=1, owner_id=101,
                                            engine_capacity=2500, horsepower=200, top_speed=130, price=25000,
                                            photo_path=os.path.normcase("E:\\Summer Training Project\\Summer-Training\\photos\\01.jpg"), description="Reliable sedan", op_type="Sale",
                                            state="available",
                                            owner_phone="01558021688"
                                            ))

        self.cars_for_sale.append(cars.Cars(manu="Ford", model="Mustang", year=2018, ID=2, owner_id=102,
                                            engine_capacity=5000, horsepower=450, top_speed=160, price=35000,
                                            photo_path=os.path.normcase("E:\\Summer Training Project\\Summer-Training\\photos\\01.jpg"), description="Muscle car", op_type="Sale",
                                            state="available",
                                            owner_phone="01558021688"
                                            ))
        self.cars_for_sale.append(cars.Cars(manu="Toyota", model="Camry", year=2020, ID=1, owner_id=101,
                                            engine_capacity=2500, horsepower=200, top_speed=130, price=25000,
                                            photo_path=os.path.normcase("E:\\Summer Training Project\\Summer-Training\\photos\\01.jpg"), description="Reliable sedan", op_type="Sale",
                                            state="available",
                                            owner_phone="01558021688"
                                            ))

        self.cars_for_sale.append(cars.Cars(manu="Ford", model="Mustang", year=2018, ID=2, owner_id=102,
                                            engine_capacity=5000, horsepower=450, top_speed=160, price=35000,
                                            photo_path=os.path.normcase("E:\\Summer Training Project\\Summer-Training\\photos\\01.jpg"), description="Muscle car", op_type="Sale",
                                            state="available",
                                            owner_phone="01558021688"
                                            ))
        self.cars_for_sale.append(cars.Cars(manu="Toyota", model="Camry", year=2020, ID=1, owner_id=101,
                                            engine_capacity=2500, horsepower=200, top_speed=130, price=25000,
                                            photo_path=os.path.normcase("E:\\Summer Training Project\\Summer-Training\\photos\\01.jpg"), description="Reliable sedan", op_type="Sale",
                                            state="available",
                                            owner_phone="01558021688"
                                            ))

        self.cars_for_sale.append(cars.Cars(manu="Ford", model="Mustang", year=2018, ID=2, owner_id=102,
                                            engine_capacity=5000, horsepower=450, top_speed=160, price=35000,
                                            photo_path=os.path.normcase("E:\\Summer Training Project\\Summer-Training\\photos\\01.jpg"), description="Muscle car", op_type="Sale",
                                            state="available",
                                            owner_phone="01558021688"
                                            ))
        self.cars_for_sale.append(cars.Cars(manu="Toyota", model="Camry", year=2020, ID=1, owner_id=101,
                                            engine_capacity=2500, horsepower=200, top_speed=130, price=25000,
                                            photo_path=os.path.normcase("E:\\Summer Training Project\\Summer-Training\\photos\\01.jpg"), description="Reliable sedan", op_type="Sale",
                                            state="available",
                                            owner_phone="01558021688"
                                            ))

        self.cars_for_sale.append(cars.Cars(manu="Ford", model="Mustang", year=2018, ID=2, owner_id=102,
                                            engine_capacity=5000, horsepower=450, top_speed=160, price=35000,
                                            photo_path=os.path.normcase("E:\\Summer Training Project\\Summer-Training\\photos\\01.jpg"), description="Muscle car", op_type="Sale",
                                            state="available",
                                            owner_phone="01558021688"
                                            ))
        self.cars_for_sale.append(cars.Cars(manu="Toyota", model="Camry", year=2020, ID=1, owner_id=101,
                                            engine_capacity=2500, horsepower=200, top_speed=130, price=25000,
                                            photo_path=os.path.normcase("E:\\Summer Training Project\\Summer-Training\\photos\\01.jpg"), description="Reliable sedan", op_type="Sale",
                                            state="available",
                                            owner_phone="01558021688"
                                            ))

        self.cars_for_sale.append(cars.Cars(manu="Ford", model="Mustang", year=2018, ID=2, owner_id=102,
                                            engine_capacity=5000, horsepower=450, top_speed=160, price=35000,
                                            photo_path=os.path.normcase("E:\\Summer Training Project\\Summer-Training\\photos\\01.jpg"), description="Muscle car", op_type="Sale",
                                            state="available",
                                            owner_phone="01558021688"
                                            ))

        self.for_sale_frame = cg.CarGrid(self.parent_frame, controller, self.cars_for_sale)
        self.for_rent_frame = cg.CarGrid(self.parent_frame, controller, self.cars_for_rent)
        self.for_sale_frame.grid_propagate(False)
        self.for_rent_frame.grid_propagate(False)
        self.for_sale_frame.grid(row=0, column=0)
        self.for_rent_frame.grid(row=0, column=0)
        self.for_sale_frame.tkraise()
        self.curr_view = "for_sale"
        self.parent_frame.place(x=70, y=160)

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

    def search(self, event):
        pass
