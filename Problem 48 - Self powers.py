"""
project euler 48
https://projecteuler.net/problem=48
by: Nir
Self powers
"""
def compute():
    MOD = 10 ** 10
    ans = sum(pow(i, i, MOD) for i in range(1, 1001)) % MOD
    return str(ans)


if __name__ == "__main__":
    print(compute())
