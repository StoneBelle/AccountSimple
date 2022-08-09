from homescreen import AppWindow, AppFrame
from tkinter import *

# Account Simple 4.0


# Password Components
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
menu_items = ("Update Login", "Delete Login", "Portrait View", "Landscape View", "View All", "Tutorial", "FAQ")


def make_menu(menu_tab, start, end, tf):
    tab = Menu(menu_bar, tearoff=False)
    count = 0
    for item in menu_items[slice(start, end)]:
        count += 1
        tab.add_command(label=item)
        if tf and count == 2:
            tab.add_separator()
    menu_bar.add_cascade(label=menu_tab, menu=tab)


# Root Window
app = AppWindow("Account Simple  4.0")

# Menu bar for Root Window
menu_bar = Menu(app)
app.config(menu=menu_bar)
make_menu("Edit", 0, 2, False)
make_menu("View", 2, 5, True)
make_menu("Help", 5, 8, False)

frame = AppFrame(app)

app.mainloop()

# TODO #2 : Create Menu Bar

# Create a class for Menu Bar

# Create Menu Bar categories

# Create a customizable Toplevel widget for pop-up screen

# Create a Scrollbar

# TODO #3: Create JSON  functions to read, write, and update data
