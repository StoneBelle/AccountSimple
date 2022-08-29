import tkinter as tk
from tkinter import END, messagebox
from menu_bar import MenuBar
import json
from functions import *

# GUI CONSTANTS
BG_COL = "#FFFFFF"
OPTIONAL_BTN = "#EECF7F"
MANDATORY_BTN = "#EF967A"
FONT = "Arial", 8, "bold"


# BUTTON FUNCTIONS
def save_data():
    all_accounts = {
        acc_entry.get(): {
            "username": user_entry.get(),
            "password": pass_entry.get(),
        }

    }

    if len(acc_entry.get()) == 0 or len(user_entry.get()) == 0 or len(pass_entry.get()) == 0:
        messagebox.showerror(title="Missing Information", message="Please do not leave any fields blank.")

    else:
        save_login(all_accounts)
        acc_entry.delete(0, END)
        user_entry.delete(0, END)
        pass_entry.delete(0, END)


def find_data():
    """Enter an account name to check if its login data already exists. If found, login data will be returned."""
    try:
        with open("data.json", "r") as data_file:
            login_dict = json.load(data_file)
    except FileNotFoundError:
        tk.messagebox.showerror(title="Error - File Not Found",
                                message=f"No login data for {acc_entry.get()} was found.")
    else:
        if acc_entry.get() in login_dict:
            user_name = login_dict[acc_entry.get()]["username"]
            pass_word = login_dict[acc_entry.get()]["password"]
            tk.messagebox.showinfo(title=f"{acc_entry.get()} Login",
                                   message=f"username: {user_name}\npassword: {pass_word}")
        else:  # If the dict key (i.e. acc_name) does not exist within the json file (i.e. KeyError)
            tk.messagebox.showerror(title="File Not Found", message=f'No login data for "{acc_entry.get()}" was found.')

def generate_pass():
    pass_entry.delete(0, END)
    password = [random.choice(letters) for letter in range(7)]
    password += [random.choice(letters).upper() for letter in range(2)]
    password += [random.choice(numbers) for number in range(4)]
    password += [random.choice(symbols) for symbol in range(2)]
    random.shuffle(password)
    new_password = "".join(password)
    pass_entry.insert(0, new_password)

def update_data():
    pass


def delete_data():
    pass


def portrait_view():
    wn.update_idletasks()
    logo_label.grid(column=3, columnspan=2, row=0)
    prompt_label.grid(column=3, columnspan=2, row=1, rowspan=2, pady=(0, 20))
    acc_label.grid(column=2, row=2, padx=(0, 15), pady=(50, 0))
    user_label.grid(column=2, row=3, padx=(0, 9))
    pass_label.grid(column=2, row=4, padx=(0, 9), pady=(0, 50))

    acc_entry.grid(column=3, row=2, pady=(50, 6), ipady=2)
    user_entry.grid(column=3, columnspan=2, row=3, ipady=2)
    pass_entry.grid(column=3, row=4, pady=(6, 50), ipady=2)

    acc_entry.grid(column=3, row=2, ipady=3)
    user_entry.grid(column=3, columnspan=2, row=3, ipady=3, ipadx=4)
    pass_entry.grid(column=3, row=4, ipady=3)

    find_button.grid(column=4, row=2, padx=(5, 0), pady=(50, 7))
    pass_button.grid(column=4, row=4, padx=(5, 0), pady=(5, 50))
    add_button.grid(column=3, columnspan=2, row=4, pady=(20, 0), ipadx=9)


def landscape_view():
    wn.geometry("800x270")
    logo_label.grid(column=0, row=0, rowspan=6, pady=(0, 20))
    prompt_label.grid(column=3, columnspan=2, row=1, rowspan=2, pady=(0, 20))
    acc_label.grid(column=2, row=2, padx=(0, 15), pady=(50, 0))
    user_label.grid(column=2, row=3, padx=(0, 9))
    pass_label.grid(column=2, row=4, padx=(0, 9), pady=(0, 50))

    acc_entry.grid(column=3, row=2, pady=(50, 6), ipady=2)
    user_entry.grid(column=3, columnspan=2, row=3, ipady=2)
    pass_entry.grid(column=3, row=4, pady=(6, 50), ipady=2)

    acc_entry.grid(column=3, row=2, ipady=3)
    user_entry.grid(column=3, columnspan=2, row=3, ipady=3, ipadx=4)
    pass_entry.grid(column=3, row=4, ipady=3)

    find_button.grid(column=4, row=2, padx=(5, 0), pady=(50, 7))
    pass_button.grid(column=4, row=4, padx=(5, 0), pady=(5, 50))
    add_button.grid(column=3, columnspan=2, row=4, pady=(20, 0), ipadx=9)


# SCREEN SETUP
wn = tk.Tk()
wn.title("AccountSimple")
wn.iconbitmap("favicon.ico")
wn.config(padx=60, pady=30, bg=BG_COL)

menu_bar = MenuBar(wn)
menu_bar.edit_item(update_data, delete_data)
menu_bar.view_item(portrait_view, landscape_view, view_all)


# WIDGETS
frame1 = tk.LabelFrame(wn, bg=BG_COL, borderwidth=0)
frame2 = tk.LabelFrame(frame1, bg=BG_COL, borderwidth=0)

# r = IntVar()
#
# Radiobutton(frame2, text="Account1", variable=r, value=1).grid()
# Radiobutton(frame2, text="Account2", variable=r, value=2).grid()

logo_img = tk.PhotoImage(file="../AccountSimple3/logo.png")
logo_label = tk.Label(frame2, image=logo_img, bg=BG_COL)
prompt_label = tk.Label(frame2, text="Find or save your account login using the fields below.", bg=BG_COL, pady=20)

acc_label = tk.Label(frame2, text="Account For:", bg=BG_COL, font=FONT)
user_label = tk.Label(frame2, text="Username:", bg=BG_COL, font=FONT)
pass_label = tk.Label(frame2, text="Password:", bg=BG_COL, font=FONT)

acc_entry = tk.Entry(frame2, width=36, bg=BG_COL)
user_entry = tk.Entry(frame2, width=55, bg=BG_COL)
pass_entry = tk.Entry(frame2, width=36, bg=BG_COL)

find_button = tk.Button(frame2, text="Find Data", command=find_data, width=15, bg=OPTIONAL_BTN)
pass_button = tk.Button(frame2, text="Generate Password", command=generate_pass, width=15, bg=OPTIONAL_BTN)
add_button = tk.Button(frame2, text="Save Account Data", command=save_data, width=45, bg=MANDATORY_BTN)

# GRID SYSTEM
frame1.pack(padx=(0, 5))
frame2.pack(ipadx=22)
portrait_view()
wn.mainloop()

