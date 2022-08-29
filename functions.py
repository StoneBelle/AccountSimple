import json
from tkinter import *
from tkinter import messagebox

FONT = "Arial", 8, "bold"
FONT2 = "Courier", 8, "roman"

# Lists for generating password
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def read_data():
    with open("data.json", "r") as data_file:
        data = json.load(data_file)
        return data

#
# def save_login(login):
#     try:  # Read existing file
#         data = read_data()
#     except FileNotFoundError:  # If file not found, make the file
#         with open("data.json", "w") as data_file:
#             json.dump(login, data_file, indent=4)
#     else:  # If file found, update file with new login data
#         with open("data.json", "w") as data_file:
#             data.update(login)
#             json.dump(data, data_file, indent=4)  # Saving updated data to file


def make_radiobutton(root, msg, val):
    var = IntVar()
    Radiobutton(root, text=msg, variable=var, value=val).grid(sticky="w")


def delete_data():
    pass


def update_data():
    top1 = Toplevel()
    top1.title("Update an Account")
    top1.iconbitmap("favicon.ico")
    top1.geometry("800x270")
    frame3 = LabelFrame(top1)
    frame3.pack()
    Label(frame3, text="Select and confirm the account login you would like to update.", font=FONT).grid(sticky="w")


def view_all():
    response = messagebox.askyesno(title="Retrieve All Logins", message="All login data will be shown on screen."
                                                                        "\nIf you would like to proceed press YES.")
    if response == 1:
        # TODO 1: Open JSON dict and convert it to python dict
        try:
            data_dict = read_data()
        except FileNotFoundError:
            messagebox.showerror(title="No Saved Logins", message="No Account Logins have been saved")
        else:
            top2 = Toplevel()
            top2.title("All Accounts")
            top2.iconbitmap("favicon.ico")
            top2.geometry("800x270")

            frame4 = LabelFrame(top2)
            frame4.pack()

            # TODO 2: Retrieve Account keys and store in a tuple that is sorted alphabetically
            account_keys = sorted(tuple(data_dict.keys()))
            Label(frame4, text=f"{len(account_keys)} SAVED LOGIN(S)", font=("Arial", 8, "bold", "underline")) \
                .grid(sticky="w", pady=(0, 15))

            # TODO 3: Retrieve appropriate user & pass data from OG dict for each of the Accounts keys
            for acc in account_keys:
                username = data_dict[acc].get("username")
                password = data_dict[acc].get("password")
                # TODO 4: Create Labels for each Account & its data
                Label(frame4, text=f"ACCOUNT:  {acc}\nUSERNAME: {username}\nPASSWORD: {password}\n\n", justify=LEFT,
                      font=FONT2).grid(sticky="w")

            top2.mainloop()
