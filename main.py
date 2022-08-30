from homescreen import AppWindow, AppFrame
import tkinter as tk
from tkinter import *

menu_items = ("Update Login", "Delete Login", "Portrait View", "Landscape View", "View All", "Tutorial", "FAQ")




# def make_menu(menu_tab, start, end, tf):
#     tab = Menu(menu_bar, tearoff=False)
#     count = 0
#     for item in menu_items[slice(start, end)]:
#         count += 1
#         tab.add_command(label=item)
#         if tf and count == 2:
#             tab.add_separator()
#     menu_bar.add_cascade(label=menu_tab, menu=tab)


 # Root Window
app = AppWindow("Account Simple  4.0")


# # Menu bar for Root Window
# menu_bar = Menu(app)
#
# # Menu bar tabs
# edit_tab = make_menu("Edit", 0, 2, False)
# make_menu("View", 2, 5, True)
# make_menu("Help", 5, 8, False)

frame = AppFrame(app)

app.mainloop()





# Create a customizable Toplevel widget for pop-up screen
# Create a Scrollbar
