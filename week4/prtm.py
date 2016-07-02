table={}
line=[]
with open("masstable.txt") as f:
  for line in f:

      x=line.split()
      table[x[0]]=x[1]
string=raw_input()
summ=0.0
for i in string:
    summ+=0.0+float(table[i])
print summ  
