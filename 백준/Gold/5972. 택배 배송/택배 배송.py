import sys
input = sys.stdin.readline
import heapq

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    start, end, cost = map(int, input().split())
    graph[start].append((cost, end))
    graph[end].append((cost, start))

costgraph = [int(1e9)]*(N+1)
def Dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    costgraph[start] = 0

    while q:
        nowcost, now = heapq.heappop(q)

        if nowcost > costgraph[now]:
            continue

        for nextcost, next in graph[now]:
            newcost = nowcost + nextcost
            if newcost < costgraph[next]:
                costgraph[next] = newcost
                heapq.heappush(q, (newcost, next))

Dijkstra(1)
print(costgraph[N])