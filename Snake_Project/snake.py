from turtle import Turtle


"""
A program which runs a snake game.
"""
POSITION = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 15
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    """Snake Game class"""

    def __init__(self):
        """Self Initializing Function"""

        self.snakes = []
        self.new_snake()

    def new_snake(self):
        for ps in POSITION:
            self.add(ps)

    def add(self, ps):
        turtle = Turtle("square")
        turtle.color("white")
        turtle.penup()
        turtle.goto(ps)
        self.snakes.append(turtle)

    def extend(self):
        self.add(self.snakes[-1].position())

    def move(self):
        """Function that gets the snake to move in its direction."""

        for s in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[s - 1].xcor()
            new_y = self.snakes[s - 1].ycor()
            self.snakes[s].goto(new_x, new_y)

        self.snakes[0].forward(DISTANCE)

    def right(self):
        if self.snakes[0].heading() != LEFT:
            self.snakes[0].setheading(RIGHT)

    def left(self):
        if self.snakes[0].heading() != RIGHT:
            self.snakes[0].setheading(LEFT)

    def up(self):
        if self.snakes[0].heading() != DOWN:
            self.snakes[0].setheading(UP)

    def down(self):
        if self.snakes[0].heading() != UP:
            self.snakes[0].setheading(DOWN)
