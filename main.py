from turtle import Screen
from snake import Snake 
from food import Food
from scoreboard import Scoreboard
import random
import time   #1 Import the time module to control the speed of the snake


screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # Turn off automatic screen updates for smoother animation

snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()  # Update the screen to reflect changes (import time module)
    time.sleep(0.1)  # Pause for a short duration to control the speed of the snake (time module)

    snake.move()  # Move the snake forward

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if (snake.head.xcor() > 290 or snake.head.xcor() < -290 or
            snake.head.ycor() > 290 or snake.head.ycor() < -290):
        scoreboard.reset()
        snake.reset()
        
    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake



screen.exitonclick()