from data import *
import tkinter as tk
from tkinter import ttk
from tkinter import *

BG_COL = "#FFFFFF"
OPTNL_BTN = "#EECF7F"
MNDTRY_BTN = "#EF967A"
FONT = "Arial", 8, "bold"
FONT2 = "Courier", 8, "roman"


def make_toplevel(wn_title, msg):
    """Creates a responsive Toplevel window with a Scrollbar. To customize the window fill in all parameters."""
    # Creates a Toplevel with customizable title
    top_wn = tk.Toplevel(pady=10)
    top_wn.title(wn_title)
    top_wn.geometry("450x375")
    top_wn.resizable(True, True)

    # Ensures Toplevel is responsive as window is resized
    top_wn.grid_columnconfigure(0, weight=1)
    top_wn.grid_rowconfigure(0, weight=1)

    # Widgets
    outer_frame = tk.LabelFrame(top_wn, borderwidth=0, highlightthickness=0)
    sub_header = tk.Label(outer_frame, text=msg, font=("Arial", 10, "bold"))
    left_btn = tk.Button(outer_frame, text="Cancel", command=lambda: top_wn.destroy())
    right_btn = tk.Button(outer_frame, text="Next", command=selected)

    # Widgets grid layout
    outer_frame.grid()
    sub_header.grid(column=2, row=1, pady=10)
    left_btn.grid(column=2, row=3, sticky=E, padx=85, pady=(10, 0), ipadx=5)
    right_btn.grid(column=2, row=3, sticky=E, padx=21, ipadx=10, pady=(10, 0))

    global inner_frame
    global scroll_bar
    global canvas_frame

    # Labelframe to hold the Canvas
    inner_frame = tk.LabelFrame(outer_frame, relief=GROOVE)
    inner_frame.grid(column=2, row=2, padx=20)

    # Canvas to attach the Scrollbar
    canvas = tk.Canvas(inner_frame, bg=BG_COL)
    canvas.grid()

    scroll_bar = ttk.Scrollbar(inner_frame, orient="vertical", command=canvas.yview)
    scroll_bar.grid(row=0, column=2, sticky=NS)

    # Configure Canvas
    canvas.configure(yscrollcommand=scroll_bar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # Creates a Frame INSIDE Canvas
    canvas_frame = Frame(canvas, bg=BG_COL)
    canvas_frame.grid()

    # Adds canvas_frame to a window in the Canvas
    canvas.create_window((0, 0), window=canvas_frame, anchor="nw")
    make_radiobutton(canvas_frame)


def make_radiobutton(root):
    """Checks for saved Account data. If data found, Account name(s) will be presented on screen as a Radiobutton."""
    try:
        global data_dict
        data_dict = read_data()
    except FileNotFoundError:
        Label(root, text="No account logins saved.", bg=BG_COL, font=FONT).grid(padx=125, pady=120)
        Button(root, text="Cancel", state=DISABLED).grid(column=1, row=3, sticky=E, padx=80, pady=(10, 0), ipadx=5)
        Button(root, text="Next", state=DISABLED).grid(column=1, row=3, sticky=E, padx=17, ipadx=10, pady=(10, 0))
    else:
        global accounts
        accounts = sorted(tuple(data_dict.keys()))
        radio_vals = [(account, account) for account in accounts]
        global var
        var = StringVar()
        var.set(accounts[0])

        for option, val in radio_vals:
            Radiobutton(root, text=option, variable=var, value=val, bg=BG_COL).grid(padx=40, pady=5, sticky="w")


def update_login():
    make_toplevel("Edit Account Login", "Select the account you would like to edit:")


def delete_login():
    make_toplevel("Delete Account Login", "Select the account you would like to delete:")


def clear_frame(frame):
    scroll_bar.destroy()
    for widgets in frame.winfo_children():
        widgets.destroy()


def selected():
    choice = var.get()
    print(choice)
    print(data_dict)
    print(type(choice))
    print(type(data_dict))

    del data_dict[choice]
    accounts.remove(choice)  # Another alternative: data_dict.pop(choice)
    print(data_dict)
    with open("login_data.json", "w") as data_file:
        data_dict.update(data_dict)  # Updating old data with new data
        json.dump(data_dict, data_file, indent=4)  # Saving updated data
    # canvas_frame.after(3000, clear_frame(canvas_frame))
    inner_frame.update_idletasks()
    Label(canvas_frame, text=f"Are you sure you want to delete\nthe login saved for your {choice} account?").grid()
    # test_wn.destroy()
    # messagebox.askyesno(title="Delete Login", message=f"Delete the login for your {choice} account?")
    # how to refresh the screen in tkinter ??? >>> USE the after method


def view_all():
    try:
        data_dict = read_data()
    except FileNotFoundError:
        view_all_wn = make_toplevel("All Saved Accounts Logins:")
        view_frame = scrollable_frames(view_all_wn, "Below are all your saved account logins:")
        Label(view_frame, text="No account logins saved.", bg=BG_COL, font=FONT).grid(padx=(125), pady=(120))
        Button(view_all_wn, text="Done", state=DISABLED).grid(column=1, row=3, sticky=E, padx=9, ipadx=10, pady=(10, 0))

    else:
        view_all_wn = make_toplevel("All Saved Accounts Logins:")
        view_frame = scrollable_frames(view_all_wn, "Below are all saved account logins:")
        # Retrieves all acc keys from dict & stores in a tuple which is then sorted alphabetically & converted into a list.
        accounts = sorted(tuple(data_dict.keys()))

        # Retrieve appropriate username & password data from original dict
        for account in accounts:
            username = data_dict[account].get("username")
            password = data_dict[account].get("password")

            Label(view_frame, text=f"ACCOUNT:  {account}\nUSERNAME: {username}\nPASSWORD: {password}\n", justify=LEFT,
                  font=FONT2, bg=BG_COL).grid(padx=40, pady=5, sticky="w")

        Button(view_all_wn, text="Done", command=lambda: view_all_wn.destroy()).grid(column=1, row=3, sticky=E, padx=9,
                                                                                     ipadx=10, pady=(10, 0))


# after method lets you call a function after a certain amount of time in milliseconds
def faq():
    pass


class MenuBar:
    def __init__(self, root):
        super().__init__()
        self.menu_bar = Menu(root)
        self.edit_item(update_login, delete_login)
        self.view_item(update_login, delete_login, view_all)
        self.help()
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

    def help(self):
        help_opt = Menu(self.menu_bar, tearoff="off")
        help_opt.add_command(label="Tutorial")
        help_opt.add_separator()
        help_opt.add_command(label="FAQ", command=faq)
        self.menu_bar.add_cascade(label="Help", menu=help_opt)
