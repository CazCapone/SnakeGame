from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Setup Screen
screen = Screen()
width, height = 600, 600
screen.setup(width, height)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

# Setup game
snake = Snake()
food = Food()
board = Scoreboard()

# Create movement controls
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left") 

# Game Loop
is_running = True

while is_running:
    screen.update()
    time.sleep(0.1)
    
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        board.add_score()

    # Collision detection
    if (snake.head.xcor() > 280 
        or snake.head.xcor() < -280 
        or snake.head.ycor() > 280 
        or snake.head.ycor() < -280): 
        board.reset()
        snake.reset()

    for p in snake.snake_parts[1:]:
        if snake.head.distance(p) < 10:
            board.reset()
            snake.reset()





















screen.exitonclick()
