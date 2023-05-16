def draw_leaf(bob, radius, arc_angle):
    arc(bob, radius, arc_angle)
    bob.lt(180-arc_angle)
    arc(bob, radius, arc_angle)


def draw_flower(bob, radius, leaf_freq):
    interleaf_angle = int(360/leaf_freq)
    arc_angle = int(360/(leaf_freq))
    for _ in range(leaf_freq):
        draw_leaf(bob, radius, arc_angle)
        if leaf_freq % 2 == 1:
            bob.lt(180+interleaf_angle)
    return arc_angle


def move(radius):
    bob.seth(0)
    bob.pu()
    bob.fd(radius)
    bob.pd()


def draw_flower_interleaved(bob, radius, leaf_freq):
    lf1= leaf_freq // 2
    lf2= leaf_freq - lf1
    print(lf1, lf2)
    ang = draw_flower(bob, radius, lf1)
    bob.rt(int(ang/2))
    draw_flower(bob, radius, lf2)
   
def draw_flowers():
    move(-radius*2)
    draw_flower(bob, radius, 7)
    move(radius*2)
    draw_flower_interleaved(bob, radius, 10)
    move(radius*2)
    draw_flower(bob, radius*3, 20)