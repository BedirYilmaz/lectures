import math


def degenerator(radians):
    return math.degrees(radians)


def is_male(user):
    return False


val = degenerator(math.pi / 8)

return_from_print = print(val)

print(return_from_print)


if val > 90:
    print("this is a wide angle")
else:
    print("whatever")


if is_male(23123):
    print("yes he is")
else:
    print("nope she isnt")