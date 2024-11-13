import sys
input = sys.stdin.readline

K, L = map(int, input().split())

cnt = 1
waiting = {}


for i in range(L):
    number = input().strip()
    waiting[number] = cnt
    cnt += 1

sorted_waiting = sorted(waiting.items(), key=lambda x:x[1])


cnt = 0
for item in sorted_waiting:
    print(item[0])
    cnt += 1
    if cnt == K:
        break