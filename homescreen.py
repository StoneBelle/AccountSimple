import random
from modify_data import *
import tkinter as tk
from tkinter import ttk
from tkinter import *
import time

# Password Components
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

MENU_ITEMS = ("Update Login", "Delete Login", "Portrait View", "Landscape View", "View All", "Tutorial", "FAQ")
DISABLE_STATE = ("Update Login", "Delete Login", "View All")


# TODO #1: Create Home Screen
class AppWindow(tk.Tk):
    """Class that inherits tk.Tk to create a window object."""
    def __init__(self, title):
        super().__init__()
        self.config(bg=BG_COL, padx=100, pady=30)
        self.title(title)
        # self.geometry("700x500")

        # Window Responsiveness
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)


class AppFrame(ttk.Frame):
    """Class that inherits ttk.Frame to create a Frame object inside a window."""
    def __init__(self, root):
        super().__init__(root)
        # ttk Widget Styles
        style = ttk.Style()
        style.configure("TFrame", background=BG_COL)
        style.configure("TButton", background=BG_COL)
        style.configure("TLabel", background=BG_COL, font=FONT)
        # print(style.lookup("TFrame", "background"))  # Checks current style applied. Takes 2 parameters: name & widget
        # print(style.theme_names())  # Shows different styles available in the OS.
        global menu
        menu = MenuBar(root, self)

        self.make_widgets(self)
        self.grid()

    def make_widgets(self, wn):

        # ttk Widgets
        global acc_entry
        global user_entry
        global pass_entry
        global acc_label
        global user_label
        global pass_label

        prompt_label = ttk.Label(wn, text="Save or find your Account login below.")
        acc_label = ttk.Label(wn, text="  Account :  ")
        user_label = ttk.Label(wn, text="Username :  ")
        pass_label = ttk.Label(wn, text="Password :  ")

        acc_entry = ttk.Entry(wn, width=36)
        user_entry = ttk.Entry(wn, width=55)

        pass_entry = ttk.Entry(wn, width=36)  # to hide password char use: show="*"

        find_button = ttk.Button(wn, text="Find Login", width=17, command=self.find_login)
        pass_button = ttk.Button(wn, text="Generate Password", width=17, command=self.make_password)
        add_button = ttk.Button(wn, text="Save Login", width=53, command=self.save_login)

        # Widget grid
        prompt_label.grid(column=3, columnspan=2, row=1, rowspan=2, pady=(0, 20))
        acc_label.grid(column=2, row=2, padx=(8, 0), pady=(50, 0))
        user_label.grid(column=2, row=3)
        pass_label.grid(column=2, row=4, padx=(3, 0), pady=(0, 50))

        acc_entry.grid(column=3, row=2, pady=(50, 6), ipady=2)
        user_entry.grid(column=3, columnspan=2, row=3, ipady=2)
        pass_entry.grid(column=3, row=4, pady=(6, 50), ipady=2)

        acc_entry.grid(column=3, row=2, ipady=3)
        user_entry.grid(column=3, columnspan=2, row=3, ipady=3, ipadx=4)
        pass_entry.grid(column=3, row=4, ipady=3)

        find_button.grid(column=4, row=2, padx=(5, 0), pady=(50, 7))
        pass_button.grid(column=4, row=4, padx=(5, 0), pady=(5, 50))
        add_button.grid(column=3, columnspan=2, row=4, pady=(20, 0), ipadx=9)

    def find_login(self):
        """Retrieves user input from account entry box and checks if an existing login was saved. User will be notified
        via a messagebox on whether a login exists."""
        account = acc_entry.get()
        try:  # Checking for saved data
            data = read_data()
        except FileNotFoundError:  # If no existing data inform user
            messagebox.showerror(title="Account Error", message=f"There are currently no saved Accounts.")
        else:  # If existing data found, retrieve login info using input from account
            if account in data.keys():
                saved_user = data[account]["username"]
                saved_pass = data[account]["password"]
                messagebox.showinfo(title="Account Login Retrieved", message=f'"{account}" Account Login Found:        '
                                                                             f'\n\nUsername:  {saved_user}'
                                                                             f'\nPassword:  {saved_pass}')
            else:
                if len(account) == 0:
                    messagebox.showerror(title="Missing Required Field", message="Enter the account name to continue.")
                    update_label(account, acc_label)
                else:
                    update_label(account, acc_label)
                    messagebox.showerror(title="Account Error", message=f'No existing login for "{account}" was found.')

    def save_login(self):
        account = acc_entry.get().strip()
        username = user_entry.get().replace(" ", "")
        password = pass_entry.get().replace(" ", "")

        login_data = {account: {
            "username": username,
            "password": password}
        }

        if len(account) == 0 or len(username) == 0 or len(password) == 0:
            messagebox.showerror(title="Missing Required Fields", message="You must fill in all fields to continue.")
            update_label(username, user_label)

        else:
            try:
                data = read_data()
            except FileNotFoundError:
                write_data(login_data)
            else:
                if account in data.keys():
                    messagebox.showerror(title="Account Login Found", message=f'A login for "{account}" already exists')
                else:
                    update_data(data, login_data)
                    messagebox.showinfo(title="Login Successfully Saved", message=f"Login for {account} was saved.")
            finally:
                acc_entry.delete(0, END)
                user_entry.delete(0, END)
                pass_entry.delete(0, END)

        update_label(account, acc_label)
        update_label(username, user_label)
        update_label(password, pass_label)

        # menu.update_state()

    def make_password(self):
        pass_entry.delete(0, END)
        pass_requirements = [random.choice(letters) for x in range(7)]
        pass_requirements += [random.choice(letters).upper() for x in range(2)]
        pass_requirements += [random.choice(numbers) for x in range(4)]
        pass_requirements += [random.choice(symbols) for x in range(2)]
        random.shuffle(pass_requirements)
        generated_pass = "".join(pass_requirements)
        pass_entry.insert(0, generated_pass)
        print(pass_requirements)

    def make_pop_up(self, title, text):
        """Creates a customizable Toplevel if saved data is found. Returns the canvas frame to be used as the root for
        customizable widgets."""
        try:
            data = read_data()
        except FileNotFoundError:
            messagebox.showerror(title="No Accounts Saved", message="There are currently no Account logins saved.")
        else:
            # Retrieves Account names from saved data and stores it in an alphabetically sorted list called "accounts"
            global accounts
            accounts = sorted(tuple(data.keys()))

            # Creates a Toplevel with customizable title & size
            global top
            top = tk.Toplevel(bg=BG_COL)
            top.title(title)
            top.resizable(True, True)
            top.geometry("400x365")

            # Ensures Toplevel is responsive as window is resized
            top.grid_columnconfigure(0, weight=1)
            top.grid_rowconfigure(0, weight=1)
            top.grid_columnconfigure(5, weight=1)
            top.grid_rowconfigure(5, weight=1)

            # Toplevel Frames
            global outer_frame
            outer_frame = ttk.Frame(top)
            inner_frame = ttk.Frame(outer_frame)

            # Toplevel Widgets
            global header
            global right_btn
            header = ttk.Label(outer_frame, text=f"Select {text}")
            left_btn = ttk.Button(outer_frame, text="Cancel", style="Left.TButton", command=lambda: top.destroy())
            right_btn = ttk.Button(outer_frame, text="Next", style="Right.TButton")

            # Canvas & Scrollbar
            canvas = tk.Canvas(inner_frame, bg=BG_COL)
            global scrollbar
            scrollbar = ttk.Scrollbar(inner_frame, orient="vertical", command=canvas.yview)

            # Configure Canvas
            canvas.configure(yscrollcommand=scrollbar.set)
            canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

            # Create Canvas frame
            global canvas_frame
            canvas_frame = ttk.Frame(canvas)

            # Toplevel Grid System
            outer_frame.grid(column=1, row=2)
            inner_frame.grid(row=2)
            header.grid(column=0, row=1, pady=15)
            left_btn.grid(column=0, row=4, padx=(140, 0), pady=10)
            right_btn.grid(column=0, row=4, padx=(305, 0))

            canvas.grid()
            canvas_frame.grid()
            canvas.create_window((0, 0), window=canvas_frame, anchor=NW)
            scrollbar.grid(row=0, column=2, sticky=NS)

    def update_login(self):
        """Displays all saved Accounts in a scrollable Toplevel. Allows users to select a single account to update."""
        try:  # Checking for saved data
            data = read_data()
        except FileNotFoundError:  # If no existing data inform user
            messagebox.showerror(title="Account Error", message=f"There are currently no saved Accounts.")
        else:  # If existing data found, retrieve login info using input from account
            self.make_pop_up("Update Login", "the login you would like to update:")
            radio_inputs = [(acc, acc) for acc in accounts]

            global var
            var = StringVar(value=0)
            for option, val in radio_inputs:
                tk.Radiobutton(canvas_frame, text=option, value=val, variable=var, bg=BG_COL, activebackground=BG_COL,
                               font=("Arial", 8, "normal"), pady=6).grid(padx=(30, 0), sticky="w")

            right_btn.config(state=DISABLED)

            while True:
                top.update()  # Refreshes screen
                time.sleep(0.07)  # Time adds a delay based on number inputted (i.e. it suspends execution)
                global selected
                selected = var.get()
                if selected in accounts:
                    right_btn.config(state=NORMAL, command=self.clicked_next)
                    break

    def clicked_next(self):
        # After user selects an account to edit, Toplevel will refresh to prompt user to make their desired changes.
        scrollbar.destroy()
        for widget in outer_frame.winfo_children():
            widget.destroy()

        # self.make_widgets(outer_frame)
        ttk.Label(outer_frame, text=f"{selected} Login Info", font=("Arial", 10, "bold")).grid()
        ttk.Label(outer_frame, text=f"{selected} Login Info", font=("Arial", 10, "bold")).grid(column=1, row=1)
        ttk.Label(outer_frame, text=selected).grid(column=1, row=2)

        user_entry = ttk.Entry(outer_frame)
        user_entry.insert(0, "Hello")
        pass_entry = ttk.Entry(outer_frame)
        pass_entry.insert(0, "Bye")

        user_entry.grid()
        pass_entry.grid()





    # TODO #2: Create Menu Bar for home screen
    def view_all(self):
        print("All Saved Logins")

    def delete_login(self):
        """Displays all saved Accounts in a scrollable Toplevel. Allows users to select an account(s) to delete."""
        # top_wn = make_pop_up("Delete Login", "the login(s) you would like to delete")
        pass


class MenuBar:
    def __init__(self, root, frame):
        self.menu_bar = Menu(root)
        self.make_menu("Edit", 0, 2, False, frame.update_login)
        self.make_menu("View", 2, 5, True, frame.update_login)
        self.make_menu("Help", 5, 8, False, frame.update_login)

        root.config(menu=self.menu_bar)

    def make_menu(self, menu_tab, start, end, tf, cmd):
        tab = Menu(self.menu_bar, tearoff=False)
        count = 0

        try:
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
        else:
            for item in MENU_ITEMS[slice(start, end)]:
                count += 1
                if tf and count == 2:
                    tab.add_separator()
                tab.add_command(label=item, command=cmd)
        finally:
            self.menu_bar.add_cascade(label=menu_tab, menu=tab)

    def update_state(self):
        self.entryconfig("Update Login", state="normal")
        self.entryconfig("Delete Login", state="normal")

        self.entryconfig("View All", state="normal")


