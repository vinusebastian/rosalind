import sys
f=open("codontable.txt","r")
table={}
line=[]
with open("codontable.txt") as f:
  for line in f:

      a,b=line.split()
      if(b in table):
        table[b]+=1
      else:
        table[b]=1
string=raw_input()
number=1
for i in string:
    
    number=(number*table[i])%1000000
number=(number*table["Stop"])%1000000
print number
