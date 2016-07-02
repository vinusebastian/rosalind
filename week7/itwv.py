strings=[]
def interwoven(dna1, dna2, superstr):
    #print dna1,dna2,superstr
   
    if len(superstr) == 0:
        return True
    elif dna1[0] == dna2[0] == superstr[0]:
        return interwoven(dna1[1:], dna2, superstr[1:]) or interwoven(dna1, dna2[1:], superstr[1:])
    elif dna1[0] == superstr[0]:
        return interwoven(dna1[1:], dna2, superstr[1:])
    elif dna2[0] == superstr[0]:
        return interwoven(dna1, dna2[1:], superstr[1:])
    else:
        return False
with open('itwv_in.txt') as fp:
     strings=fp.readlines()
s=[]
s=strings[0]

for i in range(1,len(strings)):
      for j in range(1,len(strings)):
         p=len(strings[i])+len(strings[j])
         
         check=0 
         for k in range(len(s)-p+2):
           #print k,p
           #print strings[i],strings[j],s[k:k+p-2]
           if interwoven(strings[i]+'$',strings[j]+'$',s[k:k+p-2])==True:
                 print 1,
                 check=1
                 break
         if check==0:
            print 0,                     
           
      print

#print interwoven('GT'+'$','GT'+'$','GGTT')
