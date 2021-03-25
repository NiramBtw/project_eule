"""
project euler 5
by: Nir
smallest multiple
"""

def cheak(x):
    for y in range(11, 21):
        if x % y == 0:  # x div evenly -> by current num
            continue
        else:
            return False
    return True

n = 2520

while not cheak(n):
    n += 2520

print(n)
