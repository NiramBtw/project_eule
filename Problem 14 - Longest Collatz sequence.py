"""
project euler 14
https://projecteuler.net/problem=14
by: Nir
Longest Collatz sequence
https://docs.python.org/3/library/argparse.html
"""


import argparse


def main(args):
    
    cache = {}
    longest_chain_length = 0
    longest_chain_start = 1
    for start in range(2, args.limit):
        length = 0
        number = start
        while number > 1:
            # Check if rest of chain is cached
            if number in cache:
                length += cache[number]
                break

            length += 1
            if number % 2:
                number = 3 * number + 1
            else:
                number /= 2
        cache[start] = length
        if length > longest_chain_length:
            longest_chain_length = length
            longest_chain_start = start
    print(longest_chain_start)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('limit', metavar='LIMIT', type=int, default=1000000, nargs='?')
    args = parser.parse_args()

    main(args)