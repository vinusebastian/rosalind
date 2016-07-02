from __future__ import division
strings={}
count=0
line=[]
lettercount=0
with open("rosalind_gc.txt") as f:
  for line in f:
    
    
    if line[0]=='>':
       if(count!=0):
           strings[name]=(cgcount+0.0)/(cgcount+0.0+lettercount)
       name=line[1:]
       #print name
       strings[name]=0
       #print strings
       cgcount=0
       lettercount=0
       count+=1
    else:
       for i in line:
           if i=='C' or i=='G':
               cgcount+=1
           if i=='A' or i=='T':
               lettercount+=1
             
strings[name]=(cgcount+0.0)/(cgcount+0.0+lettercount)
print max(strings,key=strings.get),
print max(strings.values())*100       

