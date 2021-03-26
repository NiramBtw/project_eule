"""
project euler 34
https://projecteuler.net/problem=34
by: Nir
Digit factorials
"""

import math


def compute():
    # 1 = 1! and 2 = 2! are excluded.
    # if a number has at least n >= 8 digits, then even if every digit is 9,
    # n * 9! is still less than the number (which is at least 10^n).
    ans = sum(i for i in range(3, 10000000) if i == factorial_digit_sum(i))
    return str(ans)


def factorial_digit_sum(n):
    result = 0
    while n >= 10000:
        result += factorial_digits_sum_with_leading_0[n % 10000]
        n //= 10000
    return result + factorial_digits_sum_out_leading_0[n]


factorial_digits_sum_out_leading_0 = [sum(math.factorial(int(c)) for c in str(i)) for i in range(10000)]
factorial_digits_sum_with_leading_0 = [sum(math.factorial(int(c)) for c in str(i).zfill(4)) for i in range(10000)]

if __name__ == "__main__":
    print(compute())

