
import urllib2
with open("rosalind_mprt.txt") as f:
  for line in f:
       x='http://www.uniprot.org/uniprot/'+line.rstrip()+'.fasta'
       downloaded_data  = urllib2.urlopen(x)
       string='' 
       name, seq = None, []
       for lines in downloaded_data.readlines():
          lines = lines.rstrip()
          if lines.startswith(">"):
            name, seq = lines[1:], []
          else:
            seq.append(lines)
          string=''.join(seq) 
       x=[]
       for i in range(len(string)-4) : 
               a=string[i:i+4]
               if(a[0]=='N' and a[1]!='P' and (a[2]=='S' or a[2]=='T') and a[3]!='P'):
                      x.append(i)
       if len(x)!=0:
          print line.rstrip()
          for i in x:
               print i+1,   
          print              
                      
                 
