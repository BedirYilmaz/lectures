def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n-1)


# countdown(10)

# for i in range(10, -1, -1):
#     if i <= 0:
#         print('Blastoff!!')
#         break
#     print(i)


# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89

def fib(index):
    if index <= 1:
        return index
    return fib(index - 1) + fib(index - 2)


print(fib(8))

j = 0
k = 1

for i in range(7, 0, -1):
    n = j + k
    if i <= 1:
        print(n)
    else:
        j, k = k, n
