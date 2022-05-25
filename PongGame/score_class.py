from turtle import Turtle

FONT = ('Courier', 15, 'normal')
ALIGNMENT = 'center'

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.penup()
        self.color('white')
        self.goto(0, 260)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        score_is = f'{self.l_score}   {self.r_score}'
        self.write(score_is, align=ALIGNMENT, font=FONT)

    def add_point(self, player):
        if player == 'left':
            self.l_score += 1
        elif player == 'right':
            self.r_score += 1
        self.update_score()