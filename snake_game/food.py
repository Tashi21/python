"""Food class"""
from turtle import Turtle
import random


class Food(Turtle):
    """Food class"""

    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("#FF0000")
        self.speed(0)
        self.move()

    def move(self) -> None:
        """Move food to random location"""
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)
