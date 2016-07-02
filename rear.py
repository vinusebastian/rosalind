f=open('rear_in.txt','r')
line=0
def reva(x,y):
         
         if len(x)==1:
           return 0
  
         if x[0]==y[0]:
            #print "yes",x,y
            return(0+reva(x[1:],y[1:]))
         else:
            #print "no",x,y
            ind=y.index(x[0])
            string=y[0:ind+1]
            #print x,y 
            #print ind
            #print string
            #y.replace(string,string[::-1])
            for i in range(len(string)):
                 y[i]=string[::-1][i] 
            #print y 
            return(1+reva(x[1:],y[1:]))
  
line1=[]
list1=[]
line2=[]
list2=[]          
for i in f:
      if line%3==0:
         line1.append(i)
      elif (line-1)%3==0:
         line2.append(i)
      line+=1
#print line1
#print line2

for i in range(len(line1)):
       numbers=line1[i].strip().split()
       #print numbers
       list1=[]
       list2=[]
       for j in numbers:
            list1.append(int(j))
       numbers=line2[i].strip().split()
       for j in numbers:
            list2.append(int(j))
        
       print reva(list1,list2)
       
         
