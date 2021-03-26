"""
project euler 32
https://projecteuler.net/problem=32
by: Nir
Pandigital products
"""
import itertools


digits = "123456789"

def get_pandigital_products(word):
    x = ""
    products = set()
    length = len(word)
    for p in itertools.permutations(word, ):
        x = "".join(p)
        multiplicandSmallerThenProduct = True
        for ai in range(1, length):
            if not multiplicandSmallerThenProduct:
                break
            a = x[:ai]
            for bl in range(1, length - ai):
                b = x[ai:(ai + bl)]
                c = x[(ai + bl):]
                if len(a) > len(c):
                    multiplicandSmallerThenProduct = False
                    break
                if int(a) * int(b) == int(c):
                    products.update([int(c)])
    return products


def main():
   
    print(sum(get_pandigital_products(digits)))


if __name__ == "__main__":
    main()
