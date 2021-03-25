"""
project euler 10
by: Nir
Summation of primes
"""

N = 2000000

import math


def IsPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1, 1):
        if n % i == 0:
            return False
    return True


def main():
    primes = [2]
    for n in range(3, N, 2):
        if IsPrime(n):
            primes.append(n)

    print(sum(primes))


if __name__ == "__main__":
    main()





