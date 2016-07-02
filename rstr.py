string=raw_input()
a,b=string.split()
a=int(a)
b=float(b)
string=raw_input()
gcc=0
atc=0
for x in string:
     if x=='G' or x=='C':
         gcc+=1
     else:
         atc+=1
gc=b/2
at=(1-b)/2
#print gc,gcc,at,atc
nots=1-1.0*(1.0*pow(gc,gcc)*1.0*pow(at,atc))
#print nots
atleastones=1-1.0*pow((nots),a)
print round(atleastones,3)
