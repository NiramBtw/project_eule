"""
project euler 58
https://projecteuler.net/problem=58
by: Nir
Spiral primes
https://www.geeksforgeeks.org/numpy-sqrt-in-python/
"""

import numpy as np

def isPrime(n):
    if (n<2):
        return 0
    else:
        ct = 0
        for i in range(2, int(np.sqrt(n))+1):
            if (n%i == 0):
                break
            else:
                ct = ct+1
        if (ct == (int(np.sqrt(n))-1)):
            return 1
        else:
            return 0

Layer = 10**9
Tn = 1
Tp = 0
for i in range(1, Layer):
    tp = 0
    for j in range(4):
        if (isPrime((1+2*i)**2-(2*i)*j) == 1):
            tp = tp+1
    Tn = Tn+4
    Tp = Tp+tp

    if ((Tp/Tn) < 0.1):        
        print((i+1)*2-1)
        break