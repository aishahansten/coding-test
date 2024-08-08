import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())
arr = [[] for _ in range(N+1)]
visited = [0]*(N+1)
for _ in range(M):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

def DFS(R):
    count = 1
    stack = [R]

    while stack:
        now = stack.pop()
        if visited[now] != 0:
            continue
        visited[now] = count
        count += 1
        arr[now].sort()
        for next in arr[now]:
            if visited[next] != 0:
                continue
            stack.append(next)

DFS(R)
for visit in visited[1:]:
    print(visit)