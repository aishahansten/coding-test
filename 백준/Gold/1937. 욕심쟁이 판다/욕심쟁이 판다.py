import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

N = int(input())
green = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

dp = [[-1]*N for _ in range(N)]

def DFS(sti, stj):
    if dp[sti][stj] == -1:
        dp[sti][stj] = 1
        for k in range(4):
            nx = sti + dx[k]
            ny = stj + dy[k]
            if 0 <= nx < N and 0 <= ny < N and green[nx][ny] > green[sti][stj]:
                dp[sti][stj] = max(dp[sti][stj], 1+ DFS(nx, ny))
                
    
    return dp[sti][stj]

move = 0
for i in range(N):
    for j in range(N):
        best = DFS(i, j)
        if best > move:
            move = best

print(move)