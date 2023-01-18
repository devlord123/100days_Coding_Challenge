import turtle
import pandas
from turtle import Turtle, Screen

screen = Screen()
image = "blank_states_img.gif"
screen.addshape(image)
t = Turtle(image)
screen.tracer(0)

data = pandas.read_csv("50_states.csv")
state = data["state"].to_list()





user_guess = []
game_on = True

while len(user_guess) <= 50:
    screen.update()
    user_ans = screen.textinput(f"{len(user_guess)}/50", "What's your guess? ").title()

    if user_ans == "Exit":
        missin_state = []
        for sta in state:
            if sta not in user_guess:
                missin_state.append(sta)
        new_data = pandas.DataFrame(missin_state)
        new_data.to_csv("missing_state.csv")
        break
    for st in state:
        if st == user_ans:
            cor = data[data.state == user_ans]
            x_cor = int(cor.x)
            y_cor = int(cor.y)
            t = Turtle()
            t.hideturtle()
            t.penup()
            t.goto(x_cor, y_cor)
            t.write(f"{user_ans}")
            user_guess.append(user_ans)









turtle.mainloop()


