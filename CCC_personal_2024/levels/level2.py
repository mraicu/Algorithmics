import numpy as np

fileName = "../level2_data/lvl2-4.inp"
fout = open("leve2_4.out", "w")
matrices = []
with open(fileName, 'r') as file:
    start, end, num_matrix = file.readline().strip().split(' ')
    start = int(start)
    end = int(end)
    num_matrix = int(num_matrix)

    for _ in range(num_matrix):
        matrix_info = list(map(int, file.readline().split()))
        timestamp, rows, cols = matrix_info
        matrix = []

        for _ in range(rows):
            row = list(map(int, file.readline().split()))
            matrix.append(row)

        cpy_mat = []
        for r in matrix:
            if r.count(0) != len(r):
                cpy_mat.append(r)

        if (cpy_mat != []):
            num_columns = len(cpy_mat[0])
            columns_to_remove = [i for i in range(num_columns) if all(row[i] == 0 for row in cpy_mat)]

            if columns_to_remove:
                cpy_mat = [[element for j, element in enumerate(row) if j not in columns_to_remove] for row in cpy_mat]

            matrices.append([cpy_mat, timestamp, 0])
    # print(matrices)


def are_matrices_equal(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        return False  # Matrices have different dimensions

    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            if matrix1[i][j] == 0 and matrix2[i][j] != 0 or matrix1[i][j] != 0 and matrix2[i][j] == 0:
                return False

    return True


def isIn(elem, matrix):
    flat_matrix = [item for sublist in matrix for item in sublist]
    return elem in flat_matrix


result = []

for i in range(len(matrices)):
    line = []
    if matrices[i][2] == 0:
        line.append(matrices[i][1])
        for j in range(i + 1, len(matrices)):
            if matrices[j][2] == 0:
                if are_matrices_equal(matrices[i][0], matrices[j][0]):
                    matrices[j][2] = 1
                    line.append(matrices[j][1])
                # elif not isIn(matrices[i][1], result):
                #     result.append([matrices[i][1]])
        result.append(line)

print(result)

for i in range(len(result)):
    fout.write(str(result[i][0])+ ' '+str(result[i][-1])+ ' ')
    fout.write(str(len(result[i])) + ' ')
    fout.write('\n')

# 2451 6550 4
# 2461 9623 6
# 3718 5975 2
# 4205 9504 5
# 6648 9990 3