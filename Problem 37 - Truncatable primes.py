"""
project euler 37
https://projecteuler.net/problem=37
by: Nir
Truncatable primes
"""

import math

num_of_truncatable_primes = 11


def Get_truncatable_primes():
    n = 10
    tractable_primes = []
    while len(tractable_primes) < num_of_truncatable_primes:
        all_primes = True
        if Is_prime(n):
            n_as_string = str(n)
            for i in range(1, len(n_as_string), 1):
                r = int(n_as_string[:i])
                l = int(n_as_string[i:])
                if not Is_prime(r) or not Is_prime(l):
                    all_primes = False
                    break
            if all_primes:
                tractable_primes.append(n)
        n += 1
    return tractable_primes

def Is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1, 1):
        if n % i == 0:
            return False
    return True


def Get_truncate_from_Right(n):
    n_as_string = str(n)
    for i in range(1, len(n_as_string), 1):
        yield int(n_as_string[:i])


def Get_truncate_from_Left(n):
    n_as_string = str(n)
    for i in range(1, len(n_as_string), 1):
        yield int(n_as_string[i:])



def main():
    
    print(sum(Get_truncatable_primes()))


if __name__ == "__main__":
    main()
