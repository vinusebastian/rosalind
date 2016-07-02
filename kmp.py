def kmpfunc(s):
    j = -1
    b = [j]
    
    for c in s:
        while j >= 0 and s[j] != c:
            j = b[j]
        j += 1
        b.append(j)

    return b[1:]
f1=open('kmp_in.txt','r')
a=f1.read().split('>')
lis=a[1:]
string=lis[0].replace('\n','')[13:]
results = kmpfunc(string)
for i in results:
    print i,

