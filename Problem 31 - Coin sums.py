"""
project euler 31
https://projecteuler.net/problem=31
by: Nir
Coin sums
"""

def function():
    total = 200

    # at the start of each loop -> ways[i] is the number of ways to use ,any copies
    # of all the coin values seen before this iteration, to form an unordered sum of i.
    ways = [1] + [0] * total
    for coin in [1, 2, 5, 10, 20, 50, 100, 200]:
        for i in range(len(ways) - coin):
            ways[i + coin] += ways[i]
    return str(ways[-1])


if __name__ == "__main__":
    print(function())
