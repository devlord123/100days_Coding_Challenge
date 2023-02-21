
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle

import json



# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_letter + password_symbols + password_numbers
    shuffle(password_list)
    gen_pas = "".join(password_list)
    password.insert(0, gen_pas)
    #pyperclip.copy(gen_pas)
    
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    web = website.get()
    em = email.get()
    pas = password.get()

    new_data = {
        web : {
            "email": em,
            "password": pas,
        }
    }

    if len(web) == 0 or len(pas) == 0:
        messagebox.askretrycancel(title="No input", message="You cant leave any input empty.")
    else:
        try:
            with open("data.json", "r") as df:
                #Load an existing data
                data = json.load(df)

        except FileNotFoundError:
            #If not found, create it and input the new data
            with open("data.json", "w") as df:
                json.dump(new_data, df, indent=4)
        else:
            #If found, update and dump it.
            data.update(new_data)
            with open("data.json", "w") as df:
                json.dump(data, df, indent=4)
        finally:
            password.delete(0, END)
            website.delete(0, END)
# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    name = website.get().title()
    if len(name) <= 0:
        messagebox.showinfo(title="Empty Search", message="Search Cannot Be Empty")
    else:
        try:
            with open("data.json", "r") as df:
                data = json.load(df)
        except FileNotFoundError:
            messagebox.showerror(title="Error", message="No Data File Found")
        else:
            try:
                if data[name]:
                    messagebox.showinfo(title="Search Found", message=f"Email: {data[name]['email']}\nPassword:\
                    {data[name]['password']}")
            except KeyError:
                messagebox.showerror(title="Error", message="No Data File Found")




# ---------------------------- UI SETUP ------------------------------- #
windows = Tk()
windows.title("Password Manager")
windows.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)


website_label = Label(text="Website", font=("Arial", 10, "normal"))
website_label.grid(column=0, row=2)
website = Entry(width=30)
website.grid(column=1, row=2)
website.focus()
search_btn = Button(text="Search", width=12, command=find_password)
search_btn.grid(column=2, row=2)


email_label = Label(text="Email/Username", font=("Arial", 10, "normal"))
email_label.grid(column=0, row=1)
email = Entry(width=45)
email.grid(column=1, columnspan=2, row=1)
email.insert(0, "owoyemiidrisolamilekan@gmail.com")





password_label = Label(text="Password", font=("Arial", 10, "normal"))
password_label.grid(column=0, row=3)
password = Entry(width=29)
password.grid(column=1, row=3)


generate = Button(text="Generate Password", font=("Arial", 10, "normal"), width=14, command=generate_password)
generate.grid(column=2, row=3)

add = Button(text="ADD", font=("Arial", 10, "normal"), width=34,command=save)
add.grid(column=1, columnspan=2, row=4)


windows.mainloop()