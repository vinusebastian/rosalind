import sys
line=[]

d={}
with open('mass_table.txt') as fp:
   for line in fp:
        

     s=line.split()
     #print s
     d[s[0]]=s[1]
#print d
a=[]
b=[]
with open('spec_in.txt') as fp:
   for line in fp:
       b=line.split()
       #print b
       if len(b)==1:
          a.append(float(b[0]))
        
#print d
#print a

for i in range(1,len(a)):
      mass=a[i]-a[i-1]
      
      for x in d:
          if round(mass,4)==round(float(d[x]),4):
               sys.stdout.write(x)
               break
                   
print

