from tkinter import *
from tkinter import messagebox
from auth import check_user
from dashboard import dashboard

def login():
    windows = Tk()
    windows.geometry("500x500")
    windows.title("Login")
    windows.config(pady=120, padx=50)
    windows.resizable(0, 0)

    def get_details():
        user_email = email_entry.get()
        user_password = pas_entry.get()


        if len(user_password) == 0 or len(user_email) == 0:
            messagebox.showerror(title="Empty", message="Email or Password can't be empty")
        else:
            if check_user(user=user_email, password=user_password):
                email_entry.delete(0, END)
                pas_entry.delete(0, END)
                messagebox.showinfo(title="Success", message="Login Sucessfully")
                windows.destroy()
                dashboard()
            else:
                messagebox.showerror(title="Error", message="User Not Found")





    canvas = Canvas(width=80, height=80)
    image = PhotoImage(file="images/user.png")
    canvas.create_image(40, 40, image=image)
    canvas.grid(column=1, row=0)

    head = Label(text="Login", font=("Arial", 20, 'bold'))
    head.config(pady=10)
    head.grid(column=1, row=1, columnspan=2)

    email = Label(text="Email:   ", font=("Arial", 10, 'bold'))
    email.grid(column=0, row=2)
    email.config(pady=5)
    email_entry = Entry(width=35)
    email_entry.grid(column=1, row=2)

    password = Label(text="Password:   ", font=("Arial", 10, 'bold'))
    password.grid(column=0, row=3)
    password.config(pady=5)
    pas_entry = Entry(width=35)
    pas_entry.grid(column=1, row=3)

    submit = Button(text="Submit", font=("Arial", 12, 'normal'), command=get_details)
    submit.config(pady=6, padx=40, bg="green", fg="white")
    submit.grid(column=1, row=4)

    windows.mainloop()


