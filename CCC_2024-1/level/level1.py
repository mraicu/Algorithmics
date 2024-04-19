fileName = "../level1_data/level1_5.in"

fin = open(fileName, "r")
fout = open("leve1_5.out", "w")
i = fin.readline()
i = int(i)
for i in range(i):
    line = fin.readline()
    w = line.count('W')
    d = line.count('D')
    s = line.count('S')
    a = line.count('A')
    fout.write(str(w) + " " + str(d) + " " + str(s) + " " + str(a) + "\n")
