from turtle import Turtle

START_POSITION = (0, -270)
STEP = 10


class Tim(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.setheading(90)
        self.go_to_start()

    def go_to_start(self):
        self.goto(START_POSITION)

    def move_up(self):
        self.forward(STEP)

    def move_left(self):
        self.goto(self.xcor() - STEP, self.ycor())

    def move_right(self):
        self.goto(self.xcor() + STEP, self.ycor())
