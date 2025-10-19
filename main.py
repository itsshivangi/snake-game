from turtle import Turtle,Screen
from snake import Snake
import random
import time #1 Import the time module to control the speed of the snake


screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


snake = Snake()


game_is_on = True
while game_is_on:
    screen.update()  # Update the screen to reflect changes (import time module)
    time.sleep(0.1)  # Pause for a short duration to control the speed of the snake (time module)

    snake.move()  # Move the snake forward
     















screen.exitonclick()