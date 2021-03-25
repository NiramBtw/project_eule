"""
project euler 6
by: Nir
Sum square difference
"""


def sum_of(max):
    total = 0
    for x in range(max + 1):
        total += x ** 2
    return total


def square_of(lim):
    total = 0
    for x in range(lim + 1):
        total += x
    return total ** 2


n = square_of(100)
i = sum_of(100)

print(n - i)

