from turtle import Turtle, Screen, colormode
import random
timmy = Turtle()
timmy.shape("turtle")
# timmy.color("red")
colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(angle)

screen = Screen()

for shape_side_n in range(3, 6):
    timmy.color(random_color())
    draw_shape(shape_side_n)

screen.exitonclick()
