import sys
profile={}
profile["A"]=[]
profile["C"]=[]
profile["G"]=[]
profile["T"]=[]
n=0
count=0
for i in range(1001):

 profile["A"].append(0)
 profile["C"].append(0)
 profile["G"].append(0)
 profile["T"].append(0)
with open("rosalind_cons.txt") as f:
  for line in f:
    if line[0]!='>':
      
      string=line[:]
      
      for i in string:
        if i!='\n': 
          profile[i][count]+=1
          count+=1
          n+=1
    else:
       
       n=0
       count=0         
for i in range(n):
      l=max(profile['A'][i],profile['C'][i],profile['G'][i],profile['T'][i])
      
      if l==profile['A'][i]:
           sys.stdout.write('A')
      elif l==profile['C'][i]:
           sys.stdout.write('C')
      elif l==profile['G'][i]:
           sys.stdout.write('G')
      elif l==profile['T'][i]:
           sys.stdout.write('T')
print
count=0
print "A:",
for i in profile['A']:
   if(count<n): 
    print i,
   count+=1
count=0
print
print "C:",
for i in profile['C']:
   if(count<n) :
    print i,
   count+=1
count=0
print
print "G:",
for i in profile['G']:
   if(count<n): 
    print i,
   count+=1
count=0
print 
print "T:",
for i in profile['T']:
   if(count<n) :
    print i,
   count+=1
