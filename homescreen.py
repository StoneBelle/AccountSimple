import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, END
import json
import random

# GUI CONSTANTS
BG_COL = "#FFFFFF"
FONT = "Arial", 8, "bold"

# Password Components
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


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


def change_text(entry_input, label):
    if len(entry_input) == 0:
        label.config(foreground="red")
    else:
        label.config(foreground="black")


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

        self.find_button = ttk.Button(self, text="Find Login", width=17, command=self.find_login)
        self.pass_button = ttk.Button(self, text="Generate Password", width=17, command=self.make_password)
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

    def find_login(self):
        account = self.acc_entry.get()
        # Retrieve user input from account entry box
        try:  # Check for saved data
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:  # If no existing data inform user
            messagebox.showerror(title="Account Error", message=f"There are currently no saved Accounts.")
        else:  # If existing data retrieve login info using input from account
            if account in data.keys():
                saved_user = data[account]["username"]
                saved_pass = data[account]["password"]
                messagebox.showinfo(title="Account Login Retrieved", message=f'"{account}" Account Login Found:        '
                                                                             f' \n\nUsername:  {saved_user}'
                                                                             f'\nPassword:  {saved_pass}')
            else:
                if len(account) == 0:
                    messagebox.showerror(title="Missing Required Field",message="Enter the account name to continue.")
                    change_text(account, self.acc_label)

                else:
                    change_text(account, self.acc_label)
                    messagebox.showerror(title="Account Error", message=f'No existing login for "{account}" was found.')

    # Return login info to user in messagebox

    def save_login(self):
        account = self.acc_entry.get()
        username = self.user_entry.get()
        password = self.pass_entry.get()

        login_data = {account: {
            "username": username,
            "password": password}
        }

        if len(account) == 0 or len(username) == 0 or len(password) == 0:
            messagebox.showerror(title="Missing Required Fields", message="You must fill in all fields to continue.")
            change_text(username, self.user_label)

        else:
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)  # Reading old data
            except FileNotFoundError:  # This will occur if file is not found (i.e. if try does not work)
                with open("data.json", "w") as data_file:
                    json.dump(login_data, data_file, indent=4)  # Write new data
            else:  # This will occur if file is found (i.e. if try does work)
                if account in data.keys():
                    messagebox.askyesno(title="Account Login Found", message=f'A login for "{account}" already exists.'
                                                                             f'\nWould you like to view it?')
                else:
                    with open("data.json", "w") as data_file:
                        data.update(login_data)  # Updating old data with new data
                        json.dump(data, data_file, indent=4)  # Saving updated data
                    messagebox.showinfo(title="Login Successfully Saved", message=f"Login for {account} was saved.")

            finally:
                self.acc_entry.delete(0, END)
                self.user_entry.delete(0, END)
                self.pass_entry.delete(0, END)

        change_text(account, self.acc_label)
        change_text(username, self.user_label)
        change_text(password, self.pass_label)

    def make_password(self):
        self.pass_entry.delete(0, END)
        self.pass_entry.config(show="")
        pass_requirements = [random.choice(letters) for x in range(7)]
        pass_requirements += [random.choice(letters).upper() for x in range(2)]
        pass_requirements += [random.choice(numbers) for x in range(4)]
        pass_requirements += [random.choice(symbols) for x in range(2)]
        random.shuffle(pass_requirements)
        generated_pass = "".join(pass_requirements)
        self.pass_entry.insert(0, generated_pass)
        print(pass_requirements)
