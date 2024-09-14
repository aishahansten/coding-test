import sys
input = sys.stdin.readline

M = int(input())
ans = 1
for _ in range(M):
    X, Y = map(int, input().split())
    if ans==X:
        ans = Y
    elif ans == Y:
        ans = X
    else:
        continue
print(ans)