import turtle


def koch(t, length):
    if length < 3:
        t.fd(length)
        return
    koch(t, length/3)
    t.lt(60)
    koch(t, length/3)
    t.rt(120)
    koch(t, length/3)
    t.lt(60)
    koch(t, length/3)


bob = turtle.Turtle()

# bob.seth(90)
# bob.setpos((0,1000))
koch(bob, 100)
bob.rt(120)
koch(bob, 100)
bob.rt(120)
koch(bob, 100)

turtle.mainloop()
