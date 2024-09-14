import sys
input = sys.stdin.readline

N, X, K = map(int, input().split())
ans = X
for _ in range(K):
    A, B = map(int, input().split())
    if ans == A:
        ans = B
    elif ans == B:
        ans = A

print(ans)
