import re
string=raw_input()
substring=raw_input()
for n in xrange(len(string)): 
      if string.find(substring, n) == n:
          print n+1,
 
