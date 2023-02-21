#STUDENT PROFILE INTERFACE
from tkinter import *
from login import login
from create_acct import create_acct

windows = Tk()
windows.geometry("500x500")
windows.title("Welcome on Board")
windows.config(pady=120, padx=50)
windows.resizable(0, 0)

welcome_lab = Label(text="WELCOME ON BOARD", font=("Arial", 25, "bold"))
welcome_lab.grid(column=0, row=0, columnspan=2)
welcome_lab.config(pady=50)


def log():
    windows.after(1000)
    windows.destroy()
    login()


def create():
    windows.after(1000)
    windows.destroy()
    create_acct()


login_btn = Button(text="Login", font=("Arial", 12, "bold"), bg="green", command=log)
login_btn.grid(column=0, row=1)

register_btn = Button(text="Register", font=("Arial", 12, "bold"), bg="red", command=create)
register_btn.grid(column=1, row=1)
windows.mainloop()
