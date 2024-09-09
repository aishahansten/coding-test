import sys
input = sys.stdin.readline
import heapq

N = int(input())

X = 0
hq = []
cnt = [0]*(N)
current_status_of_computers = [0]*N
for _ in range(N):
    P, Q = map(int, input().split())
    heapq.heappush(hq, (P,Q))

# print(hq) [(10, 100), (20, 50), (30, 120), (60, 110), (80, 90)]

while hq:
    now = heapq.heappop(hq)
    for i in range(len(current_status_of_computers)):
        if current_status_of_computers[i] <= now[0]:
            if current_status_of_computers[i] == 0:
                X+=1
            current_status_of_computers[i] = now[1]
            cnt[i] += 1
            break
    

print(X)
for j in cnt:
    if j == 0:
        pass
    else:
        print(j, end=' ')