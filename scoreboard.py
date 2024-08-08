from turtle import Turtle
ALIGN = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.highscore = 0
        self.update_highscore()
        self.penup()
        self.color("white")
        self.goto(0, 260)
        self.update_scoreboard()

    def update_highscore(self):
        with open("highscore.txt") as file:
            self.highscore = int(file.read())

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.highscore}", align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("highscore.txt", mode="w") as file:
                file.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()