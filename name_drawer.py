"""
Module: name_drawer

A program to draw a name using one (or more) turtles.

Authors:
1) Name - USD Email Address
2) Name - USD Email Address
"""
import turtle

# Add your code here, and delete this comment once you start.
import turtle

# Author: [Your Name]
# Email: [Your Email]
# Date Created: [Date]
# Description: This program uses turtle graphics to draw my first name.

# Get user input for customization
pen_color = input("Enter the color for the pen: ")
bg_color = input("Enter the color for the background: ")

turtle.bgcolor(bg_color)  # Set background color

# Create turtle object
t = turtle.Turtle()
t.speed(3)  # Set turtle speed
t.pensize(5)  # Set pen thickness
t.color(pen_color)  # Set pen color
t.shape("turtle")  # Change turtle shape

def draw_T():
    """Draw the letter T"""
    t.penup()
    t.goto(-150, 100)
    t.pendown()
    t.forward(50)
    t.backward(25)
    t.right(90)
    t.forward(75)
    t.penup()

def draw_O():
    """Draw the letter O"""
    t.goto(-80, 50)
    t.pendown()
    t.circle(25)
    t.penup()

def draw_M():
    """Draw the letter M"""
    t.goto(-20, -25)
    t.pendown()
    t.left(90)
    t.forward(75)
    t.right(135)
    t.forward(35)
    t.left(90)
    t.forward(35)
    t.right(135)
    t.forward(75)
    t.penup()

def draw_A():
    """Draw the letter A"""
    t.goto(40, -25)
    t.pendown()
    t.left(75)
    t.forward(75)
    t.right(150)
    t.forward(75)
    t.backward(35)
    t.right(105)
    t.forward(30)
    t.penup()

# Draw the name

draw_T()
draw_O()
draw_M()
draw_A()

# Hide turtle and display the window
t.hideturtle()
turtle.done()


print("COMP110 PSA1. Delete this line after you start editing.")
