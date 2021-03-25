"""
project euler 24
https://projecteuler.net/problem=24
by: Nir
Lexicographic permutations
https://docs.python.org/3/library/itertools.html
https://www.geeksforgeeks.org/python-itertools-permutations/
"""
import itertools

digits = '0123456789'
premutation_num = 1000000

def get_prem(word, n):
    i = 0
    x = ''
    for p in itertools.permutations(word, len(word)):
        x = ''.join(p)
        i += 1
        if i == n:
            break
    return x


def main():

    print(get_prem(digits, premutation_num))

if __name__ == "__main__":
    main()
    