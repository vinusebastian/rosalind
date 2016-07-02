def complementary(x):
    if x=='A':
        return 'U'
    if x=='U':
        return 'A'
    if x=='C':
        return 'G'
    if x=='G':
        return 'C'
   
def func(seq):
        count=0
	if len(seq)<=2:
             return 1
	else:             
             if seq not in table:
                    	intervals = []
			for i in range(1,len(seq),2):
				if check(seq[1:i])==True and seq[0] == complementary(seq[i]):
					intervals.append([seq[1:i],seq[i+1:]])
                        if intervals == []:
				table[seq] = 0
                        else: 
                         count=0
                         for subint in intervals:
                                count+=((func(subint[0])*func(subint[1]))%1000000)%1000000
                         table[seq]=count  
	     return table[seq]
             
def check(subint):
        a=c=u=g=0
        for i in subint:
              if i =='A':a+=1
              if i =='C':c+=1
              if i =='U':u+=1
              if i =='G':g+=1
              
        if a == u and c == g:
		return True
	return False

f=open('rosalind_cat.txt','r')
a=f.read().split('>')
table = {}
lis=a[1:]
count=0
rnaa=lis[0].replace('\n','')[13:] 
print (func(rnaa)%1000000)
