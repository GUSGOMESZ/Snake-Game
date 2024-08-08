from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.shape("circle")
        self.color("red")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-260, 260)
        random_y = random.randint(-260, 230)
        self.goto(random_x, random_y)