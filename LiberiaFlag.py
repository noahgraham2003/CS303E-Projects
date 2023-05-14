# File: LiberiaFlag.py
# Student: Noah Graham
# UT EID: nlg838
# Course Name: CS303E
# 
# Date: 4/14/23
# Description of Program: This program draws the flag of liberia using turtle graphics

import turtle

# flag will be 600x400

myBlue = (0, 32, 91)
myRed = (191, 13, 62)
white = (255, 255, 255)

def drawRectangle(width, height, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()

def drawStar():
    startingX = -215
    startingY = 140
    ted.screen.colormode(255)
    turtle.penup()
    turtle.goto(startingX,startingY)
    turtle.pendown()
    turtle.fillcolor(white) 
    turtle.begin_fill()
    for i in range(5):
        turtle.forward(40)
        turtle.right(144)
        turtle.forward(40)
        turtle.right(72 - 144)
    turtle.end_fill()

def drawStripes():
    ted.screen.colormode(255)
    turtle.up()
    turtle.goto(-300, 200)
    turtle.down()
    for i in range(11):
        if i % 2 != 0:
            drawRectangle(750, 36, white)
        else:
            drawRectangle(750, 36, myRed)
        turtle.up()
        turtle.right(90)
        turtle.forward(36)
        turtle.setheading(0)
        turtle.down()
    
def drawCanton():
    ted.screen.colormode(255)
    turtle.up()
    turtle.goto(-300, 200)
    turtle.down()
    drawRectangle(150,150, myBlue)
    

def liberiaFlag(turtle):
    drawStripes()
    drawCanton()
    drawStar()

ted = turtle.Turtle()
ted.speed(100000)
liberiaFlag(ted)
turtle.done()
