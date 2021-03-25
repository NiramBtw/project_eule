"""
project euler 25
https://projecteuler.net/problem=25
by: Nir
Lexicographic permutations
https://docs.python.org/3/library/time.html
https://www.tutorialspoint.com/python/time_time.htm
"""
import time


start_time = time.time()
desir_num_of_digi = 1000

index = 3
a = 1
b = 2
c = a + b
while len(str(c)) < desir_num_of_digi:
    c = a + b
    a = b
    b = c
    index += 1


print(index)
print("--- %s seconds ---" % (time.time() - start_time))



