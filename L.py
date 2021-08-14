import turtle
import os
a = turtle.Turtle()
a.shape("lak posht")

for i in range(6):
    a.penup()
    a.goto(0 + (8 * i), 0 - (8 * i))
    a.pendown()
    
    for j in range(i + 3):
        a.left(180 - ((i+1)*180)/(i+3)) 
        a.forward(40 + (12 * i))
        