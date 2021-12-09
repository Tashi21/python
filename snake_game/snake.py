"""Snake class"""
from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """Snake class"""

    def __init__(self) -> None:
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self) -> None:
        """Creates initial snake"""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position) -> None:
        """Adds segment to snake"""
        new_segment = Turtle(shape="square")
        new_segment.color("#00FF00")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self) -> None:
        """Reset snake"""
        for segment in self.segments:
            segment.goto(1000, 1000)

        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def move(self) -> None:
        """Moves snake"""
        for s in range(len(self.segments) - 1, 0, -1):
            x = self.segments[s - 1].xcor()
            y = self.segments[s - 1].ycor()
            self.segments[s].goto(x, y)

        self.head.forward(MOVE)

    def up(self) -> None:
        """Move snake up"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self) -> None:
        """Move snake down"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self) -> None:
        """Move snake left"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self) -> None:
        """Move snake right"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
