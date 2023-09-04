import math

def find_root(a):
    x = 25
    
    for i in range(x):
        y = (x + a / x) / 2
        x = y

    return x

def test_square_root():

    print("a      mysqrt(a)          math.sqrt(a)     diff")
    print("-      ---------          ------------     ----")

    for i in range(100000):
        result = find_root(i)
        result_lib = math.sqrt(i)
        diff = abs(result - result_lib)
        print(f"{i:.1f}    {result:.13f}    {result_lib:.13f}  {diff:.13f}")


# a = int(input("please type the number you want to find the root of"))
# print(find_root(a))

test_square_root()