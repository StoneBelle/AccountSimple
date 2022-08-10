import json
from tkinter import messagebox, END


def read_data():
    with open("data.json", "r") as data_file:
        data = json.load(data_file)  # Reading old data
    return data


def write_data(new_data):
    with open("data.json", "w") as data_file:
        json.dump(new_data, data_file, indent=4)  # Write new data


def check_exception(name, name2, new_data, data):
    if name in name2.keys():
        messagebox.askyesno(title="Account Login Found", message=f'A login for "{name}" already exists.'
                                                                 f'\nWould you like to view it?')
    else:
        with open("data.json", "w") as data_file:
            data.update(new_data)  # Updating old data with new data
            json.dump(data, data_file, indent=4)  # Saving updated data
        messagebox.showinfo(title="Login Successfully Saved", message=f"Login for {name} was saved.")
