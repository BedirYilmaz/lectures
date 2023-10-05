# Write a function called middle that takes a list and returns a new list that contains
# all but the first and last elements. For example:
# >>> t = [1, 2, 3, 4]
# >>> middle(t)
# [2, 3]

def middle(t):
    
    return [t[0], t[-1]]

print(middle([1,2,3,4,5,6,7]))