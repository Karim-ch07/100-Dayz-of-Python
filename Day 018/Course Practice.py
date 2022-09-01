# from turtle import Turtle, Screen
# from turtle import * # this module import method would import everything from the module, it is not advised

# timmy = Turtle()
# timmy.shape("circle")
# timmy.color("red")

# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)

# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)
#
# screen = Screen()
# screen.exitonclick()

# import turtle as t # defining Alias name for the turtle library

#from turtle import *

from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("circle")
tim.width(10)
tim.speed(50)

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]

# Dashed line
# for _ in range(10):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# Different shapes
def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

# draw_shape(5)

# for sides in range(3, 11):
#     tim.color(random.choice(colours))
#     draw_shape(sides)

# Random walk

def random_walk():
    tim.color(random.choice(colours))
    tim.setheading(random.choice(directions))
    tim.forward(25)

for _ in range(200):
    random_walk()

screen = Screen()
screen.exitonclick()
