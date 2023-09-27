def is_palindrome(word):
    return word[::-1] == word

l = [1,2,6,3,7,8,9,4,5]

print([i**2 for i in l if i % 2 == 1])

print([(is_palindrome(str(i)), i) for i in range(100000, 999999) if is_palindrome(str(i))])