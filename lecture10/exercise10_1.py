# Write a function called nested_sum that takes a list of lists of integers and adds up
# the elements from all of the nested lists. For example:

# >>> t = [[1, 2], [3], [4, 5, 6]]
# >>> nested_sum(t)
# 21

def nested_sum(t):
    sum_of_lists = 0
    for li in t:
        for num in li:
            sum_of_lists = sum_of_lists + num
    return sum_of_lists

print(nested_sum([[1,2,3,4,5,6,7],[1,2],[1],[0]]))