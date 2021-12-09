"""Ball"""
from turtle import Turtle


class Ball(Turtle):
    """Ball class"""

    def __init__(self) -> None:
        super().__init__()
        self.color("#FFFFFF")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1

    def move(self) -> None:
        """Move the ball"""
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x, y)

    def bounce_y(self) -> None:
        """Bounce the ball"""
        self.y_move *= -1

    def bounce_x(self) -> None:
        """Hit the ball"""
        self.x_move *= -1
        self.ball_speed *= 0.9

    def reset(self) -> None:
        """Reset the ball"""
        self.ball_speed = 0.1
        self.goto(0, 0)
        self.bounce_x()
