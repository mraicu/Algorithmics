def func(lst):
    for i in range(0, len(lst) - 1):
        #         verificam daca are diagonala
        if abs(lst[i][0] - lst[i + 1][0]) == 1 and abs(lst[i][1] - lst[i + 1][1]) == 1:
            p1 = (lst[i][0], lst[i + 1][1])
            p2 = (lst[i + 1][0], lst[i][1])
            if p1 in lst and p2 in lst:
                index1 = lst.index(p1)
                index2 = lst.index(p2)
                if abs(index1 - index2) == 1:
                    return True
    return False



fileName = "../level3_data/level3_5.in"

f = open(fileName, "r")
fout = open("level3_3.out", "w")

n = int(f.readline())
line = []

for i in range(n):
    line.append(f.readline())

m = int(f.readline())

# transmis inverssss!!!!!!

a = ()
for i in range(m):
    p = []
    l = f.readline().split(' ')
    for i in range(len(l)):
        a, b = l[i].split(',')
        c=(int(b), int(a))
        p.append(c)

    amScris=False
    if func(p):
        fout.write("INVALID" + "\n")
        amScris=True
    else:
        for el in p:
            if p.count(el) > 1:
                fout.write("INVALID" + "\n")
                amScris = True
                break

    if amScris==False:
        fout.write("VALID" + "\n")