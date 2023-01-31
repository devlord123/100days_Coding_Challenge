from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global timer, rep
    screen.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="TIMER", fg=GREEN)
    check_mark.config(text="")
    rep = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def time_func():
    global rep
    rep +=1
    work_sec = WORK_MIN * 60
    short_sec = SHORT_BREAK_MIN * 60
    long_sec = LONG_BREAK_MIN * 60

    if rep % 8 == 0:
        label.config(text="LONG BREAK", fg=RED)
        count_down(long_sec)
    elif rep % 2 == 0:
        label.config(text="BREAK", fg=PINK)
        count_down(short_sec)
    else:
        label.config(text="WORK", fg=GREEN)
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    min = math.floor(count / 60)
    sec = count % 60
    if sec < 10:
        sec = f"0{sec}"
    if sec == 0:
        sec = "00"

    canvas.itemconfig(timer_text, text=f"{min}:{sec}")
    if count > 0:
        global timer
        timer = screen.after(1000, count_down, count - 1)
    else:
        time_func()
        marks = ""
        session = math.floor(rep/2)
        for _ in range(session):
            marks += "✔️"

        check_mark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
screen = Tk()
screen.title("Pomondoro")
screen.config(padx=100, pady=50, bg=YELLOW)

label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 30, "bold"), bg=YELLOW)
label.grid(column=1, row=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(100, 110, image=image)
timer_text = canvas.create_text(103, 130, text="00:00", font=(FONT_NAME, 30, "bold"), fill="white")
canvas.grid(column=1, row=2)


start_btn = Button(text="Start", command=time_func)
start_btn.grid(column=0, row=3)

check_mark = Label(fg=GREEN, bg=YELLOW)
check_mark.grid(column=1, row=4)

reset_btn = Button(text="Reset", command=reset)
reset_btn.grid(column=2, row=3)


screen.mainloop()