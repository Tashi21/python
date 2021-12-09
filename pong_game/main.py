"""A basic pong game to apply OOP concepts like classes, inheritance, and modular programming."""
import time
from turtle import Screen

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

GAME = True

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("#000000")
screen.title("Pong")
screen.tracer(0)

right = Paddle((350, 0))
left = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(key="Up", fun=right.up)
screen.onkeypress(key="Down", fun=right.down)
screen.onkeypress(key="w", fun=left.up)
screen.onkeypress(key="s", fun=left.down)

while GAME:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.bounce_y()

    if ball.distance(right) < 50 and ball.xcor() > 320 or ball.distance(left) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        scoreboard.left += 1
        scoreboard.display()
        ball.reset()

    if ball.xcor() < -380:
        scoreboard.right += 1
        scoreboard.display()
        ball.reset()

screen.exitonclick()
