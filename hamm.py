string1=raw_input()
string2=raw_input()
count=0
hamm=0
for i in string1:
      if i!=string2[count]:
           hamm+=1
      count+=1
print hamm
