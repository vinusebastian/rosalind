import itertools
l=raw_input()
l=int(l)
a=[]
print len(list(itertools.permutations(range(l))))
a=list(itertools.permutations(range(l)))
for i in a:
   for j in i:
      print j+1,
   print
