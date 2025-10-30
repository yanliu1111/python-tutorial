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


# screen.tracer(0)  # using automatic updates
timmy.speed("fastest")

def draw_spirograph(size_of_gap):
  size = 360/size_of_gap
  for _ in range(int(size)):
    timmy.color(random_color())
    timmy.circle(100)
    # print(timmy.heading())
    timmy.setheading(timmy.heading() + size_of_gap)

draw_spirograph(20)

screen = Screen()
screen.exitonclick()
# try:
#     for _ in range(200):
#         timmy.color(random_color())
#         timmy.forward(30)
# except (Terminator, TclError):
#     print("Turtle graphics terminated (window closed).")
# else:
#     screen.exitonclick()