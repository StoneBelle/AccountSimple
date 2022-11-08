from homescreen import *
from menu import *
from tkinter import *
from modify_data import *
import time


# Root Window & Main Frame
app = AppWindow("Account Simple  4.0")
frame = AppFrame(app)
MenuBar(app, frame.update_login, frame.delete_login, frame.view_all)

# TODO #1: Create a Menu bar for Root Window


app.mainloop()
