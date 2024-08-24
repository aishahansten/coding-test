import sys
input = sys.stdin.readline
from collections import deque
import copy 

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]



def bfs():
    q = deque()
    backup_arr = copy.deepcopy(arr)

    for i in range(N):
        for j in range(M):
            if backup_arr[i][j] == 2:
                q.append((i, j))

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if backup_arr[nx][ny] == 0:
                    backup_arr[nx][ny] = 2
                    q.append((nx, ny))

    global ans
    countsafe = 0
    for i in range(N):
        countsafe += backup_arr[i].count(0)
    # for l in range(N):
    #     for m in range(M):
    #         if backup_arr[l][m] == 0:
    #             countsafe += 1
    
    ans = max(ans, countsafe)


def buildWall(cnt):

    if cnt == 3:
        bfs()
        return
    
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                arr[i][j] = 1
                buildWall(cnt + 1)
                arr[i][j] = 0
ans = 0

buildWall(0)
print(ans)