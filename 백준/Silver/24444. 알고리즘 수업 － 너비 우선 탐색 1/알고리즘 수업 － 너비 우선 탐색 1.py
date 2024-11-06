import sys
input = sys.stdin.readline
from collections import deque

def BFS(R):
    global visited
    visited[R] = 1
    q = deque([R])
    cnt = 1
    while q:
        now = q.popleft()
        arr[now].sort()
        for next in arr[now]:
            if not visited[next]:
                cnt += 1
                visited[next] = cnt
                q.append(next)


    

N, M, R = map(int, input().split())
arr = [[] for _ in range(N+1)]
visited = [0]*(N+1)
for _ in range(M):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

BFS(R)

for i in range(1, N+1):
    print(visited[i])
