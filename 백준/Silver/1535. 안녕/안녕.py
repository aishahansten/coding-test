import sys 
input = sys.stdin.readline

N = int(input())
Larray = list(map(int, input().split()))
Jarray = list(map(int, input().split()))

# dp 배열 행: 1~N 번 사람
# dp 배열 열: 체력 0~99까지의 경우
# 체력 100 다 쓰는 경우는 제외해야되므로 99칸까지만 체크
dp = [[0 for _ in range(100)] for _ in range(N+1)]


for i in range(1, N+1):
    for j in range(1, 100):
        loss = Larray[i-1]
        joy = Jarray[i-1]

        if j < loss:
            dp[i][j] = dp[i-1][j]
        
        elif j >= loss:
            dp[i][j] = max(dp[i-1][j], joy + dp[i-1][j-loss])

print(dp[N][99])