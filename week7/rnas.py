


def func(string):
	if len(string) <= 3:
	    return 1
	else:
	    if string in donedict:
		return donedict[string]
	    else:
		intervals = []
		for i in xrange(4, len(string)):
		 if string[0] in d[string[i]]:
		      intervals.append([string[1:i],string[i+1:]])
                count=0
                for subint in intervals:
                                count+=((func(subint[0])*func(subint[1])))
                count+=func(string[1:])   
		
                donedict[string]=count 
	return donedict[string]

f1=open('rnas_in.txt','r')
d={}
string=f1.readlines()
x=string[0].rstrip()
d['A']='U'
d['U']='AG'
d['C']='G'
d['G']='CU'
done_dict = {}


donedict = {}
#print x
noncross = func(x)

print noncross

