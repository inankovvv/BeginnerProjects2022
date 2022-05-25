from turtle import Turtle
import random

START_INCREMENT = 5
MOVE_INCREMENT = 5
COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']


class Cars:
    def __init__(self, level=1):
        self.level = level
        self.speed = START_INCREMENT
        self.cars_list = []

    @staticmethod
    def _car():
        new_y = random.randint(-240, 240)
        car = Turtle()
        car.penup()
        car.shape('square')
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.color(random.choice(COLORS))
        car.goto(300, new_y)
        car.setheading(180)
        return car

    def generate_cars(self):
        level = abs(10 - self.level)
        if level == 0:
            level = 1
        random_chance = random.randint(1, level)
        if random_chance == 1:
            new_car = self._car()
            self.cars_list.append(new_car)

    def move_cars(self):
        for car in self.cars_list:
            car.forward(self.speed)

    def next_level(self):
        self.speed += MOVE_INCREMENT
        self.level += 1
