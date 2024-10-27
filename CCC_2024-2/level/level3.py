fileName = "../level3_data/level3_5.in"
import numpy as np

fin = open(fileName, "r")
fout = open("level3_5.out", "w")


def write_f(mat, x, y, ):
    for i in range(x):
        for j in range(y):
            fout.write(str(mat[i][j]) + " ")
        fout.write("\n")


def inserare_linii(start, x, y, mat, k):

    for i in range(start, x):
        for j in range(y):
            mat[i][j] = k
            if (j + 1) % 3 == 0:
                k += 1
    return mat


def inserare_col(start, x, y, mat, k):

    for j in range(start, y):
        for i in range(x):
            mat[i][j] = k
            if (i + 1) % 3 == 0:
                k += 1
    return mat


n = fin.readline()
n = int(n)

for i in range(n):
    line = fin.readline().split()
    x = int(line[1])  # randuri
    y = int(line[0])  # coloane
    nr_t = int(line[2])

    mat = [[0 for _ in range(y)] for _ in range(x)]

    if (y % 3 == 0):
        inserare_linii(0, x, y, mat,1)
    elif (x % 3 == 0):
        inserare_col(0, x, y, mat, 1)
    else:
        if (y % 3 >= x % 3):
            # inserare linii
            mat = inserare_linii(0, x, y - y % 3, mat, 1)
            mat = inserare_col(y - y % 3, x - x % 3, y, mat, x*(y//3)+1)
        else:
            # inserare cols
            mat = inserare_col(0, x - x % 3, y, mat, 1)
            mat = inserare_linii(x - x % 3, x, y - y % 3, mat, y*(x//3)+1)
    write_f(mat, x, y)
