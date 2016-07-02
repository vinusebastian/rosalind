n=raw_input()
n=int(n)
string=raw_input()
gcc=0
atc=0
for x in string:
     if x=='G' or x=='C':
         gcc+=1
     else:
         atc+=1
percentages=raw_input()
pl=[]
pl=percentages.split()
#print pl
for j in pl:
      i=float(j)
      gc=i/2
      at=(1-i)/2
      s=len(string)
      print round(1.0*(n-s+1)*pow(gc,gcc)*pow(at,atc),3),
 
      
