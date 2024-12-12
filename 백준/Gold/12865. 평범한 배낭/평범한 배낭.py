import sys
input = sys.stdin.readline

# N 물품수 K 한계 무게
N, K = map(int, input().split())
array = [[0,0]]
for _ in range(N):
    array.append(list(map(int, input().split())))

dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        weight = array[i][0]
        value = array[i][1]

        if j < weight:
            dp[i][j] = dp[i-1][j]

        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight]+value)

            
         
        
print(dp[N][K])