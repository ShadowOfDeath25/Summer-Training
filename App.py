import Login
import Signup
from Signup import *
from tkinter import *
from Login import *
#import Car_Rental_View as crv
import User as user
import MainPage as mp


class App(Tk):
    def __init__(self):
        super().__init__()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"1280x720+{int((screen_width - 1280) / 2)}+{int((screen_height-720) / 2)}")
        self.resizable(False, False)
        self.container = Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        #self.car_rental_view_frame= crv.Car_Rental_View(self.container,self)
        #self.car_rental_view_frame.grid(row=0, column=0)
        self.login_frame = Login(self.container, self)
        self.main_page = mp.MainPage(self.container, self)
        self.signup_frame = Signup(self.container, self)
        self.title("The Autoshop")
        self.login_frame.grid(row=0, column=0)
        self.main_page.grid(row=0, column=0)
        self.signup_frame.grid(row=0, column=0)
        self.show_frame("Login")

    def resize_window(self, width, height):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"{width}x{height}+{int((screen_width - width) / 2)}+{int((screen_height - height) / 2)}")

    def show_frame(self, frame_name, car=None, usr=user.current_user):
        if frame_name == "Signup":

            self.signup_frame.tkraise()
        elif frame_name == "Login":

            self.login_frame.tkraise()
        elif frame_name == "car_sale_view":
            pass

        elif frame_name == "main_page":
            self.main_page.tkraise()


app = App()
app.mainloop()
