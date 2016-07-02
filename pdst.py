f=open('pdst_in.txt','r')
a=f.read().split('>')
lis=a[1:]
strings=[]
def dist(x,y):
    count=0
    for i in range(len(x)):
        if x[i]!=y[i]:
           count+=1
    #print count
    #print len(x)
    return ((0.0+count)/len(x)) 
      
for el in lis:
  strings.append(el.replace('\n','')[13:])

for i in strings:
      for j in strings:
             print dist(i,j),
      print
    
