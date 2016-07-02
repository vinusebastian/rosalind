import math
from math import log10

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

n=raw_input()
n=int(n)
a=pow(2,2*n)
b=a


for i in range(2*n):
    a-=nCr(2*n,i)
    
  
    print int(log10(a/(1.0*b))*1000)/1000.000,
    
