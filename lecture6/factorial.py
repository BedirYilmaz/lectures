def fac(p):

    if p == 1:
        return 1

    return fac(p-1) * p


def fac(p):
    if p == 1:
        return 1
    return p * fac(p-1)     


print(type(fac(5)))