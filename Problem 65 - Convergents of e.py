"""
project euler 65
https://projecteuler.net/problem=65
by: Nir
Convergents of e
"""


def compute():
    num = 1
    den = 0
    for i in reversed(range(100)):
        num, den = e_term(i) * num + den, num
    ans = sum(int(c) for c in str(num))
    return str(ans)


def e_term(i):
    if i == 0:
        return 2
    elif i % 3 == 2:
        return i // 3 * 2 + 2
    else:
        return 1


if __name__ == "__main__":
    print(compute())
