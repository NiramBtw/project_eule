"""
project euler 9
by: Nir
Special Pythagorean triplet
"""


def compute():
    perimeter = 1000
    for a in range(1, perimeter + 1):        
        for b in range(a + 1, perimeter + 1):            
            c = perimeter - a - b
            if a * a + b * b == c * c:                
                 # now implied that b < c, because having a > 0
                return str(a * b * c)


if __name__ == "__main__":
     print(compute())


