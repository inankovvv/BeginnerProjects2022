from turtle import Turtle

FONT = ('Courier', 15, 'normal')
ALIGNMENT = 'center'


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.get_high_score()
        self.penup()
        self.goto(0, 260)
        self.color('white')
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        score = f'Score: {self.score}, High Score: {self.high_score}'
        self.write(score, align=ALIGNMENT, font=FONT)

    def add_to_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('high_score.txt', mode='w') as file:
                file.write(str(self.high_score))
        self.score = 0

    @staticmethod
    def get_high_score():
        with open('high_score.txt', mode='r') as file:
            high_score = file.read()
        return int(high_score)

