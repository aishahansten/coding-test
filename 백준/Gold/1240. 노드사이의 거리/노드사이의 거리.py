import sys
input = sys.stdin.readline

def DFS(now, end):
    stack = [(now, 0)]
    visited = [False]*(N+1)
    visited[now] = True

    while stack:
        nowspot, nowlength = stack.pop()
        if nowspot == end:
            return nowlength
            
        for next in graph[nowspot]:
            nextspot, nextlength = next
            if not visited[nextspot]:
                stack.append((nextspot, nowlength+nextlength))
                visited[nextspot] = True
    

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b, l = map(int, input().split())
    graph[a].append((b, l))
    graph[b].append((a, l))

for _ in range(M):
    x, y = map(int, input().split())
    ans = DFS(x, y)
    print(ans)