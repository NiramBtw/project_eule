"""
project euler 12
by: Nir
Highly divisible triangular number
https://docs.python.org/3/library/argparse.html
"""


import argparse
import math


def main(args):
# highly divisible triangular numbe
    ordinal = 1
    triangle_number = 1
    num_factors = 1
    while num_factors <= args.divisors:
        ordinal += 1
        triangle_number += ordinal
        num_factors = len(get_factors(triangle_number))
    print(triangle_number)


def get_factors(number):
    
    factors = [1, number]
    for i in range(2, int(math.sqrt(number))):
        if number % i == 0:
            factors.extend([i, number / i])
    return(factors)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('divisors', metavar='DIVISORS', type=int, default=500, nargs='?')
    args = parser.parse_args()
    main(args)
