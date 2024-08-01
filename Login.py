from tkinter import *
from tkinter import ttk, messagebox
import DbConnection as db
import Util as ut
import bcrypt
import mysql.connector


class Login(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.config(width=800, height=600, bg="#FFFFFF")
        self.welcome_lbl = ut.create_label(self,303,31,"Welcome to the Autoshop!",("Helvitica",18,"bold"))