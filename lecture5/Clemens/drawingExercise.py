# exercise 5

import turtle
import math

def polygon(t, length, n, d = 360):
    angle = d / n
    for _ in range(n):
        t.forward(length)
        t.left(angle)

def reverse_polygon(t, length, n, d = 360):
    angle = d / n
    for _ in range(n):
        t.forward(length)
        t.right(angle)

def arc(t, r, angle):
    circumference = 2 * math.pi * r
    arc_length = circumference * (angle / 360)
    n = int(arc_length / 3)  # Approximation for number of sides
    length = arc_length / n
    polygon(t, length, n, angle)


def draw_c(bob):
    bob.seth(135)
    arc(bob, 100, 270)

## here are some of the functions that are worth exploring
## when writing CLEMENS:

# t.fd
# t.bk
# t.lt
# t.rt


# Create a turtle object
bob = turtle.Turtle()

# Test the arc function with different values of r and angle
#arc(bob, 50, 90/2)    # Arc with radius 50 and angle 90 degrees
# arc(bob, 100, 180)  # Arc with radius 100 and angle 180 degrees
# arc(bob, 150, 270)  # Arc with radius 150 and angle 270 degrees

draw_c(bob)

# Run the turtle graphics
turtle.mainloop()
