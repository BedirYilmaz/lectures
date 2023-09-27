def gerisayim(n):

    if n == 0:
        return

    print(n)
    gerisayim(n-1)

# nth fib number
def fibonacci(n):
    if n == 1:
        return 1
    elif n == 0:
        return 1
    
    return fibonacci(n-1) + fibonacci(n-2) 
    
def fibonaccis(n):
    if n == 0:
        return
    res = fibonacci(n)
    print(fibonacci(n), res / fibonacci(n-1))
    fibonaccis(n-1)

fibonaccis(25)

# print(fibonacci(6))

# gerisayim(10)