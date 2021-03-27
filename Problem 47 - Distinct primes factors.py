"""
project euler 47
https://projecteuler.net/problem=47
by: Nir
Distinct primes factors
"""
import time

Tl = 4
T = time.time()
 
def decompose(n):
    n0 = n
    l = []
    a = 1
    while a:
        for i in range(2, n0+1):
            if (n%i==0):
                if i not in l:
                    l.append(i)
                    if (len(l) > Tl):
                        return 0
                n = n/i
                break
        if (n==1):
            if (len(l)==Tl):
                return 1
            else:
                return 0
        
c = 0
n2 = 0
for i in range(2, 10**9):
    if (decompose(i)==1):
        if (i-n2 == 1):
            c = c+1
        else:
            c = 0
        n2 = i
    if (c==Tl-1):
        break

print(i-Tl+1)
