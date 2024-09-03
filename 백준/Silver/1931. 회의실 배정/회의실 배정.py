import sys
input = sys.stdin.readline

N = int(input())
time = []
for _ in range(N):
    start, end = map(int, input().split())
    time.append((end, start))

time.sort() #끝나는 시간이 빠른 순, 같다면 시작 시간이 빠른 순

cnt = 0
end = 0
for i in range(N):
    if end <= time[i][1]:
        end = time[i][0]
        cnt += 1

print(cnt)