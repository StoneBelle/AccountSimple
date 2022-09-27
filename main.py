from homescreen import AppWindow, AppFrame
from menu import *
from tkinter import *
from modify_data import *
import time

MENU_ITEMS = ("Update Login", "Delete Login", "Portrait View", "Landscape View", "View All", "Tutorial", "FAQ")
DISABLE_STATE = ("Update Login", "Delete Login", "View All")


def make_menu(menu_tab, start, end, tf, cmd):
    """Create a custom Menu bar by filling the parameters."""
    tab = Menu(menu_bar, tearoff=False)
    count = 0

    try:  # Checking for saved data
        read_data()
    except FileNotFoundError:
        for item in MENU_ITEMS[slice(start, end)]:
            count += 1
            if tf and count == 2:
                tab.add_separator()
            if item in DISABLE_STATE:
                tab.add_command(label=item, command=cmd, state=DISABLED)
            else:
                tab.add_command(label=item, command=cmd)
    else:  # If existing data found, retrieve login info using input from account
        for item in MENU_ITEMS[slice(start, end)]:
            count += 1
            if tf and count == 2:
                tab.add_separator()
        tab.add_command(label=item, command=cmd)
    finally:
        menu_bar.add_cascade(label=menu_tab, menu=tab)



# Root Window
app = AppWindow("Account Simple  4.0")
frame = AppFrame(app)

# Menu bar for Root Window
menu_bar = Menu(app)
app.config(menu=menu_bar)

# Menu bar tabs
make_menu("Edit", 0, 2, False, frame.update_login)
make_menu("View", 2, 5, True, frame.update_login)
make_menu("Help", 5, 8, False, frame.update_login)

app.mainloop()
