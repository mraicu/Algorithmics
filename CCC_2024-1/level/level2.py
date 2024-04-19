from math import inf

fileName = "../level2_data/ex.in"

fin = open(fileName, "r")
fout = open("leve2_10.out", "w")
i = fin.readline()
i = int(i)
for i in range(i):
    line = fin.readline()
    countH = 0
    countL = 0
    maxH = 0
    maxL = 0
    minH = 0
    minL = 0
    for i in range(len(line)):
        if (line[i] == 'W'):
            countH += 1
            if countH > maxH:
                maxH = countH
            if countH < minH:
                minH = countH
        if (line[i] == 'S'):
            countH -= 1
            if countH > maxH:
                maxH = countH
            if countH < minH:
                minH = countH
        if (line[i] == 'D'):
            countL += 1
            if countL > maxL:
                maxL = countL
            if countL < minL:
                minL = countL
        if (line[i] == 'A'):
            countL -= 1
            if countL > maxL:
                maxL = countL
            if countL < minL:
                minL = countL

    fout.write(str(maxL - minL + 1) + " " + str(maxH - minH + 1) + "\n")
    fout.write(str(maxH) + " " + str(maxL) + " " + str(minH) +" "+ str(minL) + "\n")
