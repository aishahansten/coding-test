import sys
input = sys.stdin.readline
from collections import deque
K = int(input())
W, H = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(H)]

cnt = -1

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
hx = [-1, -2, -2, -1, 1, 2, 2, 1]
hy = [-2, -1, 1, 2, 2, 1, -1, -2]

def BFS():
    visited = [[[0]*(K+1) for _ in range(W)] for _ in range(H)]
    q = deque([[0,0,0]])

    visited[0][0][0] = 1

    while q:
        x, y, z = q.popleft()
        if x == H-1 and y == W-1:
            return visited[x][y][z] -1
        
        if z < K:
            for k in range(8):
                hi = x + hx[k]
                hj = y + hy[k]
                if 0 <= hi < H and 0 <= hj < W:
                    if matrix[hi][hj] != 1 and not visited[hi][hj][z+1]:
                        visited[hi][hj][z+1] = visited[x][y][z] + 1
                        q.append([hi, hj, z+1])

        for r in range(4):
            nx = x + dx[r]
            ny = y + dy[r]
            if 0 <= nx < H and 0 <= ny < W:
                if not matrix[nx][ny] and not visited[nx][ny][z]:
                    visited[nx][ny][z] = visited[x][y][z]+1
                    q.append([nx, ny, z])


    return -1

ans = BFS()
print(ans)