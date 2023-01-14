from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score

game = Snake()
food = Food()
score = Score()
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


screen.listen()
screen.onkey(game.up, "Up")
screen.onkey(game.down, "Down")
screen.onkey(game.left, "Left")
screen.onkey(game.right, "Right")
snake_game = True

while snake_game:

    screen.update()
    time.sleep(0.1)
    game.move()

    # Detect when the snake eats the food
    if game.snakes[0].distance(food) < 25:
        food.refresh()
        game.extend()
        score.score_increment()

    # Detect collision with wall
    if game.snakes[0].xcor() > 290 or game.snakes[0].xcor() < -290 or game.snakes[0].ycor() > 290\
            or game.snakes[0].ycor() < -290:
        snake_game = False
        score.game_Over()

    # Detect collision with tail
    for seg in game.snakes[1:]:
        if game.snakes[0].distance(seg) < 10:
            score.game_Over()
            snake_game = False


screen.exitonclick()
