from tkinter import *
from PIL import Image, ImageTk
import Util as ut
root = Tk()
root.configure(background='white')
root.title('My Listed Cars')
window_width = 1280
window_height = 690
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 1.80)
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.resizable(False, False)
font=('Helvetica', 16)
lbl1 =ut.create_label(root,width=280,height=40,text='My Listed Cars',font=("Helvetica", 20))
lbl1.place(x=10,y=30)
sale_button_frame,sale_button = ut.create_button(root,height=40 ,width= 100,color='red',text='For Sale',font=("Helvetica", 16))
sale_button_frame.place(x=531,y=24)
rent_button_frame,rent_button = ut.create_button(root,height=40 ,width= 100,color='red',text='For Rent',font=("Helvetica", 16))
rent_button_frame.place(x=648,y=24)
add_lbl =ut.create_label(root,width=62,height=16,text='Add Car')
add_lbl.place(x=1157,y=30)
def delet_buton(y):
    delete_button_frame,delete_button = ut.create_button(root,height=40 ,width= 117,color='red',text='Delete',font=("Helvetica", 16))
    delete_button_frame.place(x=1131,y=y)
delet_buton(162)
delet_buton(329)
delet_buton(495)
back_button_frame,back_button = ut.create_button(root,height=40 ,width= 121,color='red',text='Back',font=("Helvetica", 16))
back_button_frame.place(x=980,y=640)
quit_button_frame,quit_button = ut.create_button(root,height=40 ,width= 121,color='grey',text='Quit',font=("Helvetica", 16))
quit_button_frame.place(x=1127,y=640)

car1 = Label(root, text="Hyundai Elantra 2022", font=("Helvetica", 16),background='white')
car1.place(x=302, y=179, anchor='w')
car2 = Label(root, text="BMW M3 2010", font=("Helvetica", 16),background='white')
car2.place(x=302, y=346, anchor='w')
car3 = Label(root, text="Volkswagen Golf 2005", font=("Helvetica", 16),background='white')
car3.place(x=302, y=492, anchor='w')
add_photo = PhotoImage(file='photos/add.png')
lbl =Label(root,image=add_photo,height=32,width=32,background='white')
lbl.place(x=1226,y=22)

image1_path = "photos/download.jpg"
image1 = Image.open(image1_path)
image1 = image1.resize((247, 143))
photo1 = ImageTk.PhotoImage(image1)
lbl =Label(root,image=photo1,height=143,width=248,background='white')
lbl.place(x=32,y=117)
image2_path = "photos/2010-bmw-m3.jpg"
image2 = Image.open(image2_path)
image2 = image2.resize((248, 143))
photo2 = ImageTk.PhotoImage(image2)
lbl =Label(root,image=photo2,height=143,width=248,background='white')
lbl.place(x=32,y=270)
image3_path = "photos/images.jpg"
image3 = Image.open(image3_path)
image3 = image3.resize((248, 143))
photo3 = ImageTk.PhotoImage(image3)
lbl =Label(root,image=photo3,height=143,width=248,background='white')
lbl.place(x=32,y=430)

root.mainloop()