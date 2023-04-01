def maxi(f1, f2):
    if f1==f2:
        return f1
    if (f1=='S' and f2=='P') or (f1=='P' and f2=='S'):
        return 'S'
    if (f1 == 'S' and f2 == 'R') or (f1 == 'R' and f2 == 'S'):
        return 'R'
    if (f1 == 'P' and f2 == 'R') or (f1 == 'R' and f2 == 'P'):
        return 'P'


def runda(f):
    l=[]
    for i in range(0,len(f),2):
        l.append(maxi(f[i],f[i+1]))
    return l

f_in = open("level2_1.in", "r")
f_out= open("level2_1.out", "w")

lines = f_in.readlines()
n, m=lines[0].split(' ')
n=int(n)
m=int(m)
for i in range(1, n+1):
    f=lines[i].strip()
    for i in range(2):
        f=runda(f)
    for i in range(len(f)):
        f_out.write(f[i])
    f_out.write('\n')
f_in.close()
f_out.close()
