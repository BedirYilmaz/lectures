def is_odd(number):
    return number % 2 == 1

l = [1,2,6,3,7,8,9,4,5]

l2 = [5667,56,545]

print(sorted(l, reverse=True))
l.sort()
l.extend(l2)
print(l)


print(list(filter(is_odd, l)))
