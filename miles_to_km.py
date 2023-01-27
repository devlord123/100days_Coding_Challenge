import tkinter

def miles():
    value = float(entry.get())
    km = round(value * 1.609)
    label2.config(text=f"{km}")

screen = tkinter.Tk()
screen.title("Form Table")
screen.minsize(500, 500)
screen.config(padx=50, pady=50)


entry = tkinter.Entry(width=10)
entry.grid(column=1, row=0)

label = tkinter.Label(text="Miles", font=("Arial", 20, "normal"))
label.grid(column=2, row=0)


label1 = tkinter.Label(text="is equal to", font=("Arial", 16, "normal"))
label1.grid(column=0, row=1)

label2 = tkinter.Label(text="0", font=("Arial", 16, "normal"))
label2.grid(column=1, row=1)


label3 = tkinter.Label(text="km", font=("Arial", 24, "normal"))
label3.grid(column=2, row=1)

button = tkinter.Button(text="Calculate", command=miles)
button.grid(column=1, row=2)





screen.mainloop()