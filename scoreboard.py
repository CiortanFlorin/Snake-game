from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(0, 270)
        self.color("white")
        self.write("Score:", align="center", font=("Arial", 12, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=("Arial", 12, "normal"))

    def keepscore(self, x):
        self.clear()
        self.write(f"Score: {x}", align="center", font=("Arial", 12, "normal"))