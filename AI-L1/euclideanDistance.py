#Să se determine distanța Euclideană între două locații identificate prin perechi de numere.
#De ex. distanța între (1,5) și (4,1) este 5.0
from math import sqrt


def euclidean(p, q):
    """
    p,q - pairs
    """
    return sqrt((p[1]-p[0])**2+(q[1]-q[0])**2)

def test():

    assert(euclidean((1,5), (4,1))==5.0)

test()