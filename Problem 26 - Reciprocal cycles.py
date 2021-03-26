"""
project euler 26
https://projecteuler.net/problem=26
by: Nir
Reciprocal cycles
https://www.geeksforgeeks.org/python-itertools-count/
https://www.programcreek.com/python/example/566/itertools.count
https://realpython.com/python-itertools/
"""
import itertools


def function():
    ans = max(range(1, 1000), key = reciprocal_cycle_len)
    return str(ans)


def reciprocal_cycle_len(n):
    seen = {}
    x = 1
    for i in itertools.count():
        if x in seen:
            return i - seen[x]
        else:
            seen[x] = i
            x = x * 10 % n


if __name__ == "__main__":
    print(function())
