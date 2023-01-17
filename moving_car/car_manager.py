COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle
import random


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def cars(self):
        rand_car = random.randint(1, 6)
        if rand_car == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            ran_y = random.randint(-250, 250)
            new_car.goto(300, ran_y)
            self.all_cars.append(new_car)

    def move(self):
        for cars in self.all_cars:
            cars.backward(self.car_speed)

    def level(self):
        self.car_speed += MOVE_INCREMENT