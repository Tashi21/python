"""Scoreboard class"""
from turtle import Turtle


class Scoreboard(Turtle):
    """Scoreboard class"""

    def __init__(self) -> None:
        super().__init__()
        self.left = 0
        self.right = 0
        self.hideturtle()
        self.penup()
        self.color("#FFFFFF")
        self.display()

    def display(self) -> None:
        """Display score"""
        self.clear()
        self.goto(-100, 200)
        self.write(self.left, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.right, align="center", font=("Courier", 80, "normal"))
