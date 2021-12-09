"""A rudimentary password manager app to learn how to read, write, and update files."""
import json
from random import choice, randint, shuffle
from tkinter import (
    END, Button, Canvas, Entry, Label, PhotoImage, Tk, messagebox
)


def validate(password):
    """Check if a password exists in the database already."""
    filepath = "./password-manager-start/data.json"
    try:
        with open(file=filepath, mode="r") as f:
            data = json.load(f)

    except FileNotFoundError:
        return (True, None)

    else:
        for website in data:
            if password == data[website]["password"]:
                return (False, website)

        return (True, None)


def save():
    """Save data to file"""
    filepath = "./password-manager-start/data.json"

    website = website_input.get()
    email = email_label.get()
    password = password_input.get()
    valid = validate(password)
    write = True

    if not valid[0]:
        yes = messagebox.askokcancel(
            title="Error",
            message=f"This password is already being used by {valid[1]}. Do you want to use this pasword or enter a new password."
        )

        if not yes:
            write = False
            password_input.delete(0, END)
            password_input.focus()

    if write:
        new_data = {
            website: {
                "email": email,
                "password": password
            }
        }

        if len(website) == 0 or len(email) == 0 or len(password) == 0:
            messagebox.showerror(
                title="Error", message="Please fill in all fields"
            )

        else:
            ok = messagebox.askokcancel(
                title="Details", message=f"These are the details entered:\nWebsite: {website}\nEmail: {email}\nPassword: {password}\nIs it okay to save?"
            )

            if ok:
                try:
                    with open(file=filepath, mode="r") as f:
                        # Read all data
                        data = json.load(f)
                        # Updata data
                        data.update(new_data)

                except FileNotFoundError:
                    with open(file=filepath, mode="w") as f:
                        json.dump(new_data, f, indent=4)

                else:
                    with open(file=filepath, mode="w") as f:
                        json.dump(data, f, indent=4)

                finally:
                    website_input.delete(0, END)
                    password_input.delete(0, END)


def create():
    """Create random password"""
    letters = [
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
        "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
        "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    l = [choice(letters) for _ in range(randint(8, 10))]
    n = [choice(numbers) for _ in range(randint(2, 4))]
    s = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = l + n + s
    shuffle(password_list)
    password = "".join(password_list)

    while not validate(password)[0]:
        create()
    password_input.delete(0, END)
    password_input.insert(0, password)


def find():
    """Find a particular Website and it's details."""
    filepath = "./password-manager-start/data.json"
    website = website_input.get()

    # Load data
    try:
        with open(file=filepath, mode="r") as f:
            data = json.load(f)

    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No data file found.")

    else:
        if website in data:
            messagebox.showinfo(
                title="Details", message=f"Email: {data[website]['email']}\nPassword: {data[website]['password']}"
            )
        else:
            messagebox.showwarning(
                title="Warning", message=f"No details for {website} exist."
            )


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Buttons
generate = Button(text="Generate Password", command=create)
generate.grid(column=2, row=3)

add = Button(text="Add", width=36, command=save)
add.grid(column=1, row=4, columnspan=2)

search = Button(text="Search", command=find, width=13)
search.grid(column=2, row=1)

# Inputs
website_input = Entry(width=21)
website_input.grid(column=1, row=1)
website_input.focus()

email_label = Entry(width=35)
email_label.grid(column=1, row=2, columnspan=2)
email_label.insert(0, "paritoshpanda21@gmail.com")

password_input = Entry(width=21)
password_input.grid(column=1, row=3)

# Canvas
canvas = Canvas(height=200, width=200)
logo = PhotoImage(file="./password-manager-start/logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

window.mainloop()
