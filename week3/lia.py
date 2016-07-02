import math

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)
k,n=raw_input().split()
k=int(k)
n=int(n)
l=pow(2,k)
summ=0
for i in range(n,l+1):
      summ+=0.0+pow((3/4.0),l-i)*pow((1/4.0),i)*nCr(l,i)
      
print summ
