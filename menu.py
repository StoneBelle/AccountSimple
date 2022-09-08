import tkinter as tk
from tkinter import ttk
from tkinter import *
from turtle import update
import time
from modify_data import *


# TODO #2: Create Menu Bar for home screen
def view_all():
    print("All Saved Logins")


def delete_login():
    """Displays all saved Accounts in a scrollable Toplevel. Allows users to select an account(s) to delete."""
    top_wn = make_pop_up("Delete Login", "the login(s) you would like to delete")


def make_pop_up(title, text):
    """Creates a customizable Toplevel if saved data is found. Returns the canvas frame to be used as the root for
    customizable widgets."""
    try:
        data = read_data()
    except FileNotFoundError:
        messagebox.showerror(title="No Accounts Saved", message="There are currently no Account logins saved.")
    else:
        # Retrieves Account names from saved data and stores it in a alphabetically sorted list called "accounts"
        global accounts
        accounts = sorted(tuple(data.keys()))
        # Creates a Toplevel with customizable title & size
        print("Edit Login")
        global top
        top = Toplevel(bg=BG_COL)
        top.title(title)
        top.resizable(True, True)
        top.geometry("400x365")

        # Ensures Toplevel is responsive as window is resized
        top.grid_columnconfigure(0, weight=1)
        top.grid_rowconfigure(0, weight=1)
        top.grid_columnconfigure(5, weight=1)
        top.grid_rowconfigure(5, weight=1)

        # Toplevel Frames
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


def update_login():
    """Displays all saved Accounts in a scrollable Toplevel. Allows users to select a single account to update."""
    make_pop_up("Update Login", "the login you would like to update:")
    radio_inputs = [(acc, acc) for acc in accounts]
    global var
    var = StringVar(value=0)
    r_btn = 0
    for option, val in radio_inputs:
        tk.Radiobutton(canvas_frame, text=option, value=val, variable=var, bg=BG_COL, activebackground=BG_COL,
                       font=("Arial", 8, "normal"), pady=6).grid(padx=(30, 0), sticky="w")

    right_btn.config(state=DISABLED)

    while True:
        top.update()  # Refreshes screen
        time.sleep(0.07)  # Time adds a delay based on number inputted (i.e. it suspends execution)

        selected = var.get()
        if selected in accounts:
            right_btn.config(state=NORMAL)
            break
    header.config(text="Fill in the fields below to update your account ")
    scrollbar.destroy()
    for widget in canvas_frame.winfo_children():
        widget.destroy()


class MenuBar:
    def __init__(self, root):
        self.menu_bar = Menu(root)
        self.edit_item(update_login, delete_login)
        self.view_item(update_login, update_login, view_all)
        root.config(menu=self.menu_bar)

    def edit_item(self, a_func, b_func):
        edit_opt = Menu(self.menu_bar, tearoff="off")
        edit_opt.add_command(label="Update Login", command=a_func)
        edit_opt.add_separator()
        edit_opt.add_command(label="Delete Login", command=b_func)
        self.menu_bar.add_cascade(label="Edit", menu=edit_opt)

    def view_item(self, a_func, b_func, c_func):
        view_opt = Menu(self.menu_bar, tearoff="off")
        view_opt.add_command(label="Portrait View", command=a_func)
        view_opt.add_command(label="Landscape View", command=b_func)
        view_opt.add_separator()
        view_opt.add_command(label="View All Saved Accounts", command=c_func)
        self.menu_bar.add_cascade(label="View", menu=view_opt)

