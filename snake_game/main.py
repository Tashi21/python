"""Classic snake game to apply OOP concepts and file handling."""
import time
from turtle import Screen

from food import Food
from scoreboard import Scoreboard
from snake import Snake

GAME = True
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("#000000")
screen.title("My Snake Game")
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.onkeypress(key="Up", fun=snake.up)
screen.onkeypress(key="Down", fun=snake.down)
screen.onkeypress(key="Left", fun=snake.left)
screen.onkeypress(key="Right", fun=snake.right)

while GAME:
    screen.update()
    time.sleep(0.09)
    snake.move()

    if snake.head.distance(food) < 15:
        food.move()
        scoreboard.score += 1
        snake.add_segment(snake.segments[-1].position())
        scoreboard.display_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    for segment in snake.segments[1::]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()
