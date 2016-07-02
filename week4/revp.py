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
with open("rosalind_revp.txt") as f:
           for name, seq in read_fasta(f):
             #print seq
             for stringsize in xrange(4,13,2):
               #print "Stringsize" ,stringsize      
               for i in range(len(seq)-stringsize+1):
                   #print i
                   word=seq[i:i+stringsize]
                   #print word
                   a=""
                   for j in word:
                       if j=="A":
                           a+="T"
                       elif j=="T":
                           a+="A"
                       elif j=="C":
                           a+="G"
                       elif j=="G":
                           a+="C"
                   if a==word[::-1]:
                        print i+1,stringsize
