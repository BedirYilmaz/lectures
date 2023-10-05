# Write a function called cumsum that takes a list of numbers and returns the cumulative
# sum; that is, a new list where the ith element is the sum of the first i + 1 elements from the
# original list. For example:
# >>> t = [1, 2, 3]
# >>> cumsum(t)
# [1, 3, 6]

def cumsum(t):
    
    res = []
    sum_of_elements = 0
    for i in t:
        sum_of_elements += i
        res.append(sum_of_elements)
    return res

print(cumsum([1,2,3,4,5,6,7]))