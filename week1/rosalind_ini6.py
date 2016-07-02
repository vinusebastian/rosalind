from collections import defaultdict
string=raw_input()
d=defaultdict(int)
for word in string.split():
   d[word]+=1
for i in d:
  print i,d[i]
