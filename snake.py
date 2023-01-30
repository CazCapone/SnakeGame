from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20
UP, DOWN, LEFT, RIGHT = 90, 270, 180, 0


class Snake:

    def __init__(self): 
        self.snake_parts = []
        self.create_snake()
        self.head = self.snake_parts[0]

    def create_snake(self):
        for pos in STARTING_POSITIONS:
            self.add_part(pos)

    def add_part(self, pos):
        snake = Turtle("square")
        snake.color("white")
        snake.penup()
        snake.goto(pos)
        self.snake_parts.append(snake)

    def extend(self):
        self.add_part(self.snake_parts[-1].position())

    def move(self):
        for s in range(len(self.snake_parts) - 1, 0, -1):
            new_x = self.snake_parts[s - 1].xcor()
            new_y = self.snake_parts[s - 1].ycor()
            self.snake_parts[s].goto(new_x, new_y)
        self.head.forward(DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)