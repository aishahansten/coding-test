import sys
input = sys.stdin.readline
import heapq

N = int(input())
X = 0
how_many_people_have_used = [0]*N
current_status_of_computers = [0]*N
hq = []

for _ in range(N):
    P, Q = map(int, input().split())
    heapq.heappush(hq, (P,Q))

while hq:
    now = heapq.heappop(hq)
    for i in range(len(current_status_of_computers)):
        if current_status_of_computers[i] <= now[0]:
            if current_status_of_computers[i] == 0:
                X+=1
            current_status_of_computers[i] = now[1]
            how_many_people_have_used[i] += 1
            break

print(X)
for j in how_many_people_have_used:
    if j == 0:
        pass
    else:
        print(j, end=' ')