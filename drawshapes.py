from turtle import *
import math

# Name your turtle
t = Turtle()

# Set Up your screen and starting position.
setup(500,300)
x_pos = 0
y_pos = 0
t.setposition(x_pos, y_pos)

### Write your code below:
# Sets variable for the number of sides of the drawn shape to 0
number_sides = 0

# User can choose how many sides they want their shape to have
userinput_sides = 0
userinput_sides = int(input("How many sides? (or -1 for circle) \n"))
#User can select the color they want
shape_color = input("What color?")
shape_size = int(input("What size?"))

circle = 0 #variable for circle

#conditional to make circle
#if userinput_sides = -1: #doesn't work
    #while circle < 1:
    #t.pendown()
    #t.pencolor(shape_color)
    #t.forward(shape_size)
    #t.right(1)
    #circle = circle + 1
    # or use this function to make circle
    #t.circle(100, 360, 360)

#loop for shapes except circle
t.begin_fill() #begins to fill the shape; put outside loop so it doesnt repeat each time side drawn
t.pencolor(shape_color)
while number_sides < userinput_sides:
    t.pendown()
    t.pensize(5)#thickness of line
    t.pencolor(shape_color) #Shape will be drawn in this color
    t.forward(shape_size) #The turtle will move forward
    t.right(360/userinput_sides) #The turtle will turn clockwise at the angle of the shape they want
    number_sides += 1
    t.speed(50)
t.end_fill()
t.pencolor(shape_color)

# Close window on click.
exitonclick()
