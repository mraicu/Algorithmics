#Să se determine cuvintele unui text care apar exact o singură dată în acel text.
# De ex. cuvintele care apar o singură dată în ”ana are ana are mere rosii ana" sunt: 'mere' și 'rosii'.

def oneApperance(lst):
    splitLst=lst.split(" ")
    rez=[]
    for el in splitLst:
        if splitLst.count(el)==1:
            rez.append(el)
    return rez

def test():
    assert(oneApperance("ana are ana are mere rosii ana")==["mere","rosii"])

test()