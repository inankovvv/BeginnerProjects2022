from turtle import Screen
from tim_class import Tim
from cars_class import Cars
from score_class import Score
import time

screen = Screen()
screen.setup(width=700, height=600)
screen.tracer(0)
screen.title('Turtle Crossing Game')

tim = Tim()
cars = Cars(1)
score = Score()

screen.listen()
screen.onkeypress(key='Up', fun=tim.move_up)
screen.onkeypress(key='Left', fun=tim.move_left)
screen.onkeypress(key='Right', fun=tim.move_right)

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    cars.generate_cars()
    cars.move_cars()

    # Check if tim was hit by a car
    for car in cars.cars_list:
        if car.distance(tim) < 20:
            game_on = False
            score.game_over()

    # Check if tim made it to the finish line, take him back to the start line and update the score
    if tim.ycor() > 270:
        tim.go_to_start()
        cars.next_level()
        score.update_level()

screen.exitonclick()
