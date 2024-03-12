fileName = "../level3_data/level3-02.in"

fin = open(fileName, "r")
# fout = open("leve3_1.out", "w")

lines = []
data = fin.readline()

line = data.split(" ")

rows = int(line[0])
cols = int(line[1])
nboard = int(line[2]) * 2
npath = int(line[nboard + 3])

color = int(line[nboard + 3 + 1])
start = int(line[nboard + 3 + 2])
length = int(line[nboard + 3 + 3])

path = [i.strip() for i in line[nboard + 3 + 4:]]

data = {}
for i in range(3, nboard + 2, 2):
    key = int(line[i + 1])
    value = int(line[i])

    if key in data:
        data[key].append(value)
    else:
        data[key] = [value]


def valToPoz(val):
    r = (val - 1) // cols + 1
    c = val % cols if val % cols != 0 else cols
    return r, c


def valid(r, c, data, st):
    '''
    Touches point of a different color.
    '''
    for k in data.keys():
        crt_r, crt_c = valToPoz(data[k][0])
        if (crt_c == c and crt_r == r and k != color):
            return False
        crt_r, crt_c = valToPoz(data[k][1])
        if (crt_c == c and crt_r == r and k != color):
            return False
        if (r, c) in st:
            return False

    return True


def findpath(path):
    r_start, col_start = valToPoz(start)
    r_end, col_end = valToPoz(data[color][1])  ##?? 0 sau 1 depinde de nr
    i = 0
    steps = [(r_start, col_start)]
    for i, p in enumerate(path):
        if p == 'N':
            if r_start - 1 > 0:
                r_start -= 1
                if not valid(r_start, col_start, data, steps):
                    return (-1, i)
        if p == 'E':
            if col_start + 1 <= cols:
                col_start += 1
                if not valid(r_start, col_start, data, steps):
                    return (-1, i)
        if p == 'S':
            if r_start + 1 <= rows:
                r_start += 1
                if not valid(r_start, col_start, data, steps):
                    return (-1, i)
        if p == 'W':
            if col_start - 1 > 0:
                col_start -= 1
                if not valid(r_start, col_start, data, steps):
                    return (-1, i)
        steps.append((r_start, col_start))
    return (1, i + 1) if (r_start == r_end and col_start == col_end) else (-1, i + 1)


print(findpath(path))
