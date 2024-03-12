import numpy as np

fileName = "../level1_data/lvl1-2.inp"

fin = open(fileName, "r")
fout = open("leve1_2.out", "w")

data = fin.readlines()

lines = [line.strip() for line in data]
print(lines)

start, end, img_count = lines[0].split(" ")

start = int(start)
end = int(end)
img_count = int(img_count)

st = 2
for i in range(img_count):
    timestamp, rowc, colc = lines[i * (7 + 1) + 1].split(" ")
    timestamp = int(timestamp)
    rowc = int(rowc)
    colc = int(colc)
    mat = []
    for j in range(st, st + rowc):
        mat.append([int(j) for j in lines[j].split(" ")])
    st += rowc + 1

    if sum(row.count(0) for row in mat) != colc * rowc:
        fout.write(str(timestamp)+'\n')


