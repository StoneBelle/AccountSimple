from data import *
import tkinter as tk
from tkinter import ttk
from tkinter import *

BG_COL = "#FFFFFF"
OPTNL_BTN = "#EECF7F"
MNDTRY_BTN = "#EF967A"
FONT = "Arial", 8, "bold"
FONT2 = "Courier", 8, "roman"

#window.update_idletasks()
#https://www.tutorialspoint.com/how-do-i-get-an-event-callback-when-a-tkinter-entry-widget-is-modified#:~:text=Callback%20functions%20in%20Tkinter%20are,that%20stores%20the%20user%20input.
# https://www.tutorialspoint.com/python/tk_toplevel.htm

class MenuBar(tk.Frame):

    def __init__(self, root):
        super(MenuBar, self).__init__()
        self.menu_bar = Menu(root)
        self.edit_item(self.update_login, self.delete_login)
        self.view_item(self.update_login, self.delete_login, self.view_all)

        # self.help()
        root.config(menu=self.menu_bar)

        # Attributes for pop-up windows
        self.top_wn = tk.Toplevel(pady=10)
        self.outer_frame = tk.LabelFrame(self.top_wn, borderwidth=0, highlightthickness=0)
        self.inner_frame = tk.LabelFrame(self.outer_frame, relief=GROOVE)
        self.canvas = tk.Canvas(self.inner_frame, bg=BG_COL)
        self.scroll_bar = ttk.Scrollbar(self.inner_frame, orient="vertical", command=self.canvas.yview)
        self.canvas_frame = Frame(self.canvas, bg=BG_COL)

        # self.top_wn.withdraw()

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

    #
    # def help(self):
    #     help_opt = Menu(self.menu_bar, tearoff="off")
    #     help_opt.add_command(label="Tutorial")
    #     help_opt.add_separator()
    #     help_opt.add_command(label="FAQ", command=faq)
    #     self.menu_bar.add_cascade(label="Help", menu=help_opt)

    def make_radiobutton(self, root):
        """Checks for saved Account data. If data found, Account name(s) are presented on screen as a Radiobutton(s)."""
        try:
            self.data_dict = read_data()
        except FileNotFoundError:
            tk.Label(root, text="No account logins saved.", bg=BG_COL, font=FONT).grid(padx=125, pady=120)
            tk.Button(root, text="Cancel", state=DISABLED).grid(column=1, row=3, sticky=E, padx=80, pady=(10, 0), ipadx=5)
            tk.Button(root, text="Next", state=DISABLED).grid(column=1, row=3, sticky=E, padx=17, ipadx=10, pady=(10, 0))
        else:
            global accounts
            accounts = sorted(tuple(self.data_dict.keys()))
            radio_vals = [(account, account) for account in accounts]
            global var
            var = StringVar()
            var.set(accounts[0])

            for option, val in radio_vals:
                Radiobutton(root, text=option, variable=var, value=val, bg=BG_COL).grid(padx=40, pady=5, sticky="w")

        left_btn = tk.Button(self.outer_frame, text="Cancel", command=lambda: self.top_wn.destroy())
        right_btn = tk.Button(self.outer_frame, text="Next", command=self.selected)
    def make_toplevel(self, wn_title, msg):
        """Creates a responsive Toplevel window with a Scrollbar. To customize the window fill in all parameters."""
        # Creates a Toplevel with customizable title
        self.top_wn.title(wn_title)
        self.top_wn.geometry("450x375")
        self.top_wn.resizable(True, True)

        # Ensures Toplevel is responsive as window is resized
        self.top_wn.grid_columnconfigure(0, weight=1)
        self.top_wn.grid_rowconfigure(0, weight=1)

        # Widgets
        sub_header = tk.Label(self.outer_frame, text=msg, font=("Arial", 10, "bold"))


        # Widgets grid layout
        self.outer_frame.grid()
        sub_header.grid(column=2, row=1, pady=10)

        # Labelframe to hold the Canvas
        self.inner_frame.grid(column=2, row=2, padx=20)

        # Canvas to attach the Scrollbar
        self.canvas.grid()
        self.scroll_bar.grid(row=0, column=2, sticky=NS)

        # Configure Canvas
        self.canvas.configure(yscrollcommand=self.scroll_bar.set)
        self.canvas.bind('<Configure>', lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        # Creates a Frame INSIDE Canvas
        self.canvas_frame.grid()

        # Adds canvas_frame to a window in the Canvas
        self.canvas.create_window((0, 0), window=self.canvas_frame, anchor="nw")
        self.make_radiobutton(self.canvas_frame)

    def update_login(self):
        self.make_toplevel("Edit Account Login", "Select the account you would like to edit:")

    def delete_login(self):
        self.make_toplevel("Delete Account Login", "Select the account you would like to delete:")

    def view_all(self):
        print("This is view all function.")

    def selected(self):

        choice = var.get()

        del self.data_dict[choice]
        accounts.remove(choice)  # Another alternative: data_dict.pop(choice)
        with open("login_data.json", "w") as data_file:
            self.data_dict.update(self.data_dict)  # Updating old data with new data
            json.dump(self.data_dict, data_file, indent=4)  # Saving updated data
        # canvas_frame.after(3000, clear_frame(canvas_frame))
        self.refresh(self.canvas_frame)
        Label(self.canvas_frame, text=f"Are you sure you want to delete\nthe login saved for your {choice} account?").grid()
        # test_wn.destroy()
        # messagebox.askyesno(title="Delete Login", message=f"Delete the login for your {choice} account?")
        # how to refresh the screen in tkinter ??? >>> USE the after method

    def refresh(self, frame):
        self.scroll_bar.destroy()
        for widgets in frame.winfo_children():
            widgets.destroy()
