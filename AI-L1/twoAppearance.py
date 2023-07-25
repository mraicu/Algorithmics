# Pentru un șir cu n elemente care conține valori din mulțimea {1, 2, ..., n - 1}
# astfel încât o singură valoare se repetă de două ori, să se identifice acea valoare care se repetă.
# De ex. în șirul [1,2,3,4,2] valoarea 2 apare de două ori.

def twoAppearance(lst):
    for el in lst:
        if lst.count(el)==2:
            return el

def test():
    assert(twoAppearance([1,2,3,4,2])==2)

test()