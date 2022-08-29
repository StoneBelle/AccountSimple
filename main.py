import tkinter as tk
from tkinter import messagebox, END
from menu_bar import MenuBar
from data import *
import random

# GUI CONSTANTS
BG_COL = "#FFFFFF"
OPTNL_BTN = "#EECF7F"
MNDTRY_BTN = "#EF967A"
FONT = "Arial", 8, "bold"

# Password Components
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


class InheritTk(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.config(bg=BG_COL, padx=100, pady=30)
        gui = LoginApplication(self)
        gui.master.title("Account Simple")
        gui.make_widgets(self)
        gui.landscape_view()
        gui.mainloop()

class LoginApplication(tk.Frame):
    def __init__(self, root):
        super(LoginApplication, self).__init__()

    def entry_inputs(self):
        """Returns the user inputs from Account, Username, and Password entry boxes. These inputs are stored as global
        variables which are called in the following class functions: save_login and find_login. """
        global account, username, password
        account = self.acc_entry.get().strip()
        username = self.user_entry.get().replace(" ", "")
        password = self.pass_entry.get().replace(" ", "")
        return account, username, password

    def save_login(self):
        """Stores inputted login information from entry boxes into a JSON file."""
        self.entry_inputs()
        new_login = {
            account: {
                "username": username,
                "password": password
            }
        }

        if len(account) == 0 or len(username) == 0 or len(password) == 0:
            messagebox.showerror(title="Missing Information", message="Please do not leave any fields blank.")
        else:
            try:
                login_dict = read_data()
            except FileNotFoundError:
                with open("login_data.json", "w") as data_file:
                    json.dump(new_login, data_file, indent=4)
            else:
                if account in login_dict:
                    messagebox.showinfo(title="Existing Login", message=f'A login for "{account}" already exists.')
                with open("login_data.json", "w") as data_file:
                    login_dict.update(new_login)  # Updates python dict w new input from user
                    json.dump(login_dict, data_file, indent=4)

            self.acc_entry.delete(0, END)
            self.user_entry.delete(0, END)
            self.pass_entry.delete(0, END)

    def find_login(self):
        """Searches for an account login by entering an account name in the account entry box."""
        self.entry_inputs()
        if len(account) == 0:
            messagebox.showerror(title="Missing Information", message="Enter the account name to search for a login.")
        else:
            try:
                login_dict = read_data()
            except FileNotFoundError:
                messagebox.showerror(title="No Login Found",
                                     message=f'There is no saved login details for "{account}".')
            else:
                if account in login_dict:
                    messagebox.showinfo(title=f"{account} Login Information",
                                        message=f"The following details shown are for your {account} account.\n"
                                                f"\nUsername: {login_dict[account]['username']}"
                                                f"\nPassword: {login_dict[account]['password']}")
                else:
                    messagebox.showerror(title="No Login Found",
                                         message=f'Login details for "{account}" does not exist.')

    def make_password(self):
        """Generates a secure 15 character password composed of a random mix of letters, numbers, and symbols."""
        self.pass_entry.delete(0, END)
        pass_requirements = [random.choice(letters) for letter in range(7)]
        pass_requirements += [random.choice(letters).upper() for letter in range(3)]
        pass_requirements += [random.choice(numbers) for num in range(4)]
        pass_requirements += [random.choice(symbols) for symbol in range(2)]
        random.shuffle(pass_requirements)
        generated_pass = "".join(pass_requirements)
        self.pass_entry.insert(0, generated_pass)

    def make_widgets(self, root):
        root.rowconfigure(0, weight=1)
        root.rowconfigure(6, weight=1)
        root.columnconfigure(0, weight=1)
        root.columnconfigure(5, weight=1)

        self.menu = MenuBar(root)
        self.logo_img = tk.PhotoImage(file="the_logo.png")
        self.logo_label = tk.Label(root, image=self.logo_img, bg=BG_COL)
        self.prompt_label = tk.Label(root, text="Find or Save your Account login below.", bg=BG_COL, pady=20)

        self.acc_label = tk.Label(root, text="Account For:", bg=BG_COL, font=FONT)
        self.user_label = tk.Label(root, text="Username:", bg=BG_COL, font=FONT)
        self.pass_label = tk.Label(root, text="Password:", bg=BG_COL, font=FONT)

        self.acc_entry = tk.Entry(root, width=36, bg=BG_COL)
        self.user_entry = tk.Entry(root, width=55, bg=BG_COL)
        self.pass_entry = tk.Entry(root, width=36, bg=BG_COL)

        self.find_button = tk.Button(root, text="Find Specific Login", command=self.find_login, width=15, bg=OPTNL_BTN)
        self.pass_button = tk.Button(root, text="Generate Password", command=self.make_password, width=15, bg=OPTNL_BTN)
        self.add_button = tk.Button(root, text="Save Login", command=self.save_login, width=45, bg=MNDTRY_BTN)

    def landscape_view(self):
        self.logo_label.grid(column=1, row=1, rowspan=5, pady=(0, 20))
        self.grid_widgets()

    def portrait_view(self):
        self.logo_label.grid(column=3, columnspan=2, row=0)
        self.grid_widgets()

    def grid_widgets(self):
        self.prompt_label.grid(column=3, columnspan=2, row=1, rowspan=2, pady=(0, 20))
        self.acc_label.grid(column=2, row=2, padx=(0, 15), pady=(50, 0))
        self.user_label.grid(column=2, row=3, padx=(0, 9))
        self.pass_label.grid(column=2, row=4, padx=(0, 9), pady=(0, 50))

        self.acc_entry.grid(column=3, row=2, pady=(50, 6), ipady=2)
        self.user_entry.grid(column=3, columnspan=2, row=3, ipady=2)
        self.pass_entry.grid(column=3, row=4, pady=(6, 50), ipady=2)

        self.acc_entry.grid(column=3, row=2, ipady=3)
        self.user_entry.grid(column=3, columnspan=2, row=3, ipady=3, ipadx=4)
        self.pass_entry.grid(column=3, row=4, ipady=3)

        self.find_button.grid(column=4, row=2, padx=(5, 0), pady=(50, 7))
        self.pass_button.grid(column=4, row=4, padx=(5, 0), pady=(5, 50))
        self.add_button.grid(column=3, columnspan=2, row=4, pady=(20, 0), ipadx=9)


lol = InheritTk()
