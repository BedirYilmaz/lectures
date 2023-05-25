# Exercise 5.2 Fermats Last Theorem 


def check_fermat(a, b, c, n):
    if n > 2 and a**n + b**n == c**n:
        print("Holy smokes, Fermat was wrong")
    else:
        print("No, that doesn't work")


def prompt_and_check_fermat():
    a = int(input("Enter a value for 'a': "))
    b = int(input("Enter a value for 'b': "))
    c = int(input("Enter a value for 'c': "))
    n = int(input("Enter a value for 'n': "))
    check_fermat(a, b, c, n)


prompt_and_check_fermat()
