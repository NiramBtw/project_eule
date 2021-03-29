"""
project euler 69
https://projecteuler.net/problem=69
by: Nir
Totient maximum
"""

from math import gcd
import numpy as np


N = 10 ** 6


def isPrime(n):
    if (n < 2):
        return 0
    else:
        ct = 0
        for i in range(2, int(np.sqrt(n)) + 1):
            if (n % i != 0):
                ct = ct + 1
        if (ct == (int(np.sqrt(n)) - 1)):
            return 1
        else:
            return 0


Dl = []
p = 1
for i in range(N):
    if (isPrime(i) == 1):
        p = p * i
        if (p < N):
            Dl.append(p)
        else:
            break


def totientFunction(n, tn, tphi):
    phi_n = 1
    for i in range(3, n, 2):
        if (n / phi_n < tphi):
            return 0
        if (gcd(n, i) == 1):
            phi_n = phi_n + 1
    if (n / phi_n > tphi):
        return [n, n / phi_n]
    else:
        return 0


tn = 0
tphi = 0
for a in Dl:
    if (totientFunction(a, tn, tphi) != 0):
        tn = totientFunction(a, tn, tphi)[0]
        tphi = totientFunction(a, tn, tphi)[1]

print(tn)
