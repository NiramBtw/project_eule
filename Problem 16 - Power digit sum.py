"""
project euler 16
https://projecteuler.net/problem=16
by: Nir
Power digit sum
"""


def y():
    n = 2 ** 1000
    x = sum(int(c) for c in str(n))
    return str(x)


if __name__ == "__main__":
    print(y())



