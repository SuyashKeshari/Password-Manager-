import json
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    enter_password.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = enter_website.get()
    email = enter_email.get()
    password = enter_password.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any field empty")
    else:
        try:
            with open("data.json", mode="r") as data_file:
                # Reading Old Data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        except json.decoder.JSONDecodeError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating Old Data With New Data
            data.update(new_data)
            with open("data.json", mode="w") as data_file:
                # Saving Updated Data
                json.dump(data, data_file, indent=4)
        finally:
            enter_website.delete(0, END)
            enter_password.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = enter_website.get().title()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found")
    else:
        if website in data:
            user_email = data[website]["email"]
            user_password = data[website]["password"]
            messagebox.showinfo(title="Details", message=f"Email: {user_email}\nPassword:{user_password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
enter_website = Entry(width=35)
enter_website.focus()
enter_website.grid(column=1, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
enter_email = Entry(width=35)
enter_email.insert(0,"rajeev@gmail.com")
enter_email.grid(column=1, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
enter_password = Entry(width=21)
enter_password.grid(column=1, row=3)

add_button = Button(text="Add", highlightthickness=0, width=36, command=save)
add_button.grid(column=1, row=4)

generate_button = Button(text="Generate Password", command= generate_password)
generate_button.grid(column=2, row=3)


search_button = Button(text="Search", command=find_password)
search_button.grid(column=2, row=1, )

window.mainloop()


