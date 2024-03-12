fileName = "../level2_data/level2-3.in"

fin = open(fileName, "r")
fout = open("leve2_3.out", "w")

lines = []
data = fin.readline()

line = data.split(" ")

rows = int(line[0])
cols = int(line[1])
n = int(line[2]) + 1

data = {}

for i in range(3, n * 2, 2):
    key = int(line[i + 1])
    value = int(line[i])

    if key in data:
        data[key].append(value)
    else:
        data[key] = [value]

sorted_dict = dict(sorted(data.items()))
print(sorted_dict)

def manhattan(data: dict):
    for k in data.keys():
        r1 = (data[k][0] - 1) // cols + 1
        c1 = data[k][0] % cols if data[k][0] % cols != 0 else cols
        r2 = (data[k][1] - 1) // cols + 1
        c2 = data[k][1] % cols if data[k][1] % cols != 0 else cols
        m = abs(r1 - r2) + abs(c1 - c2)
        fout.write(" " + str(m))


manhattan(sorted_dict)
