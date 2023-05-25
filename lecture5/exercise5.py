import turtle
import time

def draw_koch(t, length):

    if length < 10:
        t.fd(length)
        return
    
    draw_koch(t, length / 3)
    t.lt(60)
    draw_koch(t, length / 3)
    t.rt(120)
    draw_koch(t, length / 3)
    t.lt(60)
    draw_koch(t, length / 3)


def move(bob, radius):
    bob.seth(0)
    bob.pu()
    bob.lt(160)
    bob.fd(radius)
    bob.pd()
    bob.seth(0)


bob = turtle.Turtle()

time.sleep(25)
move(bob, radius=300)
draw_koch(bob, 600)
bob.rt(120)
draw_koch(bob, 600)
bob.rt(120)
draw_koch(bob, 600)

turtle.mainloop()
