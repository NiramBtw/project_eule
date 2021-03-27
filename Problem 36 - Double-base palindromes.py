"""
project euler 36
https://projecteuler.net/problem=36
by: Nir
Double-base palindromes
"""
lim = 1000000


def is_palindrom(n):
    return str(n) == str(n)[::-1]


def decimal_to_binary(d):
    return "{0:#b}".format(d)[2:]


def get_d_based_palindroms(limit):
    d_based_palindrome = []
    for n in range(1, limit, 1):
        if is_palindrom(n) and is_palindrom(decimal_to_binary(n)):
            d_based_palindrome.append(n)
    return d_based_palindrome



def main():
    
    print(sum(get_d_based_palindroms(lim)))


if __name__ == "__main__":
    main()
