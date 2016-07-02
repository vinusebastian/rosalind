import re
l=[]
def func(string):
 #print string
 #print string[61]
 x=[m.start() for m in re.finditer('ATG', string)]  
 for i in x:
      #print i
      orf=''
      
      for start in xrange(i,len(string),3):
      
       word=string[start:start+3]
       #print word,
       if word != 'TAA' and word!= 'TGA' and word!='TAG' and len(word)==3:
        orf+=table[word]
       else:
        if len(word)==3:
          if orf not in l:
            #print i
            print orf
            l.append(orf) 
          
          break
        
        
  
     
import sys
table={}
line=[]
with open("codontable2.txt") as f:
  for line in f:

     x=line.split()
     if len(x)>0:  
      table[x[0]]=x[1]
      table[x[2]]=x[3]
      table[x[4]]=x[5]
      table[x[6]]=x[7] 
with open("rosalind_orf.txt") as f:
  for line in f:
    
    
   if line.startswith(">"):
            name, seq = line[1:], []
   else:
            line=line.rstrip()
            seq.append(line)
   string=''.join(seq)
#print string

              
strin=""
  # print "new k=",k
func(string)
for i in range(len(string)):
    if string[i]=="A":
       strin+="T"
    elif string[i]=="T":
       strin+="A"
    elif string[i]=="C":
       strin+="G"
    elif string[i]=="G":
       strin+="C"  
#print strin
#print string
             
func(strin[::-1])
