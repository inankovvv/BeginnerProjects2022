from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x = 0, y = 0, autonomous = False):
        super().__init__()
        self.x = x
        self.y = y
        self.penup()
        self.color('white')
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(self.x, self.y)

    def move_up(self):
        self.y += 20
        self.goto(self.x, self.y)

    def move_down(self):
        self.y -= 20
        self.goto(self.x, self.y)
