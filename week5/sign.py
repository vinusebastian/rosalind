import itertools
n=raw_input()
n=int(n)
a=[]
x=[]
z=[]
for i in range(1,n+1):
    a.append(i)
    a.append(-i)
x=list(itertools.permutations(a,n))
for l in x:
    check=0
    a=[]
    for k in range(len(l)):
        if l[k]<0:
          a.append(l[k]*-1)
        else:
          a.append(l[k])
    #print a
    
    if len(a)==len(set(a)):
        z.append(l)
print len(z)
for o in z:
    for q in o:
       print q,
    print
         
         
