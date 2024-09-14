import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())

move = (K - 3) % N
ans = M + move
if ans > N:
    ans %= N
print(ans)