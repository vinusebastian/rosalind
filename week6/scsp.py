def lcs(a, b):
    lengths = [[0 for j in range(len(b)+1)] for i in range(len(a)+1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if x == y:
                lengths[i+1][j+1] = lengths[i][j] + 1
            else:
                lengths[i+1][j+1] =max(lengths[i+1][j], lengths[i][j+1])
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
def problem(s, t):
    z = lcs(s, t)
    u = ""
    i = 0
    j = 0
    for c in z:
        if i < len(s):
            while s[i] != c:
                u += s[i]
                i += 1
            i += 1
        if j < len(t):
            while t[j] != c:
                u += t[j]
                j += 1
            j += 1
        u += c
    if i < len(s):
        u += s[i:]
    if j < len(t):
        u += t[j:]
    return u
string1=raw_input()
string2=raw_input()
print problem(string1,string2)

