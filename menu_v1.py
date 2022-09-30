import tkinter as tk
from tkinter import *


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
        view_menu.add_command(label="Landscape", command=menu_cmd, state=sel_state)
        view_menu.add_command(label="Portrait", command=menu_cmd, state=sel_state)
        view_menu.add_separator()
        view_menu.add_command(label="View All", command=menu_cmd, state=sel_state)
        self.menu_bar.add_cascade(label="View", menu=view_menu)

    def help_menu(self, menu_cmd, sel_state):
        edit_menu = Menu(self.menu_bar, tearoff="off")
        edit_menu.add_command(label="Tutorial", command=menu_cmd, state=sel_state)
        edit_menu.add_command(label="FAQ", command=menu_cmd, state=sel_state)
        self.menu_bar.add_cascade(label="Help", menu=edit_menu)

    def make_menu(self, cmd):
        try:
            read_data()
        except FileNotFoundError:
            self.edit_menu(cmd, "disabled")
            self.view_menu(cmd, "disabled")
            self.help_menu(cmd, "disabled")
        else:
            self.edit_menu(cmd, "normal")
            self.view_menu(cmd, "normal")
            self.help_menu(cmd, "normal")
