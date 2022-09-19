from homescreen import AppWindow, AppFrame
from menu import *
from tkinter import *

# # Root Window
# app = AppWindow("Account Simple  4.0")
# frame = AppFrame(app)
# menu = MenuBar(app)
# app.mainloop()

# Create Menu bar for the
# homescreen
MENU_ITEMS = ("Update Login", "Delete Login", "Portrait View", "Landscape View", "View All", "Tutorial", "FAQ")


def make_menu(menu_tab, start, end, tf, cmd):
    """Create a custom Menu bar by filling the parameters.
    """
    tab = Menu(menu_bar, tearoff=False)
    count = 0
    for item in MENU_ITEMS[slice(start, end)]:
        count += 1
        tab.add_command(label=item, command=cmd)
        if tf and count == 2:
            tab.add_separator()
    menu_bar.add_cascade(label=menu_tab, menu=tab)


# Root Window
app = AppWindow("Account Simple  4.0")
frame = AppFrame(app)

# Menu bar for Root Window
menu_bar = Menu(app)

# Menu bar tabs
make_menu("Edit", 0, 2, False, frame.update_login)
make_menu("View", 2, 5, True, frame.update_login)
make_menu("Help", 5, 8, False, frame.update_login)
app.config(menu=menu_bar)

app.mainloop()
