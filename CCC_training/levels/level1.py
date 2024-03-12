fileName = "../level1_data/level1-2.in"

fin = open(fileName, "r")
fout = open("leve1_2.out", "w")

lines = []
data = fin.readline()

line = data.split(" ")

rows = int(line[0])
cols = int(line[1])
n = int(line[2])
target = [int(i) for i in line[3:]]  # 1 11 24 -> 1 1 3 3 6 4

for val in target:
    r = (val - 1) // cols + 1
    c = val % cols if val % cols != 0 else cols
    fout.write(" "+str(r)+ " "+str(c))
