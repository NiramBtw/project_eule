"""
project euler 49
https://projecteuler.net/problem=49
by: Nir
Prime permutations
"""
import numpy as np
from itertools import permutations

def isPrime(n):
    if (n<2):
        return 0
    else:
        ct = 0
        for i in range(2, int(np.sqrt(n))+1):
            if (n%i!=0):
                ct = ct+1
        if (ct == (int(np.sqrt(n))-1)):
            return 1
        else:
            return 0

lp = []
for i in range(10**3, 10**4):
    if (isPrime(i)==1):
        lp.append(i)

def permutate(n):
    l = []
    ln = []
    for i in range(len(str(n))):
        l.append(int(str(n)[i]))
    per = permutations(l)
    for i in list(per):
        n2 = int(str(i[0])+str(i[1])+str(i[2])+str(i[3]))
        if (n2 in lp) and (isPrime(n2)==1) and (n2 not in ln):
            ln.append(n2)
    return sorted(ln)

def increaseD(l):
    for i in range(len(l)-2):
        for j in range(i+1, len(l)-1):
            if ((2*l[j]-l[i]) in l):
                return [l[i], l[j], (2*l[j]-l[i])]
    return 0

L = []
for a in lp:
    if (len(permutate(a))>=3):
        if (increaseD(permutate(a))!=0):
            l = increaseD(permutate(a))
            s = str(l[0])
            for i in range(1,len(l)):
                s = s+str(l[i])
            if (s not in L):
                L.append(s)

print(L[1:])