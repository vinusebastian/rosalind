from collections import defaultdict
import collections
import itertools
f1=open('kmer_in.txt','r')
a=f1.read().split('>')
lis=a[1:]
seq=lis[0].replace('\n','')[13:]
string=seq[0:3]
d=defaultdict(int)
a=[p for p in itertools.product(['A','C','G','T'],repeat=4)]

 
for i in a:
    x=''
    for j in i:
        x=x+j
    #print x
    if len(x)==4:
      d[x]=0

for i in range(0,len(seq)-3):
      string=seq[i:i+4]
      d[string]+=1
d=collections.OrderedDict(sorted(d.items()))
for i in d:
   print d[i],
 

