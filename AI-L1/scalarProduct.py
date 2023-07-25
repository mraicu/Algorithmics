#Să se determine produsul scalar a doi vectori rari care conțin numere reale.
# Un vector este rar atunci când conține multe elemente nule. Vectorii pot avea oricâte dimensiuni.
# De ex. produsul scalar a 2 vectori unisimensionali [1,0,2,0,3] și [1,2,0,3,1] este 4.
def scalarProd(v1,v2):
    s=0
    for i in range(len(v1)):
       s=s+v1[i]*v2[i]
    return s


def test():

    assert(scalarProd([1,0,2,0,3], [1,2,0,3,1])==4)

test()