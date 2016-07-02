w=raw_input()
string=''
while 1:
 s=raw_input()
 if(s[0]!='>'):
    string=string+s 
 else:
    break 

t=raw_input()
i=0
l=-1
x=l
count=0
s=string
while 1:
   r=s[l+1:].index(t[i])
   l=r
   if l<len(s) and l>-1:
    count+=(l+1)
    l=count-1
    print count,
   else:
    break
   i=i+1
   if i==len(t):
     break
  
