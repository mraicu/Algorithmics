def readMat():
    n, m = fin.readline().split(" ")
    m = int(m)
    n = int(n)
    mat = []
    for i in range(m):
        line = list(fin.readline().strip())
        mat.append(line)
    return mat, m, n


fileName = "../level3_data/level3_5.in"

fin = open(fileName, "r")
fout = open("leve3_5.out", "w")
g = fin.readline()
g = int(g)
for _ in range(g):
    mat, m, n = readMat()
    path = fin.readline()
    countH = 0
    countL = 0
    maxH = 0
    maxL = 0
    minH = 0
    minL = 0
    for i in range(len(path)):
        if (path[i] == 'W'):
            countH += 1
            if countH > maxH:
                maxH = countH
            if countH < minH:
                minH = countH
        if (path[i] == 'S'):
            countH -= 1
            if countH > maxH:
                maxH = countH
            if countH < minH:
                minH = countH
        if (path[i] == 'D'):
            countL += 1
            if countL > maxL:
                maxL = countL
            if countL < minL:
                minL = countL
        if (path[i] == 'A'):
            countL -= 1
            if countL > maxL:
                maxL = countL
            if countL < minL:
                minL = countL
    maxH = abs(maxH)
    maxL = abs(minL)
    ok = True
    if maxH >= m or maxL >= n:
        fout.write('INVALID\n')
        continue
    if mat[maxH][maxL] == 'X':
        fout.write('INVALID\n')
        continue
    else:
        mat[maxH][maxL] = '*'
    for p in path:
        if (p == 'W'):
            maxH -= 1
            if maxH < m and maxL < n and maxL >= 0 and maxH >= 0:
                if mat[maxH][maxL] == 'X' or mat[maxH][maxL] == '*':
                    fout.write('INVALID\n')
                    ok = False
                    break
                else:
                    mat[maxH][maxL] = '*'
            else:
                fout.write('INVALID\n')
                ok = False
                break
        if (p == 'S'):
            maxH += 1
            if maxH < m and maxL < n and maxL >= 0 and maxH >= 0:
                if mat[maxH][maxL] == 'X' or mat[maxH][maxL] == '*':
                    fout.write('INVALID\n')
                    ok = False
                    break
                else:
                    mat[maxH][maxL] = '*'
            else:
                fout.write('INVALID\n')
                ok = False
                break
        if (p == 'D'):
            maxL += 1
            if maxH < m and maxL < n and maxL >= 0 and maxH >= 0:
                if mat[maxH][maxL] == 'X' or mat[maxH][maxL] == '*':
                    fout.write('INVALID\n')
                    ok = False
                    break
                else:
                    mat[maxH][maxL] = '*'
            else:
                fout.write('INVALID\n')
                ok = False
                break
        if (p == 'A'):
            maxL -= 1
            if maxH < m and maxL < n and maxL >= 0 and maxH >= 0:
                if mat[maxH][maxL] == 'X' or mat[maxH][maxL] == '*':
                    fout.write('INVALID\n')
                    ok = False
                    break
                else:
                    mat[maxH][maxL] = '*'
            else:
                fout.write('INVALID\n')
                ok = False
                break
    if ok == True:
        for row in mat:
            if row.count('.') > 0:
                fout.write('INVALID\n')
                ok = False
                break
    if ok == True:
        fout.write('VALID\n')
