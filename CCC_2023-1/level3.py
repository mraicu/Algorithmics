from itertools import permutations
def maxi(f1, f2):
    if f1==f2:
        return f1
    if (f1=='S' and f2=='P') or (f1=='P' and f2=='S'):
        return 'S'
    if (f1 == 'S' and f2 == 'R') or (f1 == 'R' and f2 == 'S'):
        return 'R'
    if (f1 == 'P' and f2 == 'R') or (f1 == 'R' and f2 == 'P'):
        return 'P'

def isSolution(lst):
    for i in range(2):
        lst=runda(lst)
    if 'R' in lst:
        return False
    if 'S' in lst:
        return True
    return False

def consistent(lst, n):
    if len(lst) == n:
        return True
    return False

def backtrackingRecursiv(x, lst):
    x.append('-')
    for i in lst:
        x[-1] = i
        if consistent(x, len(lst)):
            if isSolution(x):
                for i in range(len(x)):
                    f_out.write(x[i])
                return
            else:
                backtrackingRecursiv(x[:], lst)

def runda(f):
    l=[]
    for i in range(0,len(f),2):
        l.append(maxi(f[i],f[i+1]))
    return l

f_in = open("level3_1.in", "r")
f_out= open("level3_1.out", "w")

lines = f_in.readlines()
n, m=lines[0].split(' ')
n=int(n)
m=int(m)
for i in range(1, n+1):
    f=lines[i].strip()
    l=[]
    x=[]
    r,p,s=f.split(' ')
    r=r[:-1]
    r=int(r)
    p=p[:-1]
    p = int(p)
    s=s[:-1]
    s = int(s)
    for j in range(0,r):
        l.append('R')
    for j in range(0,p):
        l.append('P')
    for j in range(0,s):
        l.append('S')
    p=permutations(l, len(l))
    for el in p:
        if isSolution(el):
            for k in range(len(el)):
                f_out.write(el[k])
            f_out.write('\n')
            break
f_in.close()
f_out.close()
