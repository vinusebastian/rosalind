f=open('edit_in.txt','r')
a=f.read().split('>')
lis=a[1:]
strings=[]
for el in lis:
  strings.append(el.replace('\n','')[13:])
def edit(x,y):
   m=len(x)
   n=len(y)
   A = [[0 for i in range(n+1)] for j in range(m+1)]
   #print A
   for i in range(m+1):
       #print A[i][0],i
       A[i][0]=i
   for j in range(n+1):
       A[0][j]=j
   A[0][0]=0
   for j in range(1,n+1):
       for i in range(1,m+1):
            c=1
            if x[i-1]==y[j-1]:
               c=0
                     
            A[i][j]=min(c+A[i-1][j-1],1+A[i-1][j],1+A[i][j-1])
   #print A
   print A[m][n]
#print strings[0],strings[1]

#print len(strings[0])
#print len(strings[1])
edit(strings[0],strings[1]) 
