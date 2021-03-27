"""
project euler 35
https://projecteuler.net/problem=35
by: Nir
Circular primes
"""

lim = 1000000

import math


def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1, 1):
        if n % i == 0:
            return False
    return True


def get_circular_primes(limit):
    circular_primes = set()
    for n in range(2, limit, 1):
        if n in circular_primes:
            continue
        elif is_prime(n):
            all_prime = True
            circular = []
            n_as_string = str(n)
            for i in range(len(n_as_string)):
                p = n_as_string[i:] + n_as_string[:i]
                if is_prime(int(p)):
                    circular.append(int(p))
                else:
                    all_prime = False
                    break
            if all_prime:
                circular_primes.update(circular)
    return circular_primes



def main():
    
    print(len(get_circular_primes(lim)))


if __name__ == "__main__":
    main()
