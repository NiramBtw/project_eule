"""
project euler 1
by: Nir
Multiples of 3 and 5
"""

def sum_and_div_35(to=int(input("add ur num"))):
    result = 0
    for i in range(1, to):
        if i % 3 == 0 or i % 5 == 0:
            result += i
    return result


print(sum_and_div_35())
