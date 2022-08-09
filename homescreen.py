import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, END
import json

# GUI CONSTANTS
BG_COL = "#FFFFFF"
FONT = "Arial", 8, "bold"


# TODO #1: Create Home Screen
# Class that inherits tk.Tk to create a window object
class AppWindow(tk.Tk):
    def __init__(self, title):
        super().__init__()
        self.config(bg=BG_COL, padx=100, pady=30)
        self.title(title)

        # img = tk.PhotoImage(file="logo.png")
        # self_logo =tk.Label(self, image=img)
        # self_logo.grid(column=0, row=1)

        # Window Responsiveness
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)


# Class that inherits ttk.Frame to create a Frame object inside a window
# The window created from the AppWindow class will be passed in as the 'root' for this Frame
class AppFrame(ttk.Frame):
    def __init__(self, root):
        super().__init__(root)

        # ttk Widget Styles
        style = ttk.Style()
        style.configure("TFrame", background=BG_COL)
        style.configure("TButton", background=BG_COL)
        style.configure("TLabel", background=BG_COL, font=FONT)

        # ttk Widgets
        self.prompt_label = ttk.Label(self, text="Save or find your Account login below.")
        self.acc_label = ttk.Label(self, text="Account :  ")
        self.user_label = ttk.Label(self, text="Username :  ")
        self.pass_label = ttk.Label(self, text="Password :  ")

        self.acc_entry = ttk.Entry(self, width=36)
        self.user_entry = ttk.Entry(self, width=55)
        self.pass_entry = ttk.Entry(self, width=36, show="*")

        self.find_button = ttk.Button(self, text="Find Login", width=17)
        self.pass_button = ttk.Button(self, text="Generate Password", width=17)
        self.add_button = ttk.Button(self, text="Save Login", width=53, command=self.save_login)

        # ttk Widget grid
        self.prompt_label.grid(column=3, columnspan=2, row=1, rowspan=2, pady=(0, 20))
        self.acc_label.grid(column=2, row=2, padx=(8, 0), pady=(50, 0))
        self.user_label.grid(column=2, row=3)
        self.pass_label.grid(column=2, row=4, padx=(3, 0), pady=(0, 50))

        self.acc_entry.grid(column=3, row=2, pady=(50, 6), ipady=2)
        self.user_entry.grid(column=3, columnspan=2, row=3, ipady=2)
        self.pass_entry.grid(column=3, row=4, pady=(6, 50), ipady=2)

        self.acc_entry.grid(column=3, row=2, ipady=3)
        self.user_entry.grid(column=3, columnspan=2, row=3, ipady=3, ipadx=4)
        self.pass_entry.grid(column=3, row=4, ipady=3)

        self.find_button.grid(column=4, row=2, padx=(5, 0), pady=(50, 7))
        self.pass_button.grid(column=4, row=4, padx=(5, 0), pady=(5, 50))
        self.add_button.grid(column=3, columnspan=2, row=4, pady=(20, 0), ipadx=9)
        self.grid()

    def save_login(self):
        account = self.acc_entry.get()
        username = self.user_entry.get()
        password = self.pass_entry.get()

        login_data = {account: {
            "username": username,
            "password": password}
        }

        if len(account) == 0 and len(username) == 0 and len(password) == 0:
            messagebox.showerror(title="Missing Required Fields", message="You must fill in all fields to continue.")
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)  # Reading old data
        except FileNotFoundError:  # This will occur if file is not found (i.e. if try does not work)
            with open("data.json", "w") as data_file:
                json.dump(login_data, data_file, indent=4)  # Write new data
        else:  # This will occur if file is found (i.e. if try does work)
            with open("data.json", "w") as data_file:
                data.update(login_data)  # Updating old data with new data
                json.dump(data, data_file, indent=4)  # Saving updated data

        self.acc_entry.delete(0, END)
        self.user_entry.delete(0, END)
        self.pass_entry.delete(0, END)
