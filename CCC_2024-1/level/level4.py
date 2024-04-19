# def readMat():
#     n, m = fin.readline().split(" ")
#     m = int(m)
#     n = int(n)
#     mat = []
#     for i in range(m):
#         line = list(fin.readline().strip())
#         mat.append(line)
#     return mat, m, n
#
#
# fileName = "../level3_data/level3_5.in"
#
# fin = open(fileName, "r")
# fout = open("leve3_5.out", "w")
# g = fin.readline()
# g = int(g)
# for _ in range(g):
#     mat, m, n = readMat()
#     path = fin.readline()
#     countH = 0
#     countL = 0
#     maxH = 0
#     maxL = 0
#     minH = 0
#     minL = 0
#
#
#
#
fout = open("leve4_1.out", "w")
def is_valid_move(matrix, x, y, visited):
    # Check if the move is within the bounds of the matrix and not visited
    return 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and matrix[x][y] == '.' and not visited[x][y]


def dfs(matrix, x, y, visited, path):
    # Mark current cell as visited
    visited[x][y] = True
    # Add current cell to the path
    path.append((x, y))

    # If the current cell is at the bottom right corner, return True (path found)
    if x == len(matrix) - 1 and y == len(matrix[0]) - 1:
        return True

    # Define possible moves (up, down, left, right)
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # Check each possible move
    for dx, dy in moves:
        new_x, new_y = x + dx, y + dy
        if is_valid_move(matrix, new_x, new_y, visited):
            # If the move is valid, recursively call DFS
            if dfs(matrix, new_x, new_y, visited, path):
                return True

    # If no valid moves found, backtrack
    path.pop()
    return False


def find_path(matrix):
    if not matrix or not matrix[0]:
        return None

    # Initialize visited matrix
    visited = [[False] * len(matrix[0]) for _ in range(len(matrix))]
    # Initialize path
    path = []

    # Start DFS from the top-left corner
    if dfs(matrix, 0, 0, visited, path):
        return path
    else:
        return None

matrix = [
    ".............",
    ".........X...",
    ".............",
    ".............",
    ".............",
    ".............",
    ".............",
    "............."
]


path = find_path(matrix)

list = []
res =''
if path:
    print("Path found:")
    prev_row, prev_col = path[0]
    for kk in range(1, len(path)-1):
        if path[kk][0] - prev_row == 1:
            list.append('D')
            res+='D'
        if path[kk][0] - prev_row == -1:
            list.append('A')
            res+='A'
        if path[kk][1] - prev_col == 1:
            list.append('S')
            res+='S'
        if path[kk][1] - prev_col == -1:
            list.append('W')
            res+='W'

        prev_row, prev_col = path[kk]
else:
    print("No path found.")

print(res)
