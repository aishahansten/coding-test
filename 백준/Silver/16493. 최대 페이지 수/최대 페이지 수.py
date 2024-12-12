import sys 
input = sys.stdin.readline

# N일 남음, M개 챕터
N, M = map(int, input().split())
array = [[0,0]]
for _ in range(M):
    array.append(list(map(int, input().split())))

dp = [[0 for _ in range(N+1)] for _ in range(M+1)]



for i in range(1, M+1):
    for j in range(1, N+1):
        day = array[i][0]
        page = array[i][1]

        if j < day:
            dp[i][j] = dp[i-1][j]

        elif j >= day:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-day] + page)

        
print(dp[M][N])