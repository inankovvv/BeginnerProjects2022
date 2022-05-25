from turtle import Turtle

FONT = ('Courier', 15, 'normal')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.hideturtle()
        self.goto(-280, 260)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f'Level: {self.level}', align='center', font=FONT)

    def update_level(self):
        self.level += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f'Game over!', align='center', font=FONT)
