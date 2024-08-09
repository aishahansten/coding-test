import sys
input = sys.stdin.readline
import heapq

N, K = map(int, input().split())

graph = [int(1e9)]*100001
dx = [("-1", 1), ("+1", 1), ("*2", 0)]
operations = {
    "-1": lambda x: x-1,
    "+1": lambda x: x+1,
    "*2": lambda x: x*2
}
def dijk(start):
    q = []
    heapq.heappush(q, (start, 0))
    graph[start] = 0

    while q:
        now, sec = heapq.heappop(q)

        if graph[now] < sec:
            continue

        for i, j in dx:
            next = operations[i](now)
            nextsec = sec + j
            if 0 <= next <= 100000 and graph[next] > nextsec:
                graph[next] = nextsec
                heapq.heappush(q, (next, nextsec))


dijk(N)
print(graph[K])