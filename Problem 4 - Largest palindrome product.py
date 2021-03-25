"""
project euler 4
by: Nir
Largest palindrome product 
"""


def pal(x):
    x = str(x)
    i = int(len(x) / 2)
    a = x[0:i]
    b = x[i:]
    b = b[::-1]
    if a == b:
        return True


pal_list: list = []

for y in range(100, 1000):
    for n in range(100, 1000):
        if pal(y * n):
            pal_list.append(y * n)

pal_list.sort()
print(pal_list[-1])
