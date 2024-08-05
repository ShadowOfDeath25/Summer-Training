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
        self.lbl1=ut.create_label(root,width=274,height=17,text="Rented Cars",font=("Helvetica", 17))
        self.lbl1.place(x=32,y=30)

        # Frames
        self.parent_frame = Frame(self, bg="#FFFFFF", width=1280, height=600)
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
                          owner_phone=result[13]
                           ,rental_date=datetime.datetime.now().strftime("%Y / %m /%d")
                          ,return_date=datetime.datetime.now().strftime("%Y / %m /%d")
                          ))
        
        cars_for_sale = []
        cars_for_sale.append(car.Cars(manu="Toyota", model="Camry", year=2020, ID=1, owner_id=101,
                                        engine_capacity=2500, horsepower=200, top_speed=130, price=25000,
                                        photo_path=os.path.normcase(
                                            "photos/01.jpg"),
                                        description="Reliable sedan", op_type="Sale",
                                        state="available",
                                        owner_phone="01558021688",
                                        return_date=datetime.datetime.now().strftime("%Y / %m /%d"),
                                        rental_date=datetime.datetime.now().strftime("%Y / %m / %d")
                                        ))
        cars_for_sale.append(car.Cars(manu="Toyota", model="Camry", year=2020, ID=1, owner_id=101,
                                        engine_capacity=2500, horsepower=200, top_speed=130, price=25000,
                                        photo_path=os.path.normcase(
                                            "photos/01.jpg"),
                                        description="Reliable sedan", op_type="Sale",
                                        state="available",
                                        owner_phone="01558021688",
                                        return_date=datetime.datetime.now().strftime("%Y / %m /%d"),
                                        rental_date=datetime.datetime.now().strftime("%Y / %m / %d")
                                        ))
        cars_for_rent=[]
        cars_for_sale.append(car.Cars(manu="Toyota", model="Camry", year=2020, ID=1, owner_id=101,
                                        engine_capacity=2500, horsepower=200, top_speed=130, price=25000,
                                        photo_path=os.path.normcase(
                                            "photos/01.jpg"),
                                        description="Reliable sedan", op_type="Sale",
                                        state="available",
                                        owner_phone="01558021688",
                                        return_date=datetime.datetime.now().strftime("%Y / %m /%d"),
                                        rental_date=datetime.datetime.now().strftime("%Y / %m / %d")
                                        ))
        cars_for_sale.append(car.Cars(manu="Toyota", model="Camry", year=2020, ID=1, owner_id=101,
                                        engine_capacity=2500, horsepower=200, top_speed=130, price=25000,
                                        photo_path=os.path.normcase(
                                            "photos/01.jpg"),
                                        description="Reliable sedan", op_type="Sale",
                                        state="available",
                                        owner_phone="01558021688",
                                        return_date=datetime.datetime.now().strftime("%Y / %m /%d"),
                                        rental_date=datetime.datetime.now().strftime("%Y / %m / %d")
                                        ))
        cars_for_sale.append(car.Cars(manu="Toyota", model="Camry", year=2020, ID=1, owner_id=101,
                                        engine_capacity=2500, horsepower=200, top_speed=130, price=25000,
                                        photo_path=os.path.normcase(
                                            "photos/01.jpg"),
                                        description="Reliable sedan", op_type="Sale",
                                        state="available",
                                        owner_phone="01558021688",
                                        return_date=datetime.datetime.now().strftime("%Y / %m /%d"),
                                        rental_date=datetime.datetime.now().strftime("%Y / %m / %d")
                                        ))


        self.for_sale_frame = cg.CarGrid(self.parent_frame, controller, self.cars_for_sale)
        self.for_rent_frame = cg.CarGrid(self.parent_frame, controller, self.cars_for_rent)
        self.for_sale_frame.grid_propagate(False)
        self.for_rent_frame.grid_propagate(False)
        self.for_sale_frame.grid(row=0, column=0)
        self.for_rent_frame.grid(row=0, column=0)
        self.for_sale_frame.tkraise()
        self.curr_view = "for_sale"
        self.parent_frame.place(x=30, y=100)

        
       
        self.back_btn_frame, self.back_btn = ut.create_button(self, 121, 40, "red", "Back")
        self.quit_btn_frame, self.quit_btn = ut.create_button(self, 121, 40, "grey", "Quit")
        
        self.back_btn_frame.place(x=980, y=660)
        self.quit_btn_frame.place(x=1127, y=660)
        self.quit_btn.config(command=lambda: controller.destroy())
        self.back_btn.config(command=lambda: controller.show_frame("Login"))
      

        
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


root = Tk()
root.geometry("1280x720")
frame = Frame(root)
frame.pack(fill=BOTH, expand=True)
frame.pack_propagate(False)
frame.grid_propagate(False)
ob=MainPage(parent=frame,controller=root)
mp = cg.CarGrid(frame, root, MainPage.cars_for_rent)
mp.pack(fill=BOTH, expand=True)
root.mainloop()