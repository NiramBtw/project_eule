"""
project euler 21
https://projecteuler.net/problem=21
by: Nir
Amicable numbers

1. compute a table of sum-of-proper-divisors.
2. then use it to test which numbers are amicable.
3. compute the proper-divisor-sum of each number.
"""

def compute():
    # the sum of proper divisors for each number
    divisorsum = [0] * 10000
    for i in range(1, len(divisorsum)):
        for j in range(i * 2, len(divisorsum), i):
            divisorsum[j] += i

    # get all amicable pairs in range
    ans = 0
    for i in range(1, len(divisorsum)):
        j = divisorsum[i]
        if j != i and j < len(divisorsum) and divisorsum[j] == i:
            ans += i
    return str(ans)


if __name__ == "__main__":
    print(compute())
