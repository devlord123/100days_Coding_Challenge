import turtle
from turtle import Turtle, Screen
import pandas

screen = Screen()
image = "map.gif"
screen.addshape(image)
map = Turtle(image)
map.shapesize(100)

def locate(x, y):
    print(x, y)

turtle.onscreenclick(locate)

data = pandas.read_csv("36_states.csv")
all_state = data["state"].to_list()
state = data[data.state == "Kano"]
# print(state.x)

guess = True
guessed_state = []

while len(guessed_state) <= 37:

    user = screen.textinput(f"{len(guessed_state)} / 37", "What state do you wanna guess? ").title()

    if user == "Exit":
        failed_state = []
        for state in all_state:
            if state not in guessed_state:
                failed_state.append(state)
        dt = pandas.DataFrame(failed_state)
        dt.to_csv("failed_state.csv")
        break

    for state in all_state:

        if state == user:
            cor = data[data.state == user]
            x_cor = int(cor.x)
            y_cor = int(cor.y)
            place = Turtle()
            place.hideturtle()
            place.penup()
            place.goto(x_cor, y_cor)
            place.write(f"{user}")
            guessed_state.append(user)






turtle.mainloop()

