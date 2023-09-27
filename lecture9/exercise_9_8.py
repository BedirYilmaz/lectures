# a function to check whether a string is a palindrome
def is_palindrome(word):
    return word[::-1] == word

# a function to check multiple increments against palindromeness
def is_increasingly_palindromic(number):
    number_str = str(number)
    last_four = number_str[-4:]
    is_last_four_palindromic = is_palindrome(last_four)
    
    number_increased_str = str(number + 1)
    last_five = number_increased_str[-5:]
    is_last_five_palindromic = is_palindrome(last_five)
    
    number_double_increased_str = str(number + 2)
    middle_four = number_double_increased_str[1:-1]
    is_middle_four_palindromic = is_palindrome(middle_four)
    
    number_triple_increased_str = str(number + 3)
    
    return is_last_four_palindromic and is_last_five_palindromic and is_middle_four_palindromic and is_palindrome(number_triple_increased_str)


# loop over all six digit numbers
for i in range(100000, 999999):    
    #  check the increments against palindromeness
    if is_increasingly_palindromic(i):
        print(f"YEAH WE FOUND IT :{i}")
        number_str = str(i)
        number_str_1 = str(i+1)
        number_str_2 = str(i+2)
        number_str_3 = str(i+3)
        print(number_str[-4:], number_str_1[-5:], number_str_2[1:-1], number_str_3)