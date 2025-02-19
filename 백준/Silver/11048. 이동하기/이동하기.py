import sys 
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dp_arr = [[0]*M for _ in range(N)]



dp_arr[0][0] = arr[0][0]



for i in range(1,N):
    dp_arr[i][0] = dp_arr[i-1][0] + arr[i][0]

for j in range(1, M):
    dp_arr[0][j] = dp_arr[0][j-1] + arr[0][j]

for i in range(1, N):
    for j in range(1, M):
        dp_arr[i][j] = max(dp_arr[i][j-1], dp_arr[i-1][j], dp_arr[i-1][j-1]) + arr[i][j]

print(dp_arr[N-1][M-1])
