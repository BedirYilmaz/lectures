# Write a function called chop that takes a list, modifies it by removing the first and
# last elements, and returns None. For example:
# >>> t = [1, 2, 3, 4]
# >>> chop(t)
# >>> t
# [2, 3]


def chop(t):
    del t[0]
    del t[-1]

list_to_remove = [1,2,3,4,5,6,7]
chop(list_to_remove)
print(list_to_remove)