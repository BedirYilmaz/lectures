def is_triangle(a, b, c):
    if a > b + c or b > a + c or c > a + b:
        print("No, it's not a triangle!")
    else:
        print("Yes, it's a triangle!")


def prompt_and_check_triangle():
    a = int(input("Enter the length of the first stick: "))
    b = int(input("Enter the length of the second stick: "))
    c = int(input("Enter the length of the third stick: "))
    is_triangle(a, b, c)


prompt_and_check_triangle()