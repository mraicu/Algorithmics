import numpy as np

fileName = "../level3_data/lvl3-1.inp"
fout = open("leve3_1.out", "w")
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

for line in result:
    if len(line) >= 4:
        pass


# def validSubset(data):
#     result_lines = []
#     for i in range(len(data)):
#         current_subset = [data[i]]
#
#         for j in range(i , len(data)-3):
#             if data[i] + data[j] in data:
#                 d = abs(data[i] - data[j])
#                 if (max(data[i], data[j]) + 2 * d) in data:
#                     current_subset.append(data[j])
#                     current_subset.append(max(data[i], data[j]) + 2 * d)
#         # Check if the current subset is valid
#         if len(current_subset) >= 3:
#             print(current_subset)
#             result_lines.append((current_subset[0], current_subset[-1], len(current_subset) + 1))
#
#     return result_lines
def validSubset(data):
    result_lines = []
    n = len(data)

    for i in range(n):
        current_subset = [data[i]]

        for j in range(i + 1, n):
            d = abs(data[i] - data[j])

            if (data[i] - d) in data and data[i] + data[j] in data and (data[i] + 2 * d) in data:
                current_subset.extend([data[i] - d, data[i] + d, data[i] + 2 * d])

        if len(current_subset) >= 4:
            result_lines.append((min(current_subset), max(current_subset), len(current_subset) ))
    result_lines.sort(key=lambda x: x[0])

    return result_lines

print(validSubset(result[0]))

for s in validSubset(result[0]):
    fout.write(str(s[0]) + ' ' + str(s[1]) + ' ' + str(s[2]))
    fout.write('\n')
