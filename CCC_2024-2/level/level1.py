fileName = "../level1_data/level1_5.in"

fin = open(fileName, "r")
fout = open("leve1_5.out", "w")
n = fin.readline()
n = int(n)
for i in range(n):
    line = fin.readline().split()
    x = int(line[0])
    y = int(line[1])
    nr_t = x // 3 * y
    fout.write(str(nr_t) + "\n")
