n = int(input())
f = [0] * 400005
rez = 0

K = input()
d = K.split(" ")
dp = [int(i) for i in d]

dp.append(0)
dp.insert(0, 0)


for i in range(n, 0, -1):
    dp[i] += dp[i + 1]
    f[dp[i]] = 1

total = dp[1]

for i in range(n, 1, -1):
    suma = dp[i]  # sum of sequence [i, n]
    while suma < total and f[suma]:
        rez += 1
        suma += dp[i]

print(rez)




