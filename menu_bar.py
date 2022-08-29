from tkinter import *
import json


class MenuBar:
    def __init__(self, root):
        super().__init__()
        self.menu_bar = Menu(root)
        root.config(menu=self.menu_bar)

    def edit_item(self, a_func, b_func):
        edit_opt = Menu(self.menu_bar, tearoff="off")
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            edit_opt.add_command(label="Update Login", command=a_func, state="disabled", activebackground="#f0f0f0")
        else:
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

