from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game!")
screen.tracer(0)

snake = []

for _ in range(3):
    temp = Turtle("square")
    temp.color("white")
    temp.penup()
    temp.goto(-20*_, 0)
    snake.append(temp)

we_playing = True

while we_playing:
    screen.update()
    time.sleep(0.1)
    for idx in range(len(snake)-1, 0, -1):
        snake[idx].goto(snake[idx - 1].xcor(), snake[idx - 1].ycor())
    snake[0].fd(20)
    
screen.exitonclick()
