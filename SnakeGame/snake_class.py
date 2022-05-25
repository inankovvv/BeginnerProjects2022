from turtle import Turtle
import time

MOVE_DISTANCE = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self, blocks):
        self.blocks = blocks
        self.snake_list = []
        self.spawn_snake()
        self.head = self.snake_list[0]

    @staticmethod
    def _new_block(x, y):
        block = Turtle()
        block.penup()
        block.shape('square')
        block.color('white')
        block.goto(x, y)
        return block

    def spawn_snake(self):
        x = 0
        for _ in range(self.blocks):
            block = self._new_block(x, 0)
            self.snake_list.append(block)
            x -= MOVE_DISTANCE

    def add_block(self):
        last_block = self.snake_list[-1]
        x = last_block.xcor()
        y = last_block.ycor()
        new_block = self._new_block(x, y)
        self.snake_list.append(new_block)

    def move_forward(self):
        time.sleep(0.15)
        length = len(self.snake_list)
        snake = self.snake_list

        for block_num in range(length - 1, 0, -1):
            new_x = snake[block_num - 1].xcor()
            new_y = snake[block_num - 1].ycor()
            snake[block_num].goto(new_x, new_y)
        snake[0].forward(MOVE_DISTANCE)

    def reset(self):
        for block in self.snake_list:
            block.goto(1000, 1000)
        self.snake_list.clear()
        self.spawn_snake()
        self.head = self.snake_list[0]

    def go_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def go_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def go_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def go_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
