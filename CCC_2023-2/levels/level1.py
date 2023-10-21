fileName= "../level1_data/level1_1.in"

f = open(fileName, "r")
fout = open("leve1_1.out", "w")

n = int(f.readline())
line=[]

for i in range(n) :
    line.append(f.readline())

m = int(f.readline())

for i in range(m):
    a, b = f.readline().split(',')
    a = int(a)
    b = int(b)
    fout.write(line[b][a]+"\n")