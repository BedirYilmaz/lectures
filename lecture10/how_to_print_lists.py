l = [1,2,3,4,5,6,7,8,9]

print(l)

# for i in l:
#     print(i, end=" ")

# l_str = ["1","2","3","4","5","6","7","8","9"]

# print(" ".join(l_str))

def power_of_2(number):
    return number**2

print(" ".join(map(str, map(power_of_2, l))))