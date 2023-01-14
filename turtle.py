import random
import turtle
from turtle import Turtle, Screen


turtle.colormode(255)

# def color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return (r, g, b)
#
# game.speed("fastest")
#
# def draw(size):
#     for _ in range(int(369 / size)):
#         game.color(color())
#         game.circle(100)
#         head = game.heading()
#         game.setheading(head + size)
#
# draw(2)

# def forward():
#     game.forward(50)
#
# def backward():
#     game.backward(50)
#
# def right():
#     new = game.heading() - 10
#     game.setheading(new)
#
# def left():
#     new = game.heading() + 10
#     game.setheading(new)
#
# def clear():
#     game.penup()
#     game.clear()
#     game.home()
#     game.pendown()
#
#
#
# hold.listen()
# hold.onkey(forward, "w")
# hold.onkey(backward, "s")
# hold.onkey(right, "r")
# hold.onkey(left, "l")
# hold.onkey(clear, "c")


color = ["red", "green", "orange", "purple", "blue", "yellow"]
hold = Screen()
hold.setup(width=500, height=400)
user = hold.textinput(title="Turtle Game",  prompt="What color of turtle do you want to bet on? ")

position = [-70, -40, -10, 30, 60, 90]
all_turtle = []
game_on = False

if user:
    game_on = True


for i in range(0, 6):
    game = Turtle()
    game.shape("turtle")
    game.penup()
    game.color(color[i])
    game.goto(x=-220, y=position[i])
    all_turtle.append(game)

while game_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            game_on = False
            winner = turtle.pencolor()
            if winner == user:
                print(f"You won, The winner is {winner}")
            else:
                print(f"You lost, The winner is {winner}")


        ran = random.randint(0, 10)
        turtle.forward(ran)



hold.exitonclick()

