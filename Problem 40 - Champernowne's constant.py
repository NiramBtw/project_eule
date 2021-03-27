"""
project euler 40
https://projecteuler.net/problem=40
by: Nir
Champernowne's constant
https://docs.python.org/3/library/operator.html
https://docs.python.org/3/library/functools.html
"""

import operator
import functools

digi_num = [1, 10, 100, 1000, 10000, 100000, 1000000]


def Get_champernowne_constant_digits(digits_numbers):
    n = 1
    digit_number = 1
    deserted_digits = []
    reverse_deserted_digit_numbers = digits_numbers[::-1]
    current_deserted_digit_number = reverse_deserted_digit_numbers.pop()
    while 0 != len(reverse_deserted_digit_numbers):
        n_as_string = str(n)
        for d in n_as_string:
            if digit_number == current_deserted_digit_number:
                deserted_digits.append(int(d))
                if 0 == len(reverse_deserted_digit_numbers):
                    break
                current_deserted_digit_number = reverse_deserted_digit_numbers.pop()
            digit_number += 1
        n += 1
    return deserted_digits



def main():
    
    print(functools.reduce(operator.mul, Get_champernowne_constant_digits(digi_num), 1))


if __name__ == "__main__":
    main()
