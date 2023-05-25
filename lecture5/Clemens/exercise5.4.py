# code example

def recurse(n, s):
    """
    A function that prints out the numbers that are smaller from the n plus the s.

    args
    n: number to count down from
    s: base number that will be accumulated with the cumulative sum

    return:
    None
    """

    if n == 0:
        print(s)
    else: 
        recurse(n-1, n+s)
    
recurse(1, 0)

"""
n = 1
s = 0

---
**************
n = 0       **
s = 1       **
**************
---

"""