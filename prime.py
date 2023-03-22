import time
"""
S este un sir de forma: 1223334444...x de x ori. 
Dandu-se N si apoi N numere, aflati pentru fiecare numar Ti cate numere prime se afla in sirul S.
Unde ti este limita sirului S.
 | INPUT | OUTPUT |
 ==================
 |  4    |    5   |  
 |  3    |    5   |  
 |  6    |    17  |    
 |  8    |    28  |   
 |  11   |        |
 ==================
Explicatie: N=4
            T=[3,6,8,11]
            pentru 3 -> 122333 ->22333 nr prime => 5
            pentru 8 -> 122333444455555666666777777788888888 ->22333555557777777 nr prime => 17
"""
start_time=time.time()

def eratosthenes(n):
    prime = [True for i in range(n + 1)]
    prime[0] = False
    prime[1] = False
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    return prime


def sump(l):
    output = [0] * len(l)
    s = 0
    for i in range(2, len(l)):
        if l[i] == True:
            s += i
            output[i] = s
    return output


T = []
N = int(input())
for i in range(N):
    T.append(int(input()))

prime = eratosthenes(max(T))
sum_prime = sump(prime)
for nr in T:
    if prime[nr] == True:
        print(sum_prime[nr])
    elif nr == 1 or nr == 0:
        print(0)
    else:
        for i in range(nr - 1, 2, -1):
            if prime[i] == True:
                print(sum_prime[i])
                break

print("time: ", (time.time() - start_time) * 10 ** 3, "ms")