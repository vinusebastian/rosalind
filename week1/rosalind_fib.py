n,k=raw_input().split()
n=int(n)
k=int(k)
a=1
b=1
s=0
for i in range(2,n):
   s=k*a+b
   a=b
   b=s
print s    
