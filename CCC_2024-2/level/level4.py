fileName = "../level4_data/level4_1.in"
import numpy as np

fin = open(fileName, "r")
fout = open("level4_1.out", "w")

def write_f(mat, x, y, ):
    for i in range(x):
        for j in range(y):
            fout.write(str(mat[i][j]) + " ")
        fout.write("\n")


def inserare_linii(start, x, y, mat, k, n, m):

    for i in range(start, x, 2):
        j = 0
        while j < m:
            if j + 3 >= m :
                break
            mat[i][j] = 'x'
            if (j+1) % 4 == 0:
                mat[i][j] = '.'
            j += 1


    return mat


def inserare_col(start, x, y, mat, k, n, m):

    for j in range(start, y, 2):
        i = 0
        while i < n:
            if i + 3 > n :
                break
            mat[i][j] = 'x'
            if (i+1) % 4 == 0:
                mat[i][j] = '.'
            i += 1

    return mat


n = fin.readline()
n = int(n)

for i in range(n):
    line = fin.readline().split()
    x = int(line[1])  # randuri
    y = int(line[0])  # coloane
    nr_t = int(line[2])

    mat = [['.' for _ in range(y)] for _ in range(x)]

    # if (y % 3 == 0):
    #     inserare_linii(0, x, y, mat,1)
    # elif (x % 3 == 0):
    #     inserare_col(0, x, y, mat, 1)
    # else:
    if (y % 3 >= x % 3):
        # inserare linii
        mat = inserare_linii(0, x, y - y % 3, mat, 1, x, y)
        mat = inserare_col(y - y % 3 +1, x - x % 3, y, mat, x*(y//3)+1, x, y)
    else:
        # inserare cols
        mat = inserare_col(0, x - x % 3, y, mat, 1, x, y)
        mat = inserare_linii(x - x % 3 +1 , x, y - y % 3, mat, y*(x//3)+1, x, y)
    write_f(mat,x,y)