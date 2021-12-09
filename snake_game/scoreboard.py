"""Scoreboard class"""
from turtle import Turtle


class Scoreboard(Turtle):
    """Scoreboard class"""

    def __init__(self) -> None:
        super().__init__()
        self.score = 0

        with open(file="snake_game/data.txt", mode="r") as file:
            self.highscore = int(file.read())

        self.hideturtle()
        self.penup()
        self.color("#FFFFFF")
        self.goto(0, 260)
        self.display_score()

    def display_score(self) -> None:
        """Display score"""
        self.clear()
        self.write(
            f"Score: {self.score} High Score: {self.highscore}",
            align="center",
            font=("Arial", 24, "normal")
        )

    def reset(self) -> None:
        """Reset score"""
        if self.score > self.highscore:
            self.highscore = self.score

            with open(file="snake_game/data.txt", mode="w") as file:
                file.write(str(self.highscore))

        self.score = 0
        self.display_score()
