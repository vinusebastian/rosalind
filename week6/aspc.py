import math
def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)
string=raw_input()
n,m=string.split()
n=int(n)
m=int(m)
ans=0
for i in range(m,n+1):
    ans=(ans+(nCr(n,i))%1000000)%1000000
print ans
