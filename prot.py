import sys
f=open("codontable.txt","r")
table={}
line=[]
with open("codontable.txt") as f:
  for line in f:

      a,b=line.split()
      
      table[a]=b
#print table
count=0
x=[]
string=raw_input()
for i in string:
   
    x=string[count:count+3]
   
    if(table[x]=="Stop"):
         break
    else:
         sys.stdout.write(table[x])
    count+=3
print

