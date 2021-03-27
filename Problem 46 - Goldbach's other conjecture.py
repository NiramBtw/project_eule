"""
project euler 46
https://projecteuler.net/problem=46
by: Nir
Goldbach's other conjecture
"""
import math


def Is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1, 1):
        if n % i == 0:
            return False
    return True


def Is_composite(n):
    return not Is_prime(n)


class PowersDictionary:
    def __init__(self):
        self.d = dict()

    def GetPower(self, n):
        p = self.d.get(n)
        if p is None:
            self.d[n] = n ** 2
        return self.d[n]


def Get_goldbach_representation(c, powers):
    for n in range(c):
        p = c - 2 * powers.GetPower(n)
        if p <= 0:
            continue
        if Is_prime(p):
            return p, n
    return None


def Get_first_composite_out_goldbach_representation():
    c = 9
    powers = PowersDictionary()
    golda_representation = Get_goldbach_representation(c, powers)
    while golda_representation is not None:
        c += 2
        while Is_prime(c):
            c += 2
        golda_representation = Get_goldbach_representation(c, powers)
    return c



def main():
    
    print(Get_first_composite_out_goldbach_representation())


if __name__ == "__main__":
    main()
