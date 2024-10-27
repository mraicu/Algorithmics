fileName = "../level2_data/level2_2.in"
import numpy as np

fin = open(fileName, "r")
fout = open("level2_2.out", "w")
n = fin.readline()
n = int(n)
for i in range(n):
    line = fin.readline().split()
    x = int(line[1])  # randuri
    y = int(line[0])  # cols
    nr_t = int(line[2])

    k = 1
    mat = [[0 for _ in range(y)] for _ in range(x)]

    for i in range(x):
        for j in range(y):
            mat[i][j] = k
            if (j + 1) % 3 == 0:
                k += 1

    matrix = np.array(mat)

    for i in range(x):
        for j in range(y):
            fout.write(str(mat[i][j])+ " " )

        fout.write("\n")

    # Save to a file
    with open('level2_1.out', 'w') as f:
        for row in matrix:
            f.write(' '.join(map(str, row)) + '\n')