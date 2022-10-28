import random
from modify_data import *
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *

# Password Components
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

MENU_ITEMS = ("Update Login", "Delete Login", "Portrait View", "Landscape View", "View All", "Tutorial", "FAQ")
DISABLE_STATE = ("Update Login", "Delete Login", "View All")


class AppWindow(tk.Tk):
    """Class that inherits tk.Tk to create a window object."""

    def __init__(self, title):
        super().__init__()
        self.config(bg=BG_COL, padx=100, pady=30)
        self.title(title)
        self.geometry("850x430")

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
        style.configure("TRadiobutton", background=BG_COL)
        style.configure("TLabel", background=BG_COL, foreground="#787878", font=text_font)
        style.configure("Header.TLabel", background=BG_COL, foreground="#000000", font=header_font)

        # print(style.lookup("TFrame", "background"))  # Checks current style applied. Takes 2 parameters: name & widget
        # print(style.theme_names())  # Shows different styles available in the OS.
        self.make_widgets(self)
        self.grid()

    def make_widgets(self, wn):
        # global scope for selected widgets which will be used in other methods
        global acc_entry
        global user_entry
        global pass_entry
        global acc_label
        global user_label
        global pass_label

        # ttk Widgets
        prompt_label = ttk.Label(wn, style="Header.TLabel", text="Save or find your Account login below.")
        acc_label = ttk.Label(wn, text="ACCOUNT")
        user_label = ttk.Label(wn, text="USERNAME")
        pass_label = ttk.Label(wn, text="PASSWORD")

        acc_entry = ttk.Entry(wn, width=36)
        user_entry = ttk.Entry(wn, width=56)
        pass_entry = ttk.Entry(wn, width=36)  # to hide password char use: show="*"

        find_button = ttk.Button(wn, text="Find Login", width=17, command=self.find_login)
        pass_button = ttk.Button(wn, text="Generate Password", width=17, command=self.make_password)
        add_button = ttk.Button(wn, text="Save", width=12, command=self.save_login)

        # Widget grid
        prompt_label.grid(column=3, columnspan=2, row=1, pady=(15, 40))
        acc_label.grid(column=3, row=2, padx=(0, 165), pady=5)
        user_label.grid(column=3, row=4, padx=(0, 160), pady=(30, 7))
        pass_label.grid(column=3, row=6, padx=(0, 160), pady=(30, 7))

        acc_entry.grid(column=3, row=3, ipady=2)
        user_entry.grid(column=3, columnspan=2, row=5, ipady=2, padx=(0, 7))
        pass_entry.grid(column=3, row=7, ipady=2)

        find_button.grid(column=4, row=3, padx=8)
        pass_button.grid(column=4, row=7, padx=8)
        add_button.grid(column=4, row=8, padx=(22, 0), pady=30)

    def find_login(self):
        """Retrieves user input from the account entrybox and checks for a login saved under that name. User will be
        notified via a messagebox on whether a login exists."""

        account = acc_entry.get().strip()
        try:  # Checking for saved data
            data = read_data()
        except FileNotFoundError:  # If no existing data inform user
            messagebox.showerror(title="Account Error", message=f"There are currently no saved Accounts.")
        else:  # If existing data found, retrieve login info using input from account
            if account in data.keys():
                saved_user = data[account]["username"]
                saved_pass = data[account]["password"]
                messagebox.showinfo(title="Account Login Retrieved",
                                    message=f'"{account}" Login Found:\n\nUsername:  {saved_user}'
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

    def make_password(self):
        """Generates a password composed of 15 randomized characters."""
        pass_entry.delete(0, END)
        pass_requirements = [random.choice(letters) for x in range(7)]
        pass_requirements += [random.choice(letters).upper() for x in range(2)]
        pass_requirements += [random.choice(numbers) for x in range(4)]
        pass_requirements += [random.choice(symbols) for x in range(2)]
        random.shuffle(pass_requirements)
        generated_pass = "".join(pass_requirements)
        pass_entry.insert(0, generated_pass)
        print(pass_requirements)

    def make_pop_up(self, title):
        """Creates a customizable Toplevel if there is existing data is found. Returns the canvas frame to be used as
        the root for new widgets."""
        try:
            data = read_data()
        except FileNotFoundError:
            messagebox.showerror(title="No Accounts Saved", message="There are currently no Account logins saved.")
        else:
            # Retrieves Account names from saved data and stores it in an alphabetically sorted list called "accounts"
            global accounts
            accounts = sorted(data.keys())
            print(type(accounts))

            # Creates a Toplevel with customizable title & size
            global top
            top = tk.Toplevel(bg=BG_COL)
            top.title(title)
            top.resizable(True, True)
            top.geometry("700x395")

            # Ensures Toplevel is responsive as window is resized
            top.grid_columnconfigure(0, weight=1)
            top.grid_rowconfigure(0, weight=1)
            top.grid_columnconfigure(5, weight=1)
            top.grid_rowconfigure(5, weight=1)

    def make_scrollbar(self, text, cmd):
        # Toplevel Frames
        global outer_frame
        global inner_frame
        outer_frame = ttk.Frame(top)
        inner_frame = ttk.Frame(outer_frame)

        # Toplevel Widgets
        global header
        global left_btn
        global right_btn

        header = ttk.Label(outer_frame, style="Header.TLabel", text=f"Select {text}")
        left_btn = ttk.Button(outer_frame, text="Cancel", style="Left.TButton", command=top.destroy)
        right_btn = ttk.Button(outer_frame, text="Next", style="Right.TButton", command=cmd)

        # Canvas & Scrollbar
        canvas = tk.Canvas(inner_frame, bg=BG_COL, width=500, highlightthickness=0, relief=SUNKEN)
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
        left_btn.grid(column=0, row=6, padx=(280, 0), pady=10)
        right_btn.grid(column=0, row=6, padx=(445, 0))

        canvas.grid()
        canvas_frame.grid()
        canvas.create_window((0, 0), window=canvas_frame, anchor=NW)
        scrollbar.grid(row=0, column=2, sticky=NS)

    def make_radio_buttons(self):
        radio_inputs = [(acc, acc) for acc in accounts]

        global var
        var = StringVar(value=0)
        for option, val in radio_inputs:
            acc_option = ttk.Radiobutton(canvas_frame, text=option, value=val, variable=var)
            acc_option.grid(padx=(55, 0), pady=12, sticky="w")

    def sel_radio_btn(self):
        global selected
        selected = var.get()
        """Takes user to next screen if a radiobutton was selected, otherwise a user prompt will be shown. """
        if selected in accounts:
            self.clicked_next()
            header.config(foreground="#000000", font=header_font)

        else:
            header.config(text="You must select an account to proceed.", foreground="#e62315", font=header_font)

    def update_login(self):
        """Displays all saved Accounts in a scrollable Toplevel. Allows users to select a single account to update."""
        self.make_pop_up("Update Login")
        self.make_scrollbar("the login you would like to update:", self.sel_radio_btn)
        self.make_radio_buttons()

    def clicked_next(self):
        # After user selects an account to update, Toplevel will refresh to prompt user to make their desired changes.
        for widget in inner_frame.winfo_children():
            widget.destroy()

        data = read_data()
        # TODO: Find login data for selected account
        if selected in data.keys():
            saved_user = data[selected]["username"]
            saved_pass = data[selected]["password"]
        header.config(text=f'"{selected}" Login Information')

        # left_btn.config(text="Back", command=self.clear_pop_up)
        right_btn.config(text="Update", command=self.save_changes)
        # TODO: Create a command to check for changes. If changes made, save updated info
        global acc_entry
        global user_entry
        global pass_entry
        acc_entry = ttk.Entry(outer_frame, width=55)
        user_entry = ttk.Entry(outer_frame, width=55)
        pass_entry = ttk.Entry(outer_frame, width=55)
        acc_label = ttk.Label(outer_frame, text="ACCOUNT")
        user_label = ttk.Label(outer_frame, text="USERNAME")
        pass_label = ttk.Label(outer_frame, text="PASSWORD")

        # TODO: Display login data within entrybox
        acc_entry.insert(0, f"{selected}")
        user_entry.insert(0, f"{saved_user}")
        pass_entry.insert(0, f"{saved_pass}")
        acc_entry.focus_set()  # Automatically sets cursor on desired entry box so user does not need to click a box

        # TODO: Add appropriate widgets to screen
        # left_btn.grid(column=0, row=1, padx=(90, 0), pady=(10, 0))
        header.grid(column=0, row=0, pady=(20, 275))
        right_btn.grid(column=0, row=0, padx=(255, 0), pady=(330, 0))
        acc_label.grid(column=0, row=0, padx=(0, 280), pady=(0, 170))
        user_label.grid(column=0, row=0, padx=(0, 277), pady=(0, 15))
        pass_label.grid(column=0, row=0, padx=(0, 275), pady=(155, 0))
        acc_entry.grid(column=0, row=0, pady=(0, 120))
        user_entry.grid(column=0, row=0, pady=(45, 0), ipady=2)
        pass_entry.grid(column=0, row=0, pady=(215, 0), ipady=2)

    def refresh_wn(self):
        top.destroy()
        self.destroy()
        self.make_widgets(self)

    def save_changes(self):
        # TODO: Get info from entrybox and check if info is the same as what is already saved
        accinfo = acc_entry.get().strip()
        userinfo = user_entry.get().replace(" ", "")
        passinfo = pass_entry.get().replace(" ", "")

        changed_data = {
            accinfo: {
                "username": userinfo,
                "password": passinfo
            }
        }
        # TODO: If info is the same inform & prompt user to make changes

        data = read_data()
        print(data) # python dict before pop method
        # TODO: if changes made, add new entry into json file and delete old login using pop method
        data.pop(selected)
        update_data(data, changed_data)
        print(data) # python dict after pop method
        print(accinfo)


        # TODO: Change "cancel" button to "back" button & call previous screen
        header.config(text="Success! The following changes have been saved.")
        right_btn.config(text="Exit", command=top.destroy)



    def clear_pop_up(self):
        for widget in inner_frame.winfo_children():
            widget.destroy()

        self.make_scrollbar("the login you would like to update:")
        self.make_radio_buttons()

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
        self.make_menu(frame)
        root.config(menu=self.menu_bar)

    def edit_menu(self, menu_cmd, sel_state):
        edit_menu = Menu(self.menu_bar, tearoff="off")
        edit_menu.add_command(label="Update Login", command=menu_cmd, state=sel_state)
        edit_menu.add_command(label="Delete Login", command=menu_cmd, state=sel_state)
        self.menu_bar.add_cascade(label="Edit", menu=edit_menu)

    def view_menu(self, menu_cmd, sel_state):
        view_menu = Menu(self.menu_bar, tearoff="off")
        # view_menu.add_command(label="Small", command=menu_cmd, state=sel_state)
        # view_menu.add_command(label="Medium", command=menu_cmd, state=sel_state)
        # view_menu.add_separator()
        view_menu.add_command(label="View All", command=menu_cmd, state=sel_state)
        self.menu_bar.add_cascade(label="View", menu=view_menu)

    def make_menu(self, cmd):
        try:
            read_data()
        except FileNotFoundError:
            self.edit_menu(cmd, "disabled")
            self.view_menu(cmd, "disabled")
        else:
            self.edit_menu(cmd, "normal")
            self.view_menu(cmd, "normal")
