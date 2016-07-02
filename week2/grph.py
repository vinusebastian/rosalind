def read_fasta(fp):
    name, seq = None, []
    for line in fp:
        line = line.rstrip()
        if line.startswith(">"):
            if name: yield (name, ''.join(seq))
            name, seq = line[1:], []
        else:
            seq.append(line)
    if name: yield (name, ''.join(seq))
a={}
with open("rosalind_grph.txt") as f:
           for name, seq in read_fasta(f):
               a[name]=[]               
               a[name].append(seq[0:3])
               a[name].append(seq[-3:])
               

for p in a:
    for q in a:
        if p!=q:
             if(a[p][1]==a[q][0]):
                print p,q
           
   
