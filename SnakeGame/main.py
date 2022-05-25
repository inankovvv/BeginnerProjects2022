from turtle import Screen
from snake_class import Snake
from food_class import Food
from score_class import Score

screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')

snake = Snake(3)
food = Food()
score = Score()

game_on = True


def game_off():
    global game_on
    game_on = False


# Screen list for onkey
screen.listen()
screen.onkey(key='space', fun=game_off)
screen.onkey(key='Up', fun=snake.go_up)
screen.onkey(key='Down', fun=snake.go_down)
screen.onkey(key='Left', fun=snake.go_left)
screen.onkey(key='Right', fun=snake.go_right)

count = 0
while game_on:
    screen.update()
    snake.move_forward()

    # Getting longer with food
    if snake.head.distance(food) < 15:
        snake.add_block()
        food.refresh()
        score.add_to_score()

    # Check if the wall was hit
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or -290 > snake.head.ycor():
        score.reset()
        snake.reset()

    # Check if the tail was hit
    for segment in snake.snake_list:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 5:
            score.reset()
            snake.reset()
            print('Hit a segment')

screen.exitonclick()
