from homescreen import *
from menu import *
from tkinter import *
from modify_data import *
import time

MENU_ITEMS = ("Update Login", "Delete Login", "Portrait View", "Landscape View", "View All", "Tutorial", "FAQ")
DISABLE_STATE = ("Update Login", "Delete Login", "View All")


# Root Window & Main Frame
app = AppWindow("Account Simple  4.0")
frame = AppFrame(app)
MenuBar(app, frame.update_login)

# TODO #1: Create a Menu bar for Root Window
# menu_bar = Menu(app)
# app.config(menu=menu_bar)

# Menu bar tabs
# make_menu("Edit", 0, 2, False, frame.update_login)
# make_menu("View", 2, 5, True, frame.update_login)
# make_menu("Help", 5, 8, False, frame.update_login)
# # menu_bar.delete("Edit")

app.mainloop()
