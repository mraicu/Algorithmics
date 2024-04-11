def CommonElementsEasy(strArr):
    input = [s.lower() for s in strArr]
    str1 = ''
    str2 = ''
    ok = 0
    for s in input:
        if s != 'sep' and ok == 0:
            str1 += s
        elif s == 'sep':
            ok = 1
        else:
            str2 += s
    rez = []
    str1 = set(str1)
    for e in str1:
        if e in str2:
            rez.append(e)

    rez = sorted(rez)
    return rez


print(CommonElementsEasy( ["apple", "cherry", "SEP", "banana", "plum"]))
