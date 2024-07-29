from tkinter import *
from tkinter import ttk


def create_button(window, width, height, color="red", text="Button", font=("Helvetica", 10)):
    frame = Frame(window, width=width, height=height)
    btn = Button(frame)
    if color == "red":
        btn.config(bg="#EC221F")
    elif color == "grey":
        btn.config(bg="#6A6A6A")

    frame.pack_propagate(False)
    btn.config(fg="#FEE9E7", highlightthickness=0, borderwidth=0, cursor="hand2", text=text, font=font)
    btn.pack(fill=BOTH, expand=True)
    return frame


def create_entry(window, width, height, font=("Helvetica", 12)):
    frame = Frame(window, width=width, height=height, bg="#D9D9D9")
    entry = Entry(frame, bg="#D9D9D9", font=font, borderwidth=0)
    frame.pack_propagate(False)
    entry.pack(fill=BOTH, expand=True, padx=10, pady=10)
    return frame


def create_label(window, width, height, text, font=("Helvetica", 12)):
    frame = Frame(window, width=width, height=height, bg="#FFFFFF")
    frame.pack_propagate(False)
    label = Label(frame, text=text, font=font)
    label.pack(fill=BOTH, expand=True)
    return frame


def create_password(window, width, height, image_hidden, image_shown, font=("Helvetica", 12)):
    def hide(event):

        if entry["show"] == "*":
            vision.config(image=image_shown)
            entry.config(show="")
        else:
            vision.config(image=image_hidden)
            entry.config(show="*")

    parent_frame = Frame(window, bg="#D9D9D9", height=height, width=width)
    frame = Frame(parent_frame, width=width, height=height, bg="#D9D9D9")
    entry = Entry(frame, bg="#D9D9D9", font=font, borderwidth=0, show="*")
    frame.pack_propagate(False)
    entry.pack(fill=BOTH, expand=True)
    hidden = True
    vision = Label(parent_frame, image=image_hidden, bg="#D9D9D9", cursor="hand2")
    vision.bind("<Button-1>", hide)
    frame.pack(padx=10, side=LEFT)
    vision.pack(padx=10, side=RIGHT)
    return parent_frame




