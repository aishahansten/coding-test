import sys
input = sys.stdin.readline

matrix = [[0]*100 for _ in range(100)]
for i in range(4):
    xd, yd, xu, yu = map(int, input().split())

    for j in range(xd, xu):
        for k in range(yd, yu):
            matrix[j][k] += 1
S = 0
for l in range(100):
    for m in range(100):
        if matrix[l][m] != 0:
            S += 1

print(S)

