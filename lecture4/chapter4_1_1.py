"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

import math
import turtle


def square(t, length):
    """Draws a square with sides of the given length.

    Returns the Turtle to the starting position and location.
    """
    for i in range(4):
        t.fd(length)
        t.lt(90)


def polyline(t, n, length, angle):
    """Draws n line segments.

    t: Turtle object
    n: number of line segments
    length: length of each segment
    angle: degrees between segments
    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def polygon(t, n, length):
    """Draws a polygon with n sides.

    t: Turtle
    n: number of sides
    length: length of each side.
    """
    angle = 360.0/n
    polyline(t, n, length, angle)


def arc2(t, r, angle):
    """Draws an arc with the given radius and angle.

    t: Turtle
    r: radius
    angle: angle subtended by the arc, in degrees
    """
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n

    # making a slight left turn before starting reduces
    # the error caused by the linear approximation of the arc
    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)


def arc1(t, r, angle):
    """Draws an arc with the given radius and angle.

    t: Turtle
    r: radius
    angle: angle subtended by the arc, in degrees
    """
    arc_length = 2 * math.pi * r * abs(angle) / 360
    # n = int(arc_length / 4) + 3
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n

    # making a slight left turn before starting reduces
    # the error caused by the linear approximation of the arc
    # t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle),
    # t.rt(step_angle/2)


def circle(t, r, mode=1):
    """Draws a circle with the given radius.

    t: Turtle
    r: radius
    """
    if mode == 1:
        arc1(t, r, 360)

    if mode == 2:
        arc2(t, r, 360)


# the following condition checks whether we are
# running as a script, in which case run the test code,
# or being imported, in which case don't.

if __name__ == '__main__':

    bob = turtle.Turtle()
    bob.color('red')
    bob.pensize(8)

    # draw a circle centered on the origin
    radius = 600
    # circle(bob, radius, 1)
    arc1(bob, radius, 30)

    bob = turtle.Turtle()
    bob.color('green')
    bob.pensize(8)

    # draw a circle centered on the origin
    
    # circle(bob, radius, 1)
    arc2(bob, radius, 30)

    bob = turtle.Turtle()
    bob.color('blue')
    bob.pensize(8)

    # draw a circle centered on the origin
    bob.lt(15)
    bob.fd(radius/2)
    # circle(bob, radius, 2)

    # wait for the user to close the window
    turtle.mainloop()


### STACK DIAGRAM ###

## main ##

# bob => Turtle
# radius => 100

## circle ##

# t => Turtle
# r => 100

## arc ##

# t => Turtle
# r => 100
# angle => 360

# arc_length => 600
# n => 153
# step_length => 4
# step_angle => 2.3

## polyline ##

# t => Turtle 
# n => 153
# length => 4
# angle => 2.3


