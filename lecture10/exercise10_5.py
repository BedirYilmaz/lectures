# Write a function called is_sorted that takes a list as a parameter and returns True
# if the list is sorted in ascending order and False otherwise. For example:
# >>> is_sorted([1, 2, 2])
# True
# >>> is_sorted(['b', 'a'])
# False


def is_sorted(t):
    return t == sorted(t)

list_to_remove = [1,2,3,4,5,6,7]

assert is_sorted(list_to_remove) == True