import time
from tkinter import *
import pandas
from random import choice
BG = "#B1DDC6"
current_card = {}
learn = {}

#-------------------------------- READ DATA FROM CSV ------------------------------#
try:
    data = pandas.read_csv("data/To_learn.csv")
except FileNotFoundError:
    Original_data = pandas.read_csv("data/french_words.csv")
    learn = Original_data.to_dict(orient="records")
else:
    learn = data.to_dict(orient="records")

#-------------------------------- CHECK FOR NEXT CARD------------------------------#
def next_card():
    global current_card, flip_timer
    windows.after_cancel(flip_timer)
    current_card = choice(learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_bg, image=front_imge)
    flip_timer = windows.after(3000, func=flip_card)


#-------------------------------- CHANGE CARDS ------------------------------#
def flip_card():
    global current_card
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_bg, image=back_img)

#-------------------------------- PRODUCE A NEW CARD FROM WORDS NOT YET LEARNT ------------------------------#
def new_card():
    learn.remove(current_card)
    data = pandas.DataFrame(learn)
    data.to_csv("data/To_learn.csv", index=False)
    if len(learn) == 0:
        canvas.itemconfig(card_title, text="WELDONE, YOU HAVE DONE A GREAT JOB", font=("Ariel", 10, "bold"))
        canvas.itemconfig(card_word, text=f"CHEERS ON YOUR WINING, YOU COMPLETED {len(Original_data)} FRENCH WORDS", \
                          font=("Ariel", 10, "italic"))
    next_card()

#-------------------------------- UI Interface ------------------------------#

windows = Tk()
windows.title("Password Manager")
windows.config(padx=20, pady=20, bg=BG)
flip_timer = windows.after(3000, func=flip_card)


canvas = Canvas(width=800, height=450)
front_imge = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
card_bg = canvas.create_image(398, 220, image=front_imge)
card_title = canvas.create_text(398, 120, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(398, 280, text="Word", font=("Ariel", 60, "bold"))
canvas.config(bg=BG, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)


left_img = PhotoImage(file="images/wrong.png")
left_btn = Button(image= left_img, highlightthickness=0, width=75, height=75, command=next_card)
left_btn.config(bg=BG)
left_btn.grid(column=0, row=1)


right_img = PhotoImage(file="images/right.png")
right_btn = Button(image= right_img, highlightthickness=0, width=75, height=75, command=new_card)
right_btn.config(bg=BG)
right_btn.grid(column=1, row=1)
next_card()

windows.mainloop()