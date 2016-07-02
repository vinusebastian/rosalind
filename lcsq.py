def lcs(a, b):
    lengths = [[0 for j in range(len(b)+1)] for i in range(len(a)+1)]
    
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if x == y:
                lengths[i+1][j+1] = lengths[i][j] + 1
            else:
                lengths[i+1][j+1] = max(lengths[i+1][j], lengths[i][j+1])
    
    result = ""
    x, y = len(a), len(b)
    while x != 0 and y != 0:
        if lengths[x][y] == lengths[x-1][y]:
            x -= 1
        elif lengths[x][y] == lengths[x][y-1]:
            y -= 1
        else:
           if a[x-1] == b[y-1]:
            result = a[x-1] + result
            x -= 1
            y -= 1
    return result
f=open('lcsq_in.txt','r')
a=f.read().split('>')
lis=a[1:]
strings=[]
for el in lis:
  strings.append(el.replace('\n','')[13:])
print(lcs(strings[0],strings[1])) 
