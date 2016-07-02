string=raw_input()
a=0
c=0
g=0
t=0
for i in string:
   if i=='A':
      a=a+1
   elif i=='C':
      c=c+1
   elif i=='G':
      g=g+1
   elif i=='T':
      t=t+1
print a,c,g,t
     
