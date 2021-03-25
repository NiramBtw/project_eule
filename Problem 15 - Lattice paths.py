"""
project euler 15
https://projecteuler.net/problem=15
by: Nir
Lattice paths
https://www.includehelp.com/python/math-factorial-method-with-example.aspx

combinatorics problem- need to get from the top left
corner to the bottom right corner of an N*N grid.
making N moves right and N moves down in some order.
because each individual down or right move
cannot be distinguished, there are exactly 2N choose N
binomial coefficient ways of arranging these moves.
"""


N = 20

from math import factorial


def pick(n, k):
    return factorial(n) // factorial(k) // factorial(n - k)


def get_num_lattice_opt(n):
    return pick(2 * n, n)


def main():
    print(get_num_lattice_opt(N))


if __name__ == "__main__":
    main()
