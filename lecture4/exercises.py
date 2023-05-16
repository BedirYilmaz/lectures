import turtle
import time
import math

# def square(t):
#     for i in range(4):
#         t.fd(100)
#         t.lt(90)


def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)


# def polygon(t, length, n):

#     angle = 360 / n

#     for i in range(n):
#         # time.sleep(0.5)
#         t.fd(length)
#         t.lt(angle)


def polygon(t, length, n, arc=None):
    """
    Draw a polygon using the turtle graphics library.

    Args:
        t (turtle.Turtle): The turtle object to draw with.
        length (int or float): The length of each side of the polygon.
        n (int): The number of sides of the polygon.
        arc (int, optional): The number of sides to draw, forming an arc. If not provided,
            the default value is set to `n`, resulting in drawing a complete polygon. 
            Defaults to None.

    Returns:
        None

    Raises:
        None

    Example:
        # Create a turtle object
        t = turtle.Turtle()

        # Draw a complete hexagon with sides of length 100 units
        polygon(t, 100, 6)

        # Draw a quarter circle with radius of 50 units
        polygon(t, 3.14 * 50, 100, 25)

    Notes:
        - The turtle will start drawing from the current position and heading of the turtle object `t`.
        - The turtle will move forward by `length` units for each side of the polygon.
        - The angle between each side of the polygon is calculated as 360 divided by the number of sides `n`.
        - If `arc` is not provided, the function will default to drawing a complete polygon with `n` sides.
        - If `arc` is provided, the function will draw only `arc` sides of the polygon, forming an arc.
        - The turtle will turn left by the calculated angle after drawing each side to create the polygon shape.
        - The turtle will pause for 0.5 seconds after drawing each side using the `time.sleep()` function from the `time` module.
    """

    if arc is None:
        arc = n

    angle = 360 / n

    for i in range(arc):
        time.sleep(0.5)
        t.fd(length)
        t.lt(angle)


def circle(t, r):
    circumference = math.pi * (r / 2)
    polygon(t, circumference / 100, 100)


def arc(t, r, angle):
    circumference = math.pi * (r / 2)
    polygon(t, circumference / 360, 360, angle)


bob = turtle.Turtle()

# square(bob, 20)
# polygon(bob, 100, 8)
arc(bob, 400, 90)
time.sleep(5)
