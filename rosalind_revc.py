import sys
string=raw_input()
for i in reversed(string):
  if i=='A':
    sys.stdout.write('T')
  elif i=='T':
    sys.stdout.write('A')
  elif i=='C':
    sys.stdout.write('G')
  elif i=='G':
    sys.stdout.write('C')
print


