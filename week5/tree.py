count=0
edge=0
with open('tree_in.txt') as fp:
    for line in fp:
        if count==0:
           n=int(line)
        count+=1
    print (n-count)
