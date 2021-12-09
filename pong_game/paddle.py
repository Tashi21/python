"""Paddle"""
from turtle import Turtle


class Paddle(Turtle):
    """Paddle class"""

    def __init__(self, position: tuple[int, int]) -> None:
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("#FFFFFF")
        self.penup()
        self.goto(position)

    def up(self) -> None:
        """Move the paddle up"""
        self.sety(self.ycor() + 20)

    def down(self) -> None:
        """Move the paddle down"""
        self.sety(self.ycor() - 20)
