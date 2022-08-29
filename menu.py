import tkinter as tk
from tkinter import ttk
from tkinter import *
from modify_data import *


def delete_login():
    print("delete login")


def landscape_view():
    print("Landscape View")


def portrait_view():
    print("Portrait View")


def view_all():
    print("All Saved Logins")


# TODO #2: Create Menu Bar for home screen

def make_radiobutton(root, name):
    var = StringVar
    ttk.Radiobutton(root, text=name, value=name, variable=var)


def make_pop_up():
    # Creates a Toplevel with customizable title & size
    print("Edit Login")
    top = Toplevel(bg=BG_COL)
    top.title("Update Login")
    # top.geometry("450x375")
    top.resizable(True, True)

    # ttk Widget Styles
    style = ttk.Style()
    style.configure("Left.TButton", foreground="red")
    print(style.lookup("TFrame", "background"))  # Checks for current style applied. Takes 2 parameters: name & widget
    print(style.theme_names())  # Shows the different styles available in the OS.

    # Ensures Toplevel is responsive as window is resized
    top.grid_columnconfigure(0, weight=1)
    top.grid_rowconfigure(0, weight=1)
    top.grid_columnconfigure(5, weight=1)
    top.grid_rowconfigure(5, weight=1)


    # Make Frames inside the Toplevel
    outer_frame = ttk.Frame(top)
    inner_frame = ttk.Frame(outer_frame)

    # Toplevel Widgets
    header = ttk.Label(outer_frame, text="Select the login you would like to update:")
    left_btn = ttk.Button(outer_frame, text="Cancel", style="Left.TButton")
    right_btn = ttk.Button(outer_frame, text="Next", style="Right.TButton")

    # Create Canvas & Scrollbar, then attach Scrollbar to Canvas
    canvas = tk.Canvas(inner_frame, bg=BG_COL)
    scrollbar = ttk.Scrollbar(inner_frame, orient="vertical", command=canvas.yview)

    # Configure Canvas
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # Create Canvas frame???
    canvas_frame = ttk.Frame(canvas)


    # Grid System
    outer_frame.grid(column=1, row=2)
    inner_frame.grid(row=2)

    header.grid(column=0, row=1, pady=15)
    left_btn.grid(column=0, row=4, padx=(140, 0), pady=10)
    right_btn.grid(column=0, row=4, padx=(305, 0))

    canvas.grid()
    canvas_frame.grid()
    canvas.create_window((0, 0), window=canvas_frame, anchor=NW)
    scrollbar.grid(row=0, column=2, sticky=NS)

    # TODO:  Retrieve all Account names from saved data and store in a list
    # TODO:  Covert Account list into a sorted tuple
    # TODO:  Create a radiobutton for each of the sorted Account names
    # TODO:  Configure selected radiobutton to be bolded if selected
    # TODO:  Store selected radiobutton in a variable

    for text in range(10):
        # ttk.Label(canvas_frame, text="Hello").grid(padx=(50, 0), pady=5)
        pass


class MenuBar:
    def __init__(self, root):
        self.menu_bar = Menu(root)
        self.edit_item(make_pop_up, delete_login)
        self.view_item(landscape_view, portrait_view, view_all)
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
