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


def circle(t, r):
    """Draws a circle with the given radius.

    t: Turtle
    r: radius
    """
    arc(t, r, 360)


def draw_leaf(bob, radius, arc_angle):
    arc(bob, radius, arc_angle)
    bob.lt(180 - arc_angle)
    arc(bob, radius, arc_angle)


def draw_hat(bob, radius, arc_angle):
    arc(bob, radius, arc_angle)
    bob.lt(90 - arc_angle)
    arc(bob, radius, arc_angle)
    bob.lt(135 - arc_angle)
    arc(bob, int(radius * 1.5), arc_angle)


def draw_flower(bob, radius, num_leaves):
    interleaf_angle = int(360 / num_leaves)
    arc_angle = int(360 / num_leaves)
    for _ in range(num_leaves):
        draw_leaf(bob, radius, arc_angle)
        if num_leaves % 2 == 1:
            bob.lt(180 + interleaf_angle)
    return arc_angle


def move(radius):
    bob.seth(0)
    bob.pu()
    bob.fd(radius)
    bob.pd()


def draw_flower_interleaved(bob, radius, leaf_freq):
    lf1 = leaf_freq // 2
    lf2 = leaf_freq - lf1
    print(lf1, lf2)
    ang = draw_flower(bob, radius, lf1)
    bob.rt(int(ang / 2))
    # bob.rt(20)
    draw_flower(bob, radius, lf2)


def draw_flowers(radius):
    move(-radius * 2)
    draw_flower(bob, radius, 7)
    move(radius * 2)
    draw_flower_interleaved(bob, radius, 10)
    move(radius * 2)
    draw_flower(bob, radius * 3, 20)


def draw_triangle(bob, radius, large_angle):
    small_angle = (180 - large_angle) // 2
    ab = radius**2
    cos_y = math.cos(math.radians(large_angle))
    a2_b2 = radius**2
    c = math.sqrt(2 * a2_b2 - 2 * ab * cos_y)

    bob.lt(180 - large_angle)
    bob.fd(radius)
    bob.lt(180 - small_angle)
    bob.fd((c))
    bob.lt(180 - small_angle)
    bob.fd(radius)


def draw_turtle_pie(bob, radius, n):
    angle = math.floor(360 / n)
    for _ in range(n):
        draw_triangle(bob, radius, angle)
        bob.lt(angle)


def draw_turtle_pies(bob, radius):
    move(-radius * 2)
    draw_turtle_pie(bob, radius, 5)
    move(radius * 2)
    draw_turtle_pie(bob, radius, 6)
    move(radius * 3)
    draw_turtle_pie(bob, radius, 7)


# the following condition checks whether we are
# running as a script, in which case run the test code,
# or being imported, in which case don't.


if __name__ == "__main__":
    bob = turtle.Turtle()
    bob.speed("fastest")
    radius = 100
    arc_angle = 45
    # draw_turtle_pies(bob, radius)
    # draw_turtle_pies(radius)

    draw_flower_interleaved(bob, 100, 10)

    # wait for the user to close the window
    turtle.mainloop()
