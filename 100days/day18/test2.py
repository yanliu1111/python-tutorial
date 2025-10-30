from turtle import Turtle, Screen, colormode, Terminator
from tkinter import TclError
import random

timmy = Turtle()
timmy.shape("turtle")
colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b) # return as a tuple

directions = [0, 90, 180, 270]
screen = Screen()
# screen.tracer(0)  # using automatic updates
timmy.pensize(15)
timmy.speed("fastest")

try:
    for _ in range(200):
        timmy.color(random_color())
        timmy.forward(30)
        timmy.setheading(random.choice(directions))
except (Terminator, TclError):
    print("Turtle graphics terminated (window closed).")
else:
    screen.exitonclick()