
def func(string):
	if len(string) <= 1:
	    return 1
	else:
	    if string in donedict:
		return donedict[string]
	    else:
		intervals = []
		for i in xrange(1, len(string)):
		 if string[0] == d[string[i]]:
		      intervals.append([string[1:i],string[i+1:]])
                count=0
                for subint in intervals:
                                count+=((func(subint[0])*func(subint[1]))%1000000)
                count+=(func(string[1:])%1000000)%1000000  
		
                donedict[string]=count 
	return donedict[string]
f1=open('motz_in.txt','r')
a=f1.read().split('>')
lis=a[1:]
d={}
string=lis[0].replace('\n','')[13:]
d['A']='U'
d['U']='A'
d['C']='G'
d['G']='C'
donedict = {}
noncross = func(string)

print noncross%1000000

