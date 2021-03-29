"""
project euler 62
https://projecteuler.net/problem=62
by: Nir
Cubic permutations
"""

import itertools


def compute():
    num_digits = 0
    data = {}  # str numclass -> int lowest, int count
    for i in itertools.count():
        digits = [int(c) for c in str(i ** 3)]
        digits.sort()
        num_class = "".join(str(d) for d in digits)

        if len(num_class) > num_digits:
            # Process and flush data for smaller number of digits
            candidates = [lowest for (lowest, count) in data.values() if count == 5]
            if len(candidates) > 0:
                return str(min(candidates) ** 3)
            data = {}
            num_digits = len(num_class)

        lowest, count = data.get(num_class, (i, 0))
        data[num_class] = (lowest, count + 1)


if __name__ == "__main__":
    print(compute())
