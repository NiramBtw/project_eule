"""
project euler 29
https://projecteuler.net/problem=29
by: Nir 
Distinct powers
"""


def compute():
	seen = set(a**b for a in range(2, 101) for b in range(2, 101))
	return str(len(seen))


if __name__ == "__main__":
	print(compute())







