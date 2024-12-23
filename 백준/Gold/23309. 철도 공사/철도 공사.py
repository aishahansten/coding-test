import sys
input = sys.stdin.readline
N, M = map(int, input().split())
stations = list(map(int, input().split()))
prev_sts = [0]*1000001
next_sts = [0]*1000001
for i in range(N):
    prev, next = stations[i-1], stations[(i+1)%N]
    prev_sts[stations[i]] = prev
    next_sts[stations[i]] = next

for _ in range(M):
    order = list(input().split())
    if order[0] == 'BN':
        i, j = int(order[1]), int(order[2])
        next_station = next_sts[i]
        print(next_station)

        prev_sts[j] = i
        next_sts[j] = next_station
        prev_sts[next_station] = j
        next_sts[i] = j

    elif order[0] == 'BP':
        i, j = int(order[1]), int(order[2])
        prev_station = prev_sts[i]
        print(prev_station)

        prev_sts[j] = prev_station
        next_sts[j] = i
        prev_sts[i] = j
        next_sts[prev_station] = j

    elif order[0] == 'CN':
        i = int(order[1])
        next_station = next_sts[i] 
        print(next_station)
        
        next_of_next_station = next_sts[next_station]
        next_sts[i] = next_of_next_station
        prev_sts[next_of_next_station] = i
  
    else:
        i = int(order[1])
        prev_station = prev_sts[i]
        print(prev_station)

        prev_of_prev_station = prev_sts[prev_station]
        next_sts[prev_of_prev_station] = i
        prev_sts[i] = prev_of_prev_station