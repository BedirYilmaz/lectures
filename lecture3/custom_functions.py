def print_two_times_back_to_back():
    print("hey")
    print("hey")


print_two_times_back_to_back()


def display_my_integer(param_int):
    print(param_int)


def display_sqrt_of_my_integer(param_int):
    print(param_int**(1/2))


# print_two_times_back_to_back()
display_my_integer(3)
print(display_my_integer)


def use_function(func, variable_int):
    func(variable_int)


use_function(display_my_integer, 2)
use_function(display_sqrt_of_my_integer, 2)
