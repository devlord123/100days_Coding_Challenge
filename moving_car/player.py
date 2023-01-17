STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.left(90)
        self.goto(STARTING_POSITION)

    def go_start(self):
        self.goto(STARTING_POSITION)

    def finish(self):
        if self.ycor() > FINISH_LINE_Y:
           return True
        else:
            return False

    def move(self):
        self.forward(MOVE_DISTANCE)

