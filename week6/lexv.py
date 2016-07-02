import itertools
string=raw_input()
j=raw_input()
j=int(j)
#print string
stringp=[]
stringp=string.split()
a=''

for i in stringp:
     a+=i
#print a
#print stringp
def user_sorter(x):
    sum=0
    for i in xrange(len(x)-1,-1,-1):
       sum+=pow(10,i)*stringp.index(x[len(x)-1-i])
    return sum
def user(x,y):
   sum1=0
   sum2=0
   if len(x)<len(y):
      y=y[0:len(x)]
      t=-1
   elif len(y)<len(x):
      x=x[0:len(y)]
      t=1
   #print x,y
   if len(x)==len(y):
      #print x,y,stringp
      j=0 
      for i in reversed(x):
       sum1+=pow(10,j)*(stringp.index(i)+1)
       #print "here1"
       j=j+1 
      #print sum1
      j=0
      for i in reversed(y):
       sum2+=pow(10,j)*(stringp.index(i)+1)
       j=j+1 
       #print "here2"  
      #print sum2
      if(sum1-sum2==0):
       return t
      else:
       return sum1-sum2  

y=[]
l=[]
for i in range(1,j+1):
 z=itertools.product(a,repeat=i)
 y.extend(z)
for i in y:
    p=''
    for j in i:
        p+=j
    l.append(p)
#print l
l=sorted(l,cmp=user)
for i in l:
   print i

#print user("DDD","N")
#print user("DAD","NDD")

