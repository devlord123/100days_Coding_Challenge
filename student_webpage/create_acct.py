from tkinter import *
from tkinter import messagebox
from auth import save_user
from login import login



def create_acct():

    windows = Tk()
    windows.geometry("500x500")
    windows.title("Create an Account")
    windows.config(pady=120, padx=50)
    windows.resizable(0, 0)

    def get_details():
        user_email = email_entry.get()
        user_password = pas_entry.get()
        user_name = name_entry.get()

        if len(user_name) == 0 or len(user_password) == 0 or len(user_email) == 0:
            messagebox.showerror(title="Empty", message="Email or Password can't be empty")
        else:
            user = {
                user_email: {
                    "name": user_name,
                    "password": user_password,
                    "email": user_email
                }
            }
            save_user(user)
            email_entry.delete(0, END)
            pas_entry.delete(0, END)
            name_entry.delete(0, END)
            messagebox.showinfo(title="Success", message="You have sucessfully created an account, Kindly log in.")
            windows.destroy()
            login()


    canvas = Canvas(width=80, height=80)
    image = PhotoImage(file="images/user.png")
    canvas.create_image(40, 40, image=image)
    canvas.grid(column=1, row=0)

    head = Label(text="Create Account", font=("Arial", 20, 'bold'))
    head.config(pady=10)
    head.grid(column=1, row=1, columnspan=2)

    name = Label(text="Name:   ", font=("Arial", 10, 'bold'))
    name.grid(column=0, row=2)
    name.config(pady=5)
    name_entry = Entry(width=35)
    name_entry.focus()
    name_entry.grid(column=1, row=2)

    email = Label(text="Email:   ", font=("Arial", 10, 'bold'))
    email.grid(column=0, row=3)
    email.config(pady=5)
    email_entry = Entry(width=35)
    email_entry.grid(column=1, row=3)

    password = Label(text="Password:   ", font=("Arial", 10, 'bold'))
    password.grid(column=0, row=4)
    password.config(pady=5)
    pas_entry = Entry(width=35)
    pas_entry.grid(column=1, row=4)

    submit = Button(text="Submit", font=("Arial", 12, 'normal'), command=get_details)
    submit.config(pady=6, padx=40, bg="green", fg="white")
    submit.grid(column=1, row=5)

    windows.mainloop()


