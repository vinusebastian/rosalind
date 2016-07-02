f=open("rosalind_ini5.txt","r")
i=1
for line in f:
   if i%2==0:
    print line,
   i=i+1
