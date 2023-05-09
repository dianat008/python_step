import math
def comb(n, k):
    if n<k:
        return 0
    r=math.factorial(n-k)
    n=math.factorial(n)
    k=math.factorial(k)
    x=n/(r*k)
    x=int(x)
    return x