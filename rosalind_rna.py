import sys
string=raw_input()
for i in string:
   if i=='T':
     sys.stdout.write('U')
   else:
     sys.stdout.write(i)
print
