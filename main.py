from menu_bar import MenuBar
from functions import *
import random

# GUI CONSTANTS
BG_COL = "#FFFFFF"
OPTIONAL_BTN = "#EECF7F"
MANDATORY_BTN = "#EF967A"
FONT = "Arial", 8, "bold"


# BUTTON FUNCTIONS
def get_login(the_dict):
    user_name = the_dict[acc_entry.get()]["username"]
    pass_word = the_dict[acc_entry.get()]["password"]
    messagebox.showinfo(title=f"{acc_entry.get()} Login", message=f"username: {user_name}\npassword: {pass_word}")


def save_data():
    """Stores inputted login information from entry boxes into a JSON file."""
    all_accounts = {
        acc_entry.get().replace(" ", ""): {
            "username": user_entry.get().replace(" ", ""),
            "password": pass_entry.get().replace(" ", ""),
        }

    }

    if len(acc_entry.get()) == 0 or len(user_entry.get()) == 0 or len(pass_entry.get()) == 0:
        messagebox.showerror(title="Missing Information", message="Please do not leave any fields blank.")
    else:
        try:  # Open existing file


            login_dict = read_data()
        except FileNotFoundError:  # If file not found, make the file
            with open("data.json", "w") as data_file:
                json.dump(all_accounts, data_file, indent=4)
        else:  # If file found, update file with new login data
            if acc_entry.get() in login_dict:
                response = messagebox.askyesno(title="Existing Account Login",
                                               message=f'Login details for "{acc_entry.get()}" already exists'
                                                       f'\nWould you like to view the saved login?')
                if response == 1:
                    get_login(login_dict)
            else:
                with open("data.json", "w") as data_file:
                    login_dict.update(all_accounts)
                    json.dump(login_dict, data_file, indent=4)  # Saving updated data to file

        acc_entry.delete(0, END)
        user_entry.delete(0, END)
        pass_entry.delete(0, END)


def find_data():
    """Check if login data for an Account already exists by typing its name. If found, login data will be returned."""
    try:
        login_dict = read_data()
    except FileNotFoundError:
        messagebox.showerror(title="ERROR - No Saved Accounts", message=f"There are currently no saved Account logins.")
    else:
        if acc_entry.get() in login_dict:
            get_login(login_dict)
        else:
            messagebox.showerror(title="Login Not Found", message=f'No login data for "{acc_entry.get()}" was found.')


def generate_pass():
    """Generates a secure password consisting of a random mix of letters, numbers, and symbols."""
    pass_entry.delete(0, END)
    password = [random.choice(letters) for letter in range(7)]
    password += [random.choice(letters).upper() for letter in range(2)]
    password += [random.choice(numbers) for number in range(4)]
    password += [random.choice(symbols) for symbol in range(2)]
    random.shuffle(password)
    new_password = "".join(password)
    pass_entry.insert(0, new_password)


def portrait_view():
    wn.update_idletasks()
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
wn = Tk()
wn.title("AccountSimple")
wn.iconbitmap("favicon.ico")
wn.config(padx=60, pady=30, bg=BG_COL)

menu_bar = MenuBar(wn)
menu_bar.edit_item(update_data, delete_data)
menu_bar.view_item(portrait_view, landscape_view, view_all)

# WIDGETS
frame1 = LabelFrame(wn, bg=BG_COL, borderwidth=0)
frame2 = LabelFrame(frame1, bg=BG_COL, borderwidth=0)

prompt_label = Label(frame2, text="Find or save your account login using the fields below.", bg=BG_COL, pady=20)

acc_label = Label(frame2, text="Account For:", bg=BG_COL, font=FONT)
user_label = Label(frame2, text="Username:", bg=BG_COL, font=FONT)
pass_label = Label(frame2, text="Password:", bg=BG_COL, font=FONT)

acc_entry = Entry(frame2, width=36, bg=BG_COL)
user_entry = Entry(frame2, width=55, bg=BG_COL)
pass_entry = Entry(frame2, width=36, bg=BG_COL)

find_button = Button(frame2, text="Find Specific Login", command=find_data, width=15, bg=OPTIONAL_BTN)
pass_button = Button(frame2, text="Generate Password", command=generate_pass, width=15, bg=OPTIONAL_BTN)
add_button = Button(frame2, text="Save Login", command=save_data, width=45, bg=MANDATORY_BTN)

# GRID SYSTEM
frame1.pack(padx=(0, 5))
frame2.pack(ipadx=22)
portrait_view()
wn.mainloop()
