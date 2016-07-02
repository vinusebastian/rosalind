f=open('tran_in.txt','r')
a=f.read().split('>')
lis=a[1:]
strings=[]
for el in lis:
  strings.append(el.replace('\n','')[13:]) 
string1=strings[0]
string2=strings[1]  
transition=0
transversion=0
for i in range(len(string1)):
     if string1[i]!=string2[i]:
       if string1[i]=='A' and string2[i]=='G' or string1[i]=='G' and string2[i]=='A':
             transition+=1
       elif string1[i]=='C' and string2[i]=='T' or string1[i]=='T' and string2[i]=='C':
             transition+=1
       else: 
             transversion+=1 
                       
print float(transition*1.0/transversion)        
           
