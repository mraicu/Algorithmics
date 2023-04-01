def maxi(f1, f2):
    if f1==f2:
        return f1
    if (f1=='S' and f2=='P') or (f1=='P' and f2=='S'):
        return 'S'
    if (f1 == 'S' and f2 == 'R') or (f1 == 'R' and f2 == 'S'):
        return 'R'
    if (f1 == 'P' and f2 == 'R') or (f1 == 'R' and f2 == 'P'):
        return 'P'

f_in = open("level1_data/level1_1.in", "r")
f_out= open("level1_data/level1_1.out", "w")

lines = f_in.readlines()
nr=int(lines[0])
for i in range(1, nr+1):
    f1=lines[i][0]
    f2=lines[i][1]
    f_out.write(maxi(f1,f2)+"\n")
f_in.close()
f_out.close()
