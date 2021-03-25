"""
project euler 3
by: Nir
Largest prime factor - 600851475143 
"""

x = 600851475143


def prime(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


for i in range(2, x + 1):
    if prime(i) and x % i == 0:
        print(i)