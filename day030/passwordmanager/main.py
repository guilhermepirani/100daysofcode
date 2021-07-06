'''A password manager with no encription'''

import json
import pyperclip
import tkinter as tk
from PIL import Image, ImageTk
from random import choice, randint, shuffle
from tkinter import messagebox

# ---------------------------- CONSTANTS ------------------------------- #
LOGO_PATH = 'C:/100daysofcode/day030/passwordmanager/logo.png'
JSON_PATH = 'C:/100daysofcode/day030/passwordmanager/data.json'
DEFAULT_EMAIL = 'dummy@gmail.com'

# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_password():
    '''Returns entry by given website'''

    website = website_entry.get().lower()

    try:
        with open(JSON_PATH, 'r') as fdata:
            data = json.load(fdata)
    except FileNotFoundError:
        messagebox.showerror(title='ERROR', message='No data file found!')
    else:
        if website in data:
            data = data[website]
            messagebox.showinfo(title='Your login info', 
                message=
                f'Website: {website.capitalize()}\n'
                f'Username: {data["username"]}\n'
                f'Password: {data["password"]}\n'
        )
        else:
            messagebox.showerror(title='ERROR', message='No match found!')
    finally:
        website_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)
    password = ''.join(password_list)

    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    '''Confirms proper usage and saves info to data file'''

    website = website_entry.get().lower()
    username = username_entry.get()
    password = password_entry.get()

    # JSON format data
    new_entry = {
        website: {
            'username': username,
            'password': password,
        }
    }

    # Checks if there's any info for that website saved
    try:
        with open(JSON_PATH, 'r') as fdata:
            data = json.load(fdata)
            if website in data:
                messagebox.showwarning(title='WARNING', 
                    message=
                    'You already have a password for that website!\n'
                    'Saving will overwrite it!'
                )
    except FileNotFoundError:
        pass

    # Checks usage and confirm data
    if '' in [website, username, password]:
        messagebox.showerror(title='Oops', message='You must fill all fields')
    else:
        confirmation_popup = messagebox.askokcancel(title='Confirm Info', 
            message=
            f'Website: {website.capitalize()}\n'
            f'Username: {username}\n'
            f'Password: {password}\n'
        )

        # Updates JSON file and clears entries
        if confirmation_popup:
            try:
                with open(JSON_PATH, 'r') as fdata:
                    data = json.load(fdata)
                    data.update(new_entry)
            except FileNotFoundError:
                with open(JSON_PATH, 'w') as fdata:
                    json.dump(new_entry, fdata, indent=4)
            else:
                with open(JSON_PATH, 'w') as fdata:
                    json.dump(data, fdata, indent=4)
            finally:
                website_entry.delete(0, tk.END)
                password_entry.delete(0, tk.END)

# ---------------------------- UI SETUP ------------------------------- #
# Main Window
window = tk.Tk()
window.title('Password Manager')
window.resizable(False, False)
window.config(padx=50, pady=50)

logo_img = Image.open(LOGO_PATH)
ico = ImageTk.PhotoImage(logo_img)
window.wm_iconphoto(False, ico)

# Logo image canvas
logo_png = tk.PhotoImage(file=LOGO_PATH)
canvas = tk.Canvas(width=200, height=200)
canvas.create_image(120, 100, image=logo_png)
canvas.grid(row=0, column=1)

# Labels
website_label = tk.Label(text='Website: ')
website_label.grid(row=1, column=0, sticky='e', pady=2)

username_label = tk.Label(text='Email/Username: ')
username_label.grid(row=2, column=0, sticky='e', pady=2)

password_label = tk.Label(text='Password: ')
password_label.grid(row=3, column=0, sticky='e', pady=2)

# Entries
website_entry = tk.Entry(width=32)
website_entry.grid(row=1, column=1, columnspan=2, sticky='w', pady=2)
website_entry.focus()

username_entry = tk.Entry()
username_entry.grid(row=2, column=1, columnspan=2, sticky='ew', pady=2)
username_entry.insert(0, DEFAULT_EMAIL)

password_entry = tk.Entry(width=32)
password_entry.grid(row=3, column=1, sticky='w', pady=2)

# Buttons
search_button = tk.Button(text='Search', borderwidth=1, command=search_password)
search_button.grid(row=1, column=2, sticky='ew', pady=2)

password_button = tk.Button(text='Generate Password', borderwidth=1, command=generate_password)
password_button.grid(row=3, column=2, sticky='ew', pady=2)

add_button = tk.Button(text='Add', borderwidth=1, command=save_password)
add_button.grid(row=4, column=1, columnspan=2, sticky='ew', pady=2)

window.mainloop()
