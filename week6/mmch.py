import math
def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)
f1=open('mmch_in.txt','r')
a=f1.read().split('>')
lis=a[1:]
string=lis[0].replace('\n','')[13:]
a=u=c=g=0
for i in string:
     if i=='A':
         a+=1
     elif i=='U':
         u+=1
     elif i=='C':
         c+=1
     elif i=='G':
         g+=1
#print a,u,g,c
if a<u:
   diff1=u-a
   min1=a
else:
   diff1=a-u
   min1=u
if c<g:
   diff2=g-c
   min2=c
else:
   diff2=c-g
   min2=g
   
print math.factorial(min1)*math.factorial(min2)*nCr(diff1+min1,min1)*nCr(diff2+min2,min2) 
