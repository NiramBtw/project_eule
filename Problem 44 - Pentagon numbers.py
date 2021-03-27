"""
project euler 44
https://projecteuler.net/problem=44
by: Nir
Pentagon numbers
"""

import itertools


def compute():
    pentanum = PentagonalNumberHelper()
    min_d = None  # none means not found yet, positive number means found a candidate
    # for each upper pentagonal number index, going upward
    for i in itertools.count(2):
        pent_i = pentanum.term(i)
        # if the next number down is at least as big as a found difference, then conclude searching
        if min_d is not None and pent_i - pentanum.term(i - 1) >= min_d:
            break

        # for each lower pentagonal number index, going downward
        for j in range(i - 1, 0, -1):
            pent_j = pentanum.term(j)
            diff = pent_i - pent_j
            # if the difference is at least as big as a found difference, then stop testing lower pentagonal numbers
            if min_d is not None and diff >= min_d:
                break
            elif pentanum.is_term(pent_i + pent_j) and pentanum.is_term(diff):
                min_d = diff  # found a smaller difference
    return str(min_d)


# provide memoization for generating and testing pentagonal numbers.
class PentagonalNumberHelper:
    def __init__(self):
        self.term_list = [0]
        self.term_set = set()

    def term(self, x):
        assert x > 0
        while len(self.term_list) <= x:
            n = len(self.term_list)
            term = (n * (n * 3 - 1)) >> 1
            self.term_list.append(term)
            self.term_set.add(term)
        return self.term_list[x]

    def is_term(self, y):
        assert y > 0
        while self.term_list[-1] < y:
            n = len(self.term_list)
            term = (n * (n * 3 - 1)) >> 1
            self.term_list.append(term)
            self.term_set.add(term)
        return y in self.term_set


if __name__ == "__main__":
    print(compute())