"""
project euler 60
https://projecteuler.net/problem=60
by: Nir
Prime pair sets
"""

N = 10**3

ct = 0
for n in range(1, 10):
    for m in range(1, N):
        l = len(str(n**m))
        if (l > m):
            break
        elif (l==m):
            ct = ct+1

print(ct)