import json
from tkinter import messagebox, END

# GUI CONSTANTS
BG_COL = "#FFFFFF"
FONT = "Arial", 8, "bold"


# TODO #3: Create JSON  functions to read, write, and update data

def read_data():
    with open("data.json", "r") as data_file:
        data = json.load(data_file)  # Reading old data
    return data


def write_data(new_data):
    with open("data.json", "w") as data_file:
        json.dump(new_data, data_file, indent=4)  # Saves new data in JSON file


def update_data(file, new_data):
    with open("data.json", "w") as data_file:
        file.update(new_data)  # Updates old data with new data
        json.dump(file, data_file, indent=4)  # Saves updated data in JSON file


def check_exception(name, name2, new_data, data):
    if name in name2.keys():
        messagebox.askyesno(title="Account Login Found", message=f'A login for "{name}" already exists.'
                                                                 f'\nWould you like to view it?')
    else:
        with open("data.json", "w") as data_file:
            data.update(new_data)  # Updating old data with new data
            json.dump(data, data_file, indent=4)  # Saving updated data
        messagebox.showinfo(title="Login Successfully Saved", message=f"Login for {name} was saved.")


def update_label(entry_input, label):
    """Updates the Label widget."""
    if len(entry_input) == 0:
        label.config(foreground="red")
    else:
        label.config(foreground="black")


def update_button(entry_input, label):
    """Updates the state of a Button widget."""
    if len(entry_input) == 0:
        label.config(foreground="red")
    else:
        label.config(foreground="black")

