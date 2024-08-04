import Car_Rental_View
import Login
import Signup
from Signup import *
from tkinter import *
from Login import *
import Car_Rental_View as crv
import Car_Sale_View as crs
import User as user
import MainPage as mp
import Cars as cr
import DatePicker as dp
import Util as ut


class App(Tk):
    def __init__(self):
        super().__init__()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"1280x720+{int((screen_width - 1280) / 2)}+{int((screen_height - 720) / 2)}")
        self.resizable(False, False)
        self.container = Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.car_rent_view = crv.Car_Rental_View(self.container, self, cr.placeholder)
        self.login_frame = Login(self.container, self)
        # self.main_page = mp.MainPage(self.container, self)
        self.signup_frame = Signup(self.container, self)
        self.title("The Autoshop")
        self.login_frame.grid(row=0, column=0)
        # self.main_page.grid(row=0, column=0)
        self.signup_frame.grid(row=0, column=0)
        self.car_rent_view.grid(row=0, column=0)
        self.show_frame("Login")

    def resize_window(self, width, height):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"{width}x{height}+{int((screen_width - width) / 2)}+{int((screen_height - height) / 2)}")

    def show_frame(self, frame_name, car=None):
        if frame_name == "Signup":

            self.signup_frame.tkraise()
        elif frame_name == "Login":

            self.login_frame.tkraise()
        elif frame_name == "car_rent_view":
            self.car_frame = crv.Car_Rental_View(self.container, self, car)
            self.car_frame.grid(row=0, column=0)
            self.car_frame.tkraise()
        elif frame_name == "car_sale_view":
            self.car_frame = crs.Car_Sale_View(self.container, self, car)
            self.car_frame.grid(row=0, column=0)
            self.car_frame.tkraise()
        elif frame_name == "main_page":
            self.main_page = mp.MainPage(self.container, self)
            self.main_page.grid(row=0, column=0)
            self.main_page.tkraise()
        elif frame_name == "date_picker":
            self.date_picker = dp.Date_Picker(self.container , self  ,  car)
            self.date_picker.grid(row=0, column=0)
            self.date_picker.tkraise()
        elif frame_name == "listed_cars":
            pass
        elif frame_name == "add_car":
            pass
        elif frame_name == "rented_cars":
            pass


app = App()
app.mainloop()
