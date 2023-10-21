def listToAdj(lst, n):
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            matrix[i][j] = 1 if lst[i][j] == "L" else 0

    return matrix

def are_nodes_in_same_component(matrix, node1, node2):
    def dfs(node, visited):
        row, col = node
        visited[row][col] = True

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < len(matrix) and 0 <= new_col < len(matrix[0]) and matrix[new_row][new_col] == 1 and not visited[new_row][new_col]:
                dfs((new_row, new_col), visited)

    if matrix[node1[0]][node1[1]] == 1 and matrix[node2[0]][node2[1]] == 1:
        visited = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        dfs(node1, visited)
        return visited[node2[0]][node2[1]]
    else:
        return False


fileName = "../level2_data/level2_5.in"

f = open(fileName, "r")
fout = open("level2_5.out", "w")

n = int(f.readline())
line = []

for i in range(n):
    line.append(f.readline())

m = int(f.readline())

for i in range(m):
    #
    data1, data2 = f.readline().split(' ')
    a, b = data1.split(',')
    c, d = data2.split(',')
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    matrix = listToAdj(line, n)
    u1 = 1 if line[b][a] == "L" else 0
    u2 = 1 if line[d][c] == "L" else 0

    if are_nodes_in_same_component(matrix, (b,a), (d,c) ):
        fout.write('SAME\n')
    else:
        fout.write('DIFFERENT\n')


