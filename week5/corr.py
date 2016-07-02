import sys
def reversecomp(seq):
     a=''
     for i in seq:
         if i=='A':
             a=a+'T'
         elif i=='T':
             a=a+'A'
         elif i=='C':
             a=a+'G'
         elif i=='G':
             a=a+'C'
     return a[::-1]

def hamm(seq1,seq2):
    count=0
    for i in range(len(seq1)):
         if seq1[i]!=seq2[i]:
             count+=1
    return count
  
         
from collections import defaultdict
d=defaultdict(int)
f=open('corr_in.txt','r')
a=f.read().split('>')
lis=a[1:]
strings=[]
correct=[]
incorrect=[]
for el in lis:
  strings.append(el.replace('\n','')[13:])  
for string in strings:
      reverse=reversecomp(string)
      #print string,reverse  
      d[string]+=1
      d[reverse]+=1
for l in d:
    if d[l]>1:
       correct.append(l)
    else:
       incorrect.append(l)
#print correct
#print incorrect
for i in strings:
     for j in correct:
         #print hamm(i,j), 
         if hamm(i,j)==1:
              #print i,'->',j
              sys.stdout.write(i)
              sys.stdout.write('->')
              sys.stdout.write(j)
              print 
        
         
