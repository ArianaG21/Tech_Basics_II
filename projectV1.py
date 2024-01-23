import tkinter as tk
import customtkinter as ctk
from customtkinter import CTkImage, CTk
from tkinter import messagebox
from datetime import datetime
from PIL import Image


# create the gui window
window = ctk.CTk()

# name the gui window
window.title("Moonchildren")

#
label = ctk.CTkLabel(window, text = "An App for lovers of galaxy",
                     fg_color = "dark blue",
                     text_color = "yellow",
                     corner_radius = 10 )
label.pack()
# define the width and height of the app
width, height = 600, 450

# set the gui window size
window.geometry(f"{width}x{height}")
# set the gui minimum window size
window.minsize(width,height)

button = ctk.CTkButton(window, text = "Click here",
                       text_color = "white")
button.pack()
background = ctk.CTkImage(dark_image =Image.open("images/MoonBG.png"), size=(550, 400))
window.mainloop()
