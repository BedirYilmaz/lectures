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
    angle = 360.0 / n
    polyline(t, n, length, angle)


def arc(t, r, angle):
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
    t.lt(step_angle / 2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle / 2)


def draw_leaf(bob, radius, angle):
    # draw a leaf
    arc(bob, radius, angle)
    bob.lt(180 - angle)
    arc(bob, radius, angle)


def draw_flower(bob, radius, n):
    angle = 360 / n
    for _ in range(n):
        draw_leaf(bob, radius, angle)
        if n % 2 == 1:
            bob.lt(180 + angle)
    return angle


def draw_flower_interleaved(bob, radius, n):
    ang = draw_flower(bob, radius, n)
    bob.rt(ang / 2)
    draw_flower(bob, radius, n)


def draw_flowers(bob, radius):
    # move(bob, -radius)
    # draw_flower(bob, radius, 7)
    # move(bob, radius * 2)
    # draw_flower_interleaved(bob, radius, 5)
    # move(bob, radius * 2)
    draw_flower(bob, radius*5, 20)


def move(bob, radius):
    bob.seth(0)
    bob.pu()
    bob.fd(radius)
    bob.pd()


def circle(t, r):
    """Draws a circle with the given radius.

    t: Turtle
    r: radius
    """
    arc(t, r, 360)


def draw_turtle_pie(bob, radius, n):
    angle = 360 / n
    for _ in range(n):
        draw_triangle(bob, radius, angle)
        bob.lt(angle)

# the following condition checks whether we are
# running as a script, in which case run the test code,
# or being imported, in which case don't.


def draw_triangle(bob, radius, angle):
    a2_b2 = 2 * radius**2
    two_ab = 2 * radius**2
    cos_g = math.cos(math.radians(angle))

    c = math.sqrt(a2_b2 - two_ab * cos_g)

    small_angle = (180 - angle) / 2

    bob.lt(180 - angle)
    bob.fd(radius)
    bob.lt(180 - small_angle)
    bob.fd(c)
    bob.lt(180 - small_angle)
    bob.fd(radius)


if __name__ == "__main__":
    bob = turtle.Turtle()
    radius = 100
    draw_flowers(bob, 100)

    # move(bob, -7*radius)
    # bob.speed("slowest")
    # draw_turtle_pie(bob, 100, 5)
    # move(bob, 3*radius)
    # bob.speed("slow")
    # draw_turtle_pie(bob, 100, 7)
    # move(bob, 3*radius)
    # bob.speed("normal")
    # draw_turtle_pie(bob, 100, 9)
    # move(bob, 3*radius)
    # bob.speed("fast")
    # draw_turtle_pie(bob, 100, 11)
    # move(bob, 3*radius)
    # bob.speed("fastest")
    # draw_turtle_pie(bob, 100, 13)

    # wait for the user to close the window
    turtle.mainloop()
