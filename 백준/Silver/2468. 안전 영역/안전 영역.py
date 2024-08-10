import sys
input = sys.stdin.readline
from collections import deque


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# 최대 높이 찾아서 순환
maxHeight = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] > maxHeight:
            maxHeight = arr[i][j]

def BFS(i, j):
    global count
    q = deque([(i, j)])
    visited[i][j] = True
    count += 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<N and 0<=ny<N and visited[nx][ny] == False:
                visited[nx][ny] = True
                q.append((nx, ny))


countlist = []
for h in range(maxHeight):
    count = 0
    visited = [[False]*(N) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] <= h:
                visited[i][j] = True
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                BFS(i, j)
    countlist.append(count)

print(max(countlist))

