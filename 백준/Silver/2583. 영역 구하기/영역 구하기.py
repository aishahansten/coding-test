import sys
input = sys.stdin.readline
from collections import deque

M, N, K = map(int, input().split())
graph = [[False]*N for _ in range(M)]
for _ in range(K):
    ldx, ldy, rux, ruy = map(int, input().split())
    for i in range(ldy, ruy):
        for j in range(ldx, rux):
            graph[i][j] = True

dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def BFS(i, j):
    global count, size
    q = deque([(i, j)])
    graph[i][j] = True
    count += 1
    size = 1
    while q:
        x, y = q.popleft()
        for dx, dy in dir:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < M and 0 <= ny < N and graph[nx][ny] == False:
                graph[nx][ny] = True
                size += 1
                q.append((nx, ny))


count = 0
size_ls = []
for i in range(M):
    for j in range(N):
        if graph[i][j] == False:
            BFS(i, j)
            size_ls.append(size)
       
size_ls.sort()
print(count)
print(*size_ls)