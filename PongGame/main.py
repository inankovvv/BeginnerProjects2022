from turtle import Screen
from paddle_class import Paddle
from ball_class import Ball
from score_class import Score
import time

screen = Screen()
screen.tracer(0)
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong Game')

r_paddle = Paddle(x=350, y=0)
l_paddle = Paddle(x=-350, y=0)

ball = Ball()
score = Score()

screen.listen()
screen.onkeypress(key='Up', fun=r_paddle.move_up)
screen.onkeypress(key='Down', fun=r_paddle.move_down)
screen.onkeypress(key='w', fun=l_paddle.move_up)
screen.onkeypress(key='s', fun=l_paddle.move_down)

game_on = True

while game_on:
    screen.update()
    ball.move()
    time.sleep(ball.speed)

    # Collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Collision with right paddle
    if ball.xcor() > 320 and ball.distance(r_paddle) < 60:
        ball.bounce_x()

    # Collision with left paddle
    if ball.xcor() < -320 and ball.distance(l_paddle) < 60:
        ball.bounce_x()

    # Check if left player wins
    if ball.xcor() > 380:
        score.add_point('left')
        ball.reset_position()
    elif ball.xcor() < -380:
        score.add_point('right')
        ball.reset_position()

screen.exitonclick()
