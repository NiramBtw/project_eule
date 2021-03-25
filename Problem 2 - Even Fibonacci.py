"""
project euler 2
by: Nir
Even Fibonacci numbers
"""

def fib(to=10):
    a = 1
    b = 2
    for x in range(to):

        #print(b)
        a, b = b , a+b

fib()


# generat fib

fibNums = [1,2]
#while True:
while fibNums[-1] < 4000000:
     fibNums.append(fibNums[-1]+ fibNums[-2])

#print(fibNums)
del fibNums[-1]
#print(fibNums)

sum_fibNum = 0
for fibNum in fibNums:
    if fibNum % 2 == 0:
        sum_fibNum += fibNum

print(sum_fibNum)
