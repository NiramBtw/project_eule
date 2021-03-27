"""
project euler 41
https://projecteuler.net/problem=41
by: Nir
Pandigital prime
https://www.geeksforgeeks.org/python-itertools-permutations/
"""

import math
import itertools

digi = '123456789'


def Is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1, 1):
        if n % i == 0:
            return False
    return True

def Get_premutation(word):
    for p in itertools.permutations(word, len(word)):
        yield ''.join(p)

def Get_Max_pandigital_prime():
    current_digits = digi
    while current_digits != "":
        maximal_pandigital = 0
        for p_as_string in Get_premutation(current_digits):
            p = int(p_as_string)
            if Is_prime(p) and maximal_pandigital < p:
                maximal_pandigital = p
        current_digits = current_digits[:(len(current_digits) - 1)]
        if 0 != maximal_pandigital:
            return maximal_pandigital
    return 0


def main():
    
    
    print(Get_Max_pandigital_prime())
    
if __name__ == "__main__":
    main()