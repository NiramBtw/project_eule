"""
project euler 27
https://projecteuler.net/problem=27
by: Nir 
Quadratic primes
"""


import math

ab_abs_val = 1000 - 1 # a b absolute value


def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1, 1):
        if n % i == 0:
            return False
    return True


def quadratics_equation(a, b, x):
    return x ** 2 + a * x + b


def get_con_prime_quad_equ(a, b): # getting consecutive primes of quadratics equation
    n = 0
    primes_counter = 0
    while True:
        p = quadratics_equation(a, b, n)
        if p <= 0 or not is_prime(p):
            break
        else:
            n += 1
            primes_counter += 1
    return primes_counter


def max_con_prime_quad_equ(coef_abs_val): # getting maximal consecutive primes of quadratics equation
    # coefficients absolute value
    max_con_a = 0 #
    max_con_b = 0 #
    max_con_primes = -1 # maximal consecutive of primes
    for a in range(-1 * coef_abs_val, coef_abs_val, 1):
        for b in range(-1 * coef_abs_val, coef_abs_val, 1):
            con_primes = \
                get_con_prime_quad_equ(a, b)
            if con_primes > max_con_primes:
                max_con_primes = con_primes
                max_con_a = a
                max_con_b = b
    return (max_con_a, max_con_b, max_con_primes)


def main():
    max_consecutive = max_con_prime_quad_equ(ab_abs_val)
    print(max_consecutive[0] * max_consecutive[1])



if __name__ == "__main__":
    main()
